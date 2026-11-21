# wavvon-sdk

[![PyPI](https://img.shields.io/pypi/v/wavvon-sdk)](https://pypi.org/project/wavvon-sdk/)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![CI](https://github.com/Wavvon/Wavvon-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/Wavvon/Wavvon-sdk-python/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

Write programs that talk to a [Wavvon](https://github.com/Wavvon) hub: bots,
apps with slash commands and buttons, event consumers, mini-app hosts, and
receivers for outgoing webhooks.

A program on Wavvon is a client like any other: an Ed25519 keypair, the same
challenge-response login, the same permissions. There is no bot account. What
makes a program an *app* is a role carrying `apps.register`. The design this
package implements is
[sdk.md](https://github.com/Wavvon/Wavvon-docs/blob/main/docs/sdk.md) (tier 1).

- Python 3.11 or later, asyncio, fully typed (`py.typed`, checked with `mypy --strict`).
- Depends on `httpx`, `websockets` and `cryptography`, plus `attrs`,
  `python-dateutil` and `typing-extensions` for the generated REST models.
- Apache-2.0, so a closed-source program can use it.

## Install

```sh
pip install wavvon-sdk
```

The import package is `wavvon`.

## Quick start

```python
import asyncio, os
import uvicorn  # any ASGI server; or call the handler from your own framework
from wavvon import WavvonClient, create_dispatch_handler, to_asgi


async def main() -> None:
    async with WavvonClient(
        "https://hub.example",
        seed=os.environ["WAVVON_SEED"],  # 32-byte Ed25519 seed, hex. Never sent anywhere.
        invite_code=os.environ.get("WAVVON_INVITE"),  # only needed the first time, on an invite-only hub
    ) as client:
        info = await client.info()
        app = to_asgi(
            create_dispatch_handler(
                hub_public_key=info["public_key"],
                on_slash_command=lambda inv: {"reply": {"body": f"you said: {inv['args_raw']}"}},
            )
        )

        await client.set_app_profile({"name": "Echo", "webhook_url": "https://bot.example/hook"})
        await client.set_app_commands([{"name": "echo", "description": "Repeat after me"}])

        events = client.connect()  # after set_app_profile, see below
        events.on("message", lambda e: print(e["message"].get("sender"), e["message"].get("content")))
        events.on("unknown", lambda e: print("new frame type:", e["raw_type"]))

        await uvicorn.Server(uvicorn.Config(app, port=8080)).serve()


asyncio.run(main())
```

A fuller one is [examples/echo_bot.py](examples/echo_bot.py).

Every REST route is a generated function under `wavvon.rest.api`; pass
`client.rest` and unwrap with `ok()`, which raises `HubError` on a refusal:

```python
from wavvon import ok
from wavvon.rest.api.channels import list_channels

channels = ok(await list_channels.asyncio_detailed(client=client.rest))
```

## What is in it

| Piece | Entry point |
|---|---|
| Login (challenge, sign, verify) that renews itself | `WavvonClient`, `authenticate`, `identity_from_seed` |
| Every REST route, typed from `openapi.yaml` | `wavvon.rest.api.*` with `client=client.rest`; `ok()` |
| Retry with backoff on 429, 5xx, timeouts | built into `client.rest`; `fetch_with_retry` |
| Capability checks | `client.has_capability`, `client.require_capability` |
| Keyset paging to the end of a list | `paginate` (async iterator) |
| WebSocket events with resume after reconnect | `client.connect()` -> `EventStream` |
| HTTP polling instead of a socket | `client.poll_events(cursor)` |
| App registration | `set_app_profile`, `set_app_commands`, `set_app_subscriptions` |
| Slash command and button webhooks | `create_dispatch_handler`, `verify_dispatch`, `to_asgi` |
| Outgoing webhook receiver | `verify_outgoing_webhook` |
| Mini-app host | `EventStream.announce_app`, `dismiss_app`, `send_mini_app_message` |

`create_dispatch_handler` returns a plain `async (method, headers, body) ->
WebhookResponse` function, so it fits any framework; `to_asgi` wraps it for
uvicorn, hypercorn, Starlette or FastAPI.

## End-to-end encrypted DMs

```python
await client.publish_dh_key()  # once per hub; without it nobody can encrypt to you
dms = client.dms()
conv = await dms.create_conversation([peer_pubkey])
await dms.send_text(conv.id, "hello")  # double ratchet; groups use sender keys
for m in await dms.poll(conv.id):  # call it when a `dm` event arrives
    print(m.sender, m.content.content if m.error is None else m.error)
```

A 1:1 sends the double-ratchet envelope and reads both it and the older static
one; groups use sender keys. Nothing is ever sent in the clear because
encryption failed: a peer without a key raises `RecipientHasNoKeyError`, a
changed key raises `DhKeyChangedError` until you call `accept_dh_key`, and
plaintext is the separate `send_plaintext`. DH pins, ratchet sessions and group
chains live in a `StateStore` (in memory by default): pass `store=` to
`WavvonClient` to keep them across restarts, since losing ratchet state makes
those conversations unreadable. Design: [sdk-dm.md](https://github.com/Wavvon/Wavvon-docs/blob/main/docs/sdk-dm.md).

## Voice

```python
voice = await client.join_voice(channel_id)  # publishes the DH key, joins, opens the audio session
await voice.send_opus(packet)  # one 20 ms Opus packet, paced to real time
async for ev in voice:  # Audio, Roster, Speaking, Zones, Position, ...
    if isinstance(ev, Audio):
        print(ev.from_pubkey, ev.ts, len(ev.opus))
await voice.leave()
```

Same wire as the desktop and web clients: signalling on the chat socket, audio
on a WebRTC data channel (`aiortc`; the hub must advertise `voice.webrtc`), every packet sealed with a per-sender key
wrapped to each listener's DH key. `send_opus` refuses anything but exactly
20 ms and holds each packet to its slot, so a file read faster than real time
is not flooded into the relay. `set_position` is coalesced to one update per
50 ms, `set_muted` and `set_deafened` are local, `Rejoining` and
`PositionRefused` are events, never fatal. For PCM in and out, install the
extra (`pip install wavvon-sdk[opus]`, which needs the libopus shared library)
and join with `pcm=True`; then `send_pcm(960 floats)` and `Audio.pcm` work.
Design: [sdk-voice.md](https://github.com/Wavvon/Wavvon-docs/blob/main/docs/sdk-voice.md).

## Capabilities each feature needs

Hubs say what they support in `GET /info` `capabilities`. The SDK checks those
strings and never compares version numbers. A feature the hub does not
advertise raises `UnsupportedByHubError`.

| Feature | Capability |
|---|---|
| `set_app_profile`, `set_app_commands`, `set_app_subscriptions`, embeds, game cards | `apps.register` |
| `verify_dispatch` / `verify_outgoing_webhook` (they require `X-Wavvon-Signature-V1`) | `webhooks.signedtimestamp` |
| Paging `GET /users`, `/conversations/{id}/messages`, `/admin/reports` | `list.cursor` |
| Paging bans, mutes, invites, pending, conversations, pins, polls | `list.cursor.lists` |
| `ping` / `pong` over the socket | `ws.ping` |
| `join_voice` | `channels.voice` |
| Signed plaintext DMs (`send_plaintext`), signed group changes | `dms.plaintext.v2`, `dms.group.signedmembers` |

Login, REST, the socket and polling need no capability.

## Behaviour you can rely on

- **A transient failure is never an answer.** 429, 5xx, timeouts and dropped
  connections are retried with capped exponential backoff and jitter. If the
  budget runs out you get `HubUnavailableError`, not an empty list or a 404.
  Set `RetryOptions(max_attempts=math.inf)` to wait forever.
- **Sessions renew themselves.** A 401 triggers one fresh login and a retry.
  `client.on_state_change` and `events.on_state_change` show when it is happening.
- **Unknown is delivered.** A socket frame or dispatch type this version does
  not model reaches you as `{"type": "unknown", "raw_type": ..., "raw": ...}`.
- **Missed events are replayed.** The event stream remembers the last
  `hub_event` seq and asks the hub to resume from it after every reconnect.
  If the gap is older than the hub keeps (72 hours) you get
  `replay_unavailable`. Register the app profile before `connect()`: the hub
  only pushes and replays events on a socket opened by a registered app.
- **The seed stays with you.** No call sends a seed or private key anywhere.

## Conformance

Every signed byte sequence is checked against the shared wire vectors in
Wavvon-server (`crates/identity/wire-vectors.json`): the auth challenge, the
Ed25519 dispatch signature, and the outgoing-webhook HKDF + HMAC. CI reads them
from Wavvon-server at commit `78ff4aab3ba905ef4480d02d47f24d63762cc697`.

The REST client was generated from Wavvon-docs at the commit in
[src/wavvon/rest/SPEC_COMMIT](src/wavvon/rest/SPEC_COMMIT).

## Licence

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
