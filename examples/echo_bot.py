"""Echoes every message in the channels it can read, and answers /echo.

    WAVVON_HUB=https://hub.example  WAVVON_SEED=<64 hex chars> \\
    WAVVON_INVITE=<code, first run only>  WAVVON_WEBHOOK_URL=https://bot.example/hook \\
    PORT=8080 python examples/echo_bot.py

Needs `pip install uvicorn`. The identity needs a role carrying apps.register
to register /echo. The hub POSTs invocations to WAVVON_WEBHOOK_URL, which must
reach PORT here.
"""

from __future__ import annotations

import asyncio
import os

import uvicorn

from wavvon import (
    AppResponse,
    MessageEvent,
    SlashInvocation,
    UnknownEvent,
    WavvonClient,
    create_dispatch_handler,
    to_asgi,
)
from wavvon.rest.api.messages import create_channel_message
from wavvon.rest.models.create_channel_message_body import CreateChannelMessageBody


def echo(inv: SlashInvocation) -> AppResponse:
    return {"reply": {"body": inv["args_raw"] or "(nothing to echo)"}, "ephemeral": True}


async def main() -> None:
    async with WavvonClient(
        os.environ["WAVVON_HUB"], seed=os.environ["WAVVON_SEED"], invite_code=os.environ.get("WAVVON_INVITE")
    ) as client:
        me = (await client.login()).canonical_pubkey
        hub_public_key = (await client.info())["public_key"]

        app = to_asgi(create_dispatch_handler(hub_public_key=hub_public_key, on_slash_command=echo))
        server = uvicorn.Server(uvicorn.Config(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080"))))

        await client.set_app_profile({"name": "Echo", "webhook_url": os.environ["WAVVON_WEBHOOK_URL"]})
        await client.set_app_commands(
            [{"name": "echo", "description": "Repeat what you say, to you only", "args": "<text>"}]
        )

        events = client.connect()
        events.on_state_change(lambda s: print(f"socket: {s}"))

        def unmodelled(e: UnknownEvent) -> None:
            print(f"unmodelled frame: {e['raw_type']}")

        async def on_message(e: MessageEvent) -> None:
            m = e["message"]
            content = m.get("content", "")
            if m.get("sender") == me or m.get("visible_to_pubkey") or content.startswith("/"):
                return
            await create_channel_message.asyncio_detailed(
                e["channel_id"], client=client.rest, body=CreateChannelMessageBody(content=f"echo: {content}")
            )

        events.on("unknown", unmodelled)
        events.on("message", on_message)
        await server.serve()
        await events.close()


if __name__ == "__main__":
    asyncio.run(main())
