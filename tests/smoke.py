"""Smoke test against a real hub, through the public API only. Not collected
by pytest: it needs a hub. scripts/smoke_local.py boots one and runs this.

    WAVVON_SMOKE_HUB            hub URL, e.g. http://localhost:3600
    WAVVON_SMOKE_INVITE         an invite whose role grants apps.register
    WAVVON_SMOKE_CHANNEL        optional channel id; default: the first text channel
    WAVVON_SMOKE_WEBHOOK_HOST   host the hub can reach this process at (default localhost)

Authenticates as a fresh identity, posts a message, registers a slash command,
invokes it, and checks that the verified invocation's reply lands in the channel.
"""

from __future__ import annotations

import asyncio
import os
import secrets
import socket
import sys
import time
from collections.abc import Callable
from typing import Any

import uvicorn

from wavvon import (
    AppResponse,
    MessageEvent,
    RetryInfo,
    RetryOptions,
    SlashInvocation,
    UnknownEvent,
    WavvonClient,
    create_dispatch_handler,
    ok,
    to_asgi,
)
from wavvon.rest.api.channels import list_channels
from wavvon.rest.api.messages import create_channel_message
from wavvon.rest.models.create_channel_message_body import CreateChannelMessageBody
from wavvon.rest.types import UNSET


def step(s: str) -> None:
    print(f"smoke: {s}", flush=True)


def report_retry(i: RetryInfo) -> None:
    step(f"retrying after {i.status or 'network error'} (attempt {i.attempt})")


async def wait_until(pred: Callable[[], Any], what: str) -> Any:
    deadline = time.monotonic() + 10.0
    while time.monotonic() < deadline:
        hit = pred()
        if hit:
            return hit
        await asyncio.sleep(0.05)
    raise TimeoutError(f"timed out waiting for {what}")


async def main() -> None:
    hub_url = os.environ.get("WAVVON_SMOKE_HUB")
    invite = os.environ.get("WAVVON_SMOKE_INVITE")
    if not hub_url or not invite:
        print("set WAVVON_SMOKE_HUB and WAVVON_SMOKE_INVITE", file=sys.stderr)
        sys.exit(2)

    async with WavvonClient(
        hub_url, seed=secrets.token_bytes(32), invite_code=invite, retry=RetryOptions(on_retry=report_retry)
    ) as client:
        session = await client.login()
        step(f"authenticated as {session.canonical_pubkey} ({session.scope})")
        await client.require_capability("apps.register")
        await client.require_capability("webhooks.signedtimestamp")
        info = await client.info()

        invocations: list[SlashInvocation] = []

        def on_slash(inv: SlashInvocation) -> AppResponse:
            invocations.append(inv)
            return {"reply": {"body": f"pong: {inv['args_raw']}"}}

        app = to_asgi(create_dispatch_handler(hub_public_key=info["public_key"], on_slash_command=on_slash))
        sock = socket.socket()
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
        server = uvicorn.Server(uvicorn.Config(app, log_level="warning"))
        serving = asyncio.create_task(server.serve(sockets=[sock]))
        webhook_url = f"http://{os.environ.get('WAVVON_SMOKE_WEBHOOK_HOST', 'localhost')}:{port}/hook"

        await client.set_app_profile(
            {"name": "SDK smoke", "description": "wavvon-sdk smoke test", "webhook_url": webhook_url}
        )
        await client.set_app_commands([{"name": "sdksmoke", "description": "Answers pong", "cooldown_seconds": 0}])
        step(f"registered /sdksmoke -> {webhook_url}")

        # After the profile, so the hub treats this socket as an app's.
        stream = client.connect()
        seen: list[dict[str, Any]] = []
        unknown: set[str] = set()

        def on_message(e: MessageEvent) -> None:
            seen.append(dict(e["message"]))

        def on_unknown(e: UnknownEvent) -> None:
            unknown.add(e["raw_type"])

        stream.on("message", on_message)
        stream.on("unknown", on_unknown)
        await wait_until(lambda: stream.state == "open", "the socket")
        step("socket open")

        channel_id = os.environ.get("WAVVON_SMOKE_CHANNEL")
        if not channel_id:
            channels = ok(await list_channels.asyncio_detailed(client=client.rest))
            channel_id = next(
                (
                    c.id
                    for c in channels
                    if not c.is_category and isinstance(c.id, str) and c.channel_type in (UNSET, "text")
                ),
                None,
            )
            if not channel_id:
                raise AssertionError("no text channel to post in")

        text = f"hello from wavvon-sdk {time.time()}"
        body = CreateChannelMessageBody(content=text)
        ok(await create_channel_message.asyncio_detailed(channel_id, client=client.rest, body=body))
        await wait_until(lambda: any(m.get("content") == text for m in seen), "our own message over the socket")
        step("posted a message and saw it come back")

        body = CreateChannelMessageBody(content="/sdksmoke ping")
        ok(await create_channel_message.asyncio_detailed(channel_id, client=client.rest, body=body))
        reply = await wait_until(
            lambda: next((m for m in seen if m.get("content") == "pong: ping"), None), "the slash command reply"
        )
        inv = invocations[0] if invocations else None
        if not inv or inv["command"] != "sdksmoke" or inv["args_raw"] != "ping":
            raise AssertionError(f"odd invocation {inv}")
        if reply.get("sender") != session.canonical_pubkey:
            raise AssertionError(f"reply sent by {reply.get('sender')}")
        step("verified the invocation and the reply landed")

        if unknown:
            step(f"frames this SDK does not model (delivered as unknown): {', '.join(sorted(unknown))}")
        await stream.close()
        server.should_exit = True
        await serving
    step("PASSED")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"smoke: FAILED: {e!r}", file=sys.stderr)
        raise
