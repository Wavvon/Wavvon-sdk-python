"""Smoke test of E2E DMs against ONE real hub and the Rust SDK's `dm_echo`
example as the peer, 1:1 and group. Not collected by pytest.

    WAVVON_SMOKE_HUB     hub URL
    WAVVON_SMOKE_SEED    seed (64 hex) of a hub owner, which mints the invites (default 5a repeated)
    WAVVON_RUST_DM_ECHO  path to the built `dm_echo` example of Wavvon-sdk-rust

Every assertion needs a decrypted message, never a roster row.
"""

from __future__ import annotations

import asyncio
import os
import secrets
import subprocess
import sys
import time
from collections.abc import Awaitable, Callable
from typing import Any

from wavvon import DmError, DmErrorReason, WavvonClient, identity_from_seed


def step(s: str) -> None:
    print(f"smoke-dm: {s}", flush=True)


async def joined(hub: str, owner: WavvonClient, seed: str | None = None) -> tuple[WavvonClient, str]:
    seed = seed or secrets.token_hex(32)
    pub = identity_from_seed(seed).public_key
    invite = await owner.json_call("POST", "/invites", json={"bound_pubkey": pub})
    client = WavvonClient(hub, seed=seed, invite_code=invite["code"])
    await client.login()
    await client.publish_dh_key()
    return client, invite["code"]


async def until(what: str, probe: Callable[[], Awaitable[Any]], seconds: float = 30.0) -> Any:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        hit = await probe()
        if hit:
            return hit
        await asyncio.sleep(0.3)
    raise TimeoutError(f"timed out waiting for {what}")


READ: dict[tuple[int, str], list[str]] = {}


def poller(client: WavvonClient, conv: str, want: str) -> Callable[[], Awaitable[bool]]:
    """Poll hands each message out once, so what was read is kept per client and conversation."""
    seen = READ.setdefault((id(client), conv), [])

    async def probe() -> bool:
        for m in await client.dms().poll(conv):
            if isinstance(m.error, DmError) and m.error.reason is DmErrorReason.OWN_MESSAGE:
                continue
            if m.error is not None:
                raise AssertionError(f"could not read {m.id}: {m.error!r}")
            seen.append(m.content.content)
        return want in seen

    return probe


async def main() -> int:
    hub = os.environ["WAVVON_SMOKE_HUB"]
    echo_bin = os.environ["WAVVON_RUST_DM_ECHO"]
    owner = WavvonClient(hub, seed=os.environ.get("WAVVON_SMOKE_SEED", "5a" * 32))
    me, _ = await joined(hub, owner)
    carol, _ = await joined(hub, owner)
    echo_seed = secrets.token_hex(32)
    echo_pub = identity_from_seed(echo_seed).public_key
    invite = await owner.json_call("POST", "/invites", json={"bound_pubkey": echo_pub})
    echo = subprocess.Popen(  # noqa: ASYNC220
        [echo_bin],
        env={**os.environ, "WAVVON_HUB": hub, "WAVVON_SEED": echo_seed, "WAVVON_INVITE": invite["code"]},
    )
    try:
        step(f"python {me.identity.public_key[:8]}, rust echo {echo_pub[:8]}")
        probe = me.peer_dh_key
        await until("the Rust program's DH key", lambda: _has_key(probe, echo_pub))

        dms = me.dms()
        conv = (await dms.create_conversation([echo_pub])).id
        for i in range(3):
            sent = await dms.send_text(conv, f"hello {i}")
            await until(f"echo of hello {i}", poller(me, conv, f"echo: hello {i}"))
            assert sent.id
        step("1:1: three messages out, three echoes decrypted (ratchet stepped both ways)")

        group = (await dms.create_conversation([echo_pub, carol.identity.public_key])).id
        sent = await dms.send_text(group, "group hi")
        assert sent.distribution is not None and sorted(sent.distribution.delivered) == sorted(
            [echo_pub, carol.identity.public_key]
        ), sent.distribution
        await until("echo in the group", poller(me, group, "echo: group hi"))
        await until("carol reading Python's group message", poller(carol, group, "group hi"))
        await until("carol reading the Rust echo", poller(carol, group, "echo: group hi"))
        step("group: Rust and a second Python member read Python's message; Python and carol read Rust's")

        dist = await dms.rotate_group_key(group)
        assert dist.version == 2 and not dist.skipped
        await dms.send_text(group, "after rotate")
        await until("echo after rotation", poller(me, group, "echo: after rotate"))
        await until("carol after rotation", poller(carol, group, "after rotate"))
        step("group: rotated to version 2, both still read")

        refused = await dms.send_plaintext(conv, "explicit plaintext")
        assert refused.id
        step("explicit plaintext is a separate call and was accepted")
        print("DM SMOKE OK")
        return 0
    finally:
        echo.kill()
        echo.wait()
        for c in (me, carol, owner):
            await c.aclose()


async def _has_key(probe: Callable[[str], Awaitable[bytes]], pub: str) -> bool:
    from wavvon import RecipientHasNoKeyError

    try:
        await probe(pub)
    except RecipientHasNoKeyError:
        return False
    return True


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
