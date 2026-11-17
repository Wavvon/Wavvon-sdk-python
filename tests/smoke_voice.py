"""Smoke test of voice against ONE real hub. Not collected by pytest. Every
assertion needs a decrypted frame, never a roster row. Nothing is played:
audio stays in memory.

    WAVVON_SMOKE_HUB        hub URL
    WAVVON_SMOKE_SEED       seed (64 hex) of a hub owner: it creates the channel and mints invites
                            (default 5a repeated)
    WAVVON_SMOKE_SECONDS    length of the sustained phase (default 20)
    WAVVON_RUST_VOICE_PEER  optional: a Rust SDK program that joins CHANNEL and sends a tone for
                            SECS seconds, reading HUB, SEED, INVITE, CHANNEL, SECS and TONE_OUT
                            (where it writes length-prefixed Opus packets) from the environment.
                            The sustained phase then runs against it instead of a second Python
                            instance.

Phases: sustained two-way traffic (frames, ctr gaps, resource counters), then
with a second Python instance: a 40 ms packet is refused, key rotation after a
leave and rejoin, proximity (coalescing, a creator-only refusal).
"""

from __future__ import annotations

import asyncio
import os
import secrets
import subprocess
import sys
import tempfile
import time
import tracemalloc
from collections import defaultdict
from pathlib import Path
from typing import Any

from wavvon import WavvonClient, identity_from_seed
from wavvon.voice import Audio, BadFrameError, Position, PositionRefused, Voice, Zones


def step(s: str) -> None:
    print(f"smoke-voice: {s}", flush=True)


def tone_packet() -> bytes:
    # A CELT fullband 20 ms packet (TOC 0xF8): any payload is decodable, which
    # is all a transport smoke needs without an encoder.
    return b"\xf8" + os.urandom(60)


class Tally:
    """What one voice session heard, per (speaker, key_id)."""

    def __init__(self, voice: Voice) -> None:
        self.frames: dict[tuple[str, int], int] = defaultdict(int)
        self.gaps: dict[tuple[str, int], int] = defaultdict(int)
        self.last_ctr: dict[tuple[str, int], int] = {}
        self.max_interval = 0.0
        self.last_at = 0.0
        self.zones: list[str] = []
        self.positions: list[list[float]] = []
        self.refused: list[str] = []
        self.failures: list[Exception] = []
        self.task = asyncio.get_running_loop().create_task(self._drain(voice))

    async def _drain(self, voice: Voice) -> None:
        from wavvon.voice import Failure

        async for ev in voice:
            if isinstance(ev, Audio):
                k = (ev.from_pubkey, ev.key_id)
                now = time.monotonic()
                if self.last_at:
                    self.max_interval = max(self.max_interval, now - self.last_at)
                self.last_at = now
                self.frames[k] += 1
                if k in self.last_ctr and ev.ctr > self.last_ctr[k] + 1:
                    self.gaps[k] += ev.ctr - self.last_ctr[k] - 1
                self.last_ctr[k] = ev.ctr
            elif isinstance(ev, Zones):
                self.zones = [z.zone_id for z in ev.zones]
            elif isinstance(ev, Position):
                self.positions.append(ev.position)
            elif isinstance(ev, PositionRefused):
                self.refused.append(ev.reason)
            elif isinstance(ev, Failure):
                self.failures.append(ev.error)

    def from_(self, pub: str, min_key: int = 1) -> int:
        return sum(n for (p, k), n in self.frames.items() if p == pub and k >= min_key)


async def until(what: str, ok: Any, seconds: float = 20.0) -> None:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if ok():
            return
        await asyncio.sleep(0.05)
    raise TimeoutError(f"timed out waiting for {what}")


async def new_member(hub: str, owner: WavvonClient) -> WavvonClient:
    seed = secrets.token_hex(32)
    invite = await owner.json_call("POST", "/invites", json={"bound_pubkey": identity_from_seed(seed).public_key})
    client = WavvonClient(hub, seed=seed, invite_code=invite["code"])
    await client.login()
    return client


async def send_for(voice: Voice, seconds: float, packets: list[bytes]) -> int:
    end, n = time.monotonic() + seconds, 0
    while time.monotonic() < end:
        await voice.send_opus(packets[n % len(packets)])
        n += 1
    return n


def read_tone(path: Path) -> list[bytes]:
    raw, out, i = path.read_bytes(), [], 0
    while i < len(raw):
        n = int.from_bytes(raw[i : i + 2], "big")
        out.append(raw[i + 2 : i + 2 + n])
        i += 2 + n
    return out


async def sustained(hub: str, owner: WavvonClient, channel: str, a: WavvonClient, seconds: int) -> None:
    peer_proc: subprocess.Popen[bytes] | None = None
    peer_pub: str
    tone_file = Path(tempfile.mkdtemp(prefix="wavvon-py-voice-")) / "tone.bin"
    b: WavvonClient | None = None
    peer_bin = os.environ.get("WAVVON_RUST_VOICE_PEER")
    if peer_bin:
        seed = secrets.token_hex(32)
        peer_pub = identity_from_seed(seed).public_key
        invite = await owner.json_call("POST", "/invites", json={"bound_pubkey": peer_pub})
        peer_proc = subprocess.Popen(  # noqa: ASYNC220
            [peer_bin],
            env={
                **os.environ,
                "HUB": hub,
                "SEED": seed,
                "INVITE": invite["code"],
                "CHANNEL": channel,
                "SECS": str(seconds + 4),
                "TONE_OUT": str(tone_file),
            },
        )
        await until("the Rust peer's tone file", tone_file.exists, 60)
        await asyncio.sleep(1)
        packets = read_tone(tone_file)
    else:
        b = await new_member(hub, owner)
        peer_pub = b.identity.public_key
        packets = [tone_packet() for _ in range(500)]

    tracemalloc.start()
    va = await a.join_voice(channel)
    seen_a = Tally(va)
    vb = seen_b = None
    if b is not None:
        vb = await b.join_voice(channel)
        seen_b = Tally(vb)
    me = a.identity.public_key
    step(f"sustained phase: {seconds} s against {'the Rust SDK' if peer_bin else 'a second Python instance'}")
    await asyncio.sleep(3)  # key distribution
    started = time.monotonic()
    sender = asyncio.ensure_future(send_for(va, seconds, packets))
    other = asyncio.ensure_future(send_for(vb, seconds, packets)) if vb is not None else None
    mark = 0
    while not sender.done():
        await asyncio.sleep(min(60, max(1, seconds / 5)))
        cur, _ = tracemalloc.get_traced_memory()
        heard = seen_a.from_(peer_pub)
        step(
            f"t={time.monotonic() - started:5.0f}s heard {heard} (+{heard - mark}) from the peer, "
            f"traced {cur // 1024} KiB, tasks {len(va._tasks)}, marks {len(va._marks)}, "
            f"queued events {va._events.qsize()}, remote keys {len(va._remote)}"
        )
        mark = heard
    sent = await sender
    if other is not None:
        await other
    await asyncio.sleep(3)
    heard_by_a = seen_a.from_(peer_pub)
    gaps_a = sum(seen_a.gaps.values())
    step(f"python sent {sent} frames in {seconds} s ({sent / seconds:.1f}/s), heard {heard_by_a}, ctr gaps {gaps_a}")
    assert heard_by_a >= 0.95 * seconds * 50, f"heard only {heard_by_a} of ~{seconds * 50}"
    assert gaps_a <= 0.02 * seconds * 50, f"too many ctr gaps: {gaps_a}"
    assert not seen_a.failures, seen_a.failures
    if seen_b is not None:
        heard_by_b = seen_b.from_(me)
        step(f"second python heard {heard_by_b} of {sent}, gaps {sum(seen_b.gaps.values())}")
        assert heard_by_b >= 0.95 * sent
    if peer_proc is not None:
        peer_proc.wait(timeout=60)
    step(f"max interval between two frames heard by Python: {seen_a.max_interval * 1000:.0f} ms")
    if vb is not None:
        await vb.leave()
    await va.leave()
    if b is not None:
        await b.aclose()
    tracemalloc.stop()


async def features(hub: str, owner: WavvonClient, channel: str, a: WavvonClient) -> None:
    b = await new_member(hub, owner)
    a_pub, b_pub = a.identity.public_key, b.identity.public_key
    va, vb = await a.join_voice(channel), await b.join_voice(channel)
    seen_a, seen_b = Tally(va), Tally(vb)
    await asyncio.sleep(2)
    pk = tone_packet()

    try:
        await va.send_opus(b"\xf9\x00\x00")  # 40 ms
    except BadFrameError:
        step("a 40 ms packet is refused before anything is sent")
    else:
        raise AssertionError("a 40 ms packet was accepted")

    await send_for(va, 2, [pk])
    await until("B to decrypt A", lambda: seen_b.from_(a_pub) >= 90)
    await send_for(vb, 2, [pk])
    await until("A to decrypt B", lambda: seen_a.from_(b_pub) >= 90)
    step("both directions decrypt (key_id 1)")

    await vb.leave()
    await asyncio.sleep(1)
    vb2 = await b.join_voice(channel)
    seen_b2 = Tally(vb2)
    await asyncio.sleep(2)
    await send_for(va, 2, [pk])
    await until("the rejoined B to decrypt A at key_id >= 2", lambda: seen_b2.from_(a_pub, 2) >= 90)
    step("after B left, A rotated to key_id >= 2 and the rejoined B decrypts it")

    await owner_zone(hub, a, va, seen_b2, vb2)
    await va.leave()
    await vb2.leave()
    await b.aclose()


async def owner_zone(hub: str, owner: WavvonClient, va: Voice, seen_b: Tally, vb: Voice) -> None:
    await va.create_zone("smoke-zone", "smoke", "2d", None, "any_channel_member")
    await until(
        "both to see the zone",
        lambda: "smoke-zone" in seen_b.zones and any(z.zone_id == "smoke-zone" for z in va.zones),
    )
    for i in range(10):
        va.set_position("smoke-zone", [10.0 + i, 50.0])
        await asyncio.sleep(0.01)
    await until("B to see the last position", lambda: seen_b.positions[-1:] == [[19.0, 50.0]])
    step(f"ten positions in 100 ms coalesced to {len(seen_b.positions)}, ending at the last")
    assert len(seen_b.positions) <= 4
    await va.create_zone("own-zone", "own", "2d", None, "creator_only")
    await until("B to see the creator-only zone", lambda: any(z.zone_id == "own-zone" for z in vb.zones))
    vb.set_position("own-zone", [1.0, 1.0])
    await until("B to be refused", lambda: bool(seen_b.refused))
    step(f"B's position in a creator-only zone was refused: {seen_b.refused[0]}")


async def main() -> int:
    hub = os.environ["WAVVON_SMOKE_HUB"]
    seconds = int(os.environ.get("WAVVON_SMOKE_SECONDS", "20"))
    owner = WavvonClient(hub, seed=os.environ.get("WAVVON_SMOKE_SEED", "5a" * 32))
    name = f"py-voice-{secrets.token_hex(3)}"
    await owner.json_call("POST", "/channels", json={"name": name, "channel_type": "voice"})
    channels = await owner.json_call("GET", "/channels")
    channel = next(c["id"] for c in channels if c["name"] == name)
    a = await new_member(hub, owner)
    # The owner holds channels.manage, so it creates the zones; a plain member would not.
    await sustained(hub, owner, channel, a, seconds)
    await features(hub, owner, channel, owner)
    await a.aclose()
    await owner.aclose()
    print("VOICE SMOKE OK")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
