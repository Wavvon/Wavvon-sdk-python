from __future__ import annotations

import base64
import hashlib
import hmac
import inspect
import json
import re
import time
from collections.abc import Awaitable, Callable, Mapping, MutableMapping
from dataclasses import dataclass, field
from typing import Any, Literal, TypedDict, cast

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from .errors import WebhookVerificationError
from .events import HubEvent

# Wire shapes (Wavvon-server crates/hub/src/routes/app_models.rs)


class _AuthorBase(TypedDict):
    pubkey: str


class AuthorInfo(_AuthorBase, total=False):
    display_name: str


class SlashInvocation(TypedDict):
    type: Literal["slash_command"]
    hub_url: str
    channel_id: str
    message_id_hint: str
    author: AuthorInfo
    command: str
    args_raw: str
    args_tokens: list[str]


class ComponentInteraction(TypedDict):
    type: Literal["component_interaction"]
    hub_url: str
    channel_id: str
    message_id: str
    custom_id: str
    values: list[str]
    user: AuthorInfo


class UnknownDispatch(TypedDict):
    """A verified dispatch whose `type` this SDK does not know. Delivered, never dropped."""

    type: Literal["unknown"]
    raw_type: str
    raw: dict[str, Any]


Dispatch = SlashInvocation | ComponentInteraction | UnknownDispatch


class EmbedField(TypedDict, total=False):
    name: str
    value: str
    inline: bool


class Embed(TypedDict, total=False):
    title: str
    url: str
    description: str
    color: str
    fields: list[EmbedField]
    thumbnail_url: str
    image_url: str
    footer: dict[str, str]


class SelectOption(TypedDict, total=False):
    label: str
    value: str
    description: str


class AppComponent(TypedDict, total=False):
    type: Literal["button", "select"]
    custom_id: str
    label: str
    style: str
    disabled: bool
    placeholder: str
    min_values: int
    max_values: int
    options: list[SelectOption]


class ComponentRow(TypedDict):
    type: Literal["row"]
    components: list[AppComponent]


class GameLaunchCard(TypedDict, total=False):
    entry_url: str
    name: str
    description: str
    thumbnail_url: str


class Reply(TypedDict, total=False):
    body: str
    embeds: list[Embed]
    components: list[ComponentRow]
    reply_to: str


class Reaction(TypedDict):
    message_id: str
    emoji: str


class AppResponse(TypedDict, total=False):
    """What a slash command handler answers. `ephemeral`: only the invoker sees
    the reply. `defer`: the app will post later on its own. `game`: a "Play"
    card attached to the reply, ignored without one."""

    reply: Reply
    ephemeral: bool
    reactions: list[Reaction]
    defer: bool
    game: GameLaunchCard


class ComponentUpdate(TypedDict, total=False):
    body: str
    components: list[ComponentRow]


class EphemeralReply(TypedDict):
    body: str


class ComponentResponse(TypedDict, total=False):
    """What a component interaction handler answers."""

    update: ComponentUpdate
    ephemeral_reply: EphemeralReply
    defer: bool


class OutgoingWebhookEvent(HubEvent, total=False):
    """The outgoing-webhook envelope: a hub_event plus delivery fields."""

    webhook_id: str
    truncated: bool


# Signing bytes (wire-format.md, "Webhook delivery")

_DELIVERY_TAG = b"wavvon/webhook-delivery/v1\0"


def webhook_delivery_signing_bytes(timestamp: int, body: bytes) -> bytes:
    """`"wavvon/webhook-delivery/v1\\0" || u64le(timestamp) || body`."""
    return _DELIVERY_TAG + timestamp.to_bytes(8, "little") + body


def outgoing_webhook_signing_key(secret: str | bytes) -> bytes:
    """The HMAC key for an outgoing webhook: HKDF-SHA256 over the secret's
    decoded bytes, salt "wavvon-webhook-signing", empty info. A str is the
    secret as the admin was shown it (base64url, no padding); bytes are the
    decoded secret."""
    raw = _b64url_decode(secret.strip()) if isinstance(secret, str) else secret
    return HKDF(algorithm=SHA256(), length=32, salt=b"wavvon-webhook-signing", info=b"").derive(raw)


def _b64url_decode(s: str) -> bytes:
    if not re.fullmatch(r"[A-Za-z0-9_-]*", s):
        raise ValueError("secret is not base64url")
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


# Verification


def _header(headers: Mapping[str, str], name: str) -> str | None:
    want = name.lower()
    for k, v in headers.items():
        if k.lower() == want:
            return v
    return None


def _signed_timestamp(headers: Mapping[str, str], now: float | None, tolerance_sec: int) -> tuple[int, bytes]:
    sig_hex = _header(headers, "X-Wavvon-Signature-V1")
    ts_text = _header(headers, "X-Wavvon-Timestamp")
    if not sig_hex or not ts_text:
        raise WebhookVerificationError("missing X-Wavvon-Signature-V1 or X-Wavvon-Timestamp")
    if not re.fullmatch(r"\d{1,20}", ts_text):
        raise WebhookVerificationError("malformed X-Wavvon-Timestamp")
    ts = int(ts_text)
    current = int(time.time() if now is None else now)
    if abs(current - ts) > tolerance_sec:
        raise WebhookVerificationError("timestamp outside the allowed window")
    try:
        return ts, bytes.fromhex(sig_hex)
    except ValueError:
        raise WebhookVerificationError("malformed signature") from None


def _as_bytes(body: bytes | str) -> bytes:
    return body.encode("utf-8") if isinstance(body, str) else body


def _parse_json(body: bytes) -> dict[str, Any]:
    try:
        v = json.loads(body)
    except ValueError:
        v = None
    if not isinstance(v, dict):
        raise WebhookVerificationError("body is not a JSON object")
    return v


def verify_dispatch(
    headers: Mapping[str, str],
    raw_body: bytes | str,
    hub_public_key: str,
    *,
    now: float | None = None,
    tolerance_sec: int = 300,
) -> Dispatch:
    """Verifies a slash command or component dispatch and decodes it.
    `hub_public_key` is the hub's key as the program pinned it (GET /info
    `public_key`); the X-Wavvon-Hub-Pubkey header is only compared against it,
    never trusted. Pass the raw request bytes: re-serialised JSON will not verify."""
    body = _as_bytes(raw_body)
    sent = _header(headers, "X-Wavvon-Hub-Pubkey")
    if sent is not None and sent.lower() != hub_public_key.lower():
        raise WebhookVerificationError("signed by a different hub")
    ts, sig = _signed_timestamp(headers, now, tolerance_sec)
    try:
        Ed25519PublicKey.from_public_bytes(bytes.fromhex(hub_public_key)).verify(
            sig, webhook_delivery_signing_bytes(ts, body)
        )
    except (InvalidSignature, ValueError):
        raise WebhookVerificationError("bad signature") from None
    raw = _parse_json(body)
    if raw.get("type") in ("slash_command", "component_interaction"):
        return cast(Dispatch, raw)
    return {"type": "unknown", "raw_type": str(raw.get("type")), "raw": raw}


def verify_outgoing_webhook(
    headers: Mapping[str, str],
    raw_body: bytes | str,
    secret: str | bytes,
    *,
    now: float | None = None,
    tolerance_sec: int = 300,
) -> OutgoingWebhookEvent:
    """Verifies an outgoing-webhook delivery (HMAC-SHA256) and decodes its
    hub_event envelope. `secret` is what the admin copied when the webhook was
    created or rotated."""
    body = _as_bytes(raw_body)
    ts, sig = _signed_timestamp(headers, now, tolerance_sec)
    key = outgoing_webhook_signing_key(secret)
    expected = hmac.new(key, webhook_delivery_signing_bytes(ts, body), hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        raise WebhookVerificationError("bad signature")
    return cast(OutgoingWebhookEvent, _parse_json(body))


# A framework-agnostic handler: method, headers and raw body in, response out.


@dataclass(frozen=True)
class WebhookResponse:
    status: int
    body: bytes
    headers: dict[str, str] = field(default_factory=dict)


WebhookHandler = Callable[[str, Mapping[str, str], bytes], Awaitable[WebhookResponse]]


async def _call(fn: Callable[[Any], Any] | None, arg: Any) -> Any:
    if fn is None:
        return None
    result = fn(arg)
    return await result if inspect.isawaitable(result) else result


def create_dispatch_handler(
    *,
    hub_public_key: str,
    on_slash_command: Callable[[SlashInvocation], AppResponse | Awaitable[AppResponse]] | None = None,
    on_component: Callable[[ComponentInteraction], ComponentResponse | Awaitable[ComponentResponse]] | None = None,
    on_unknown: Callable[[UnknownDispatch], Any] | None = None,
    now: float | None = None,
    tolerance_sec: int = 300,
) -> WebhookHandler:
    """A handler for the app's webhook_url. Refuses anything that does not
    verify with 401; answers a verified dispatch with the handler's JSON (`{}`
    when there is no handler for it). The hub waits 5 s for the answer.
    Callbacks may be plain functions or coroutines."""

    async def handle(method: str, headers: Mapping[str, str], body: bytes) -> WebhookResponse:
        if method.upper() != "POST":
            return WebhookResponse(405, b"method not allowed")
        try:
            dispatch = verify_dispatch(headers, body, hub_public_key, now=now, tolerance_sec=tolerance_sec)
        except WebhookVerificationError as e:
            return WebhookResponse(401, str(e).encode())
        if dispatch["type"] == "slash_command":
            answer = await _call(on_slash_command, dispatch)
        elif dispatch["type"] == "component_interaction":
            answer = await _call(on_component, dispatch)
        else:
            answer = await _call(on_unknown, dispatch)
        return WebhookResponse(200, json.dumps(answer or {}).encode(), {"content-type": "application/json"})

    return handle


AsgiScope = MutableMapping[str, Any]
AsgiReceive = Callable[[], Awaitable[MutableMapping[str, Any]]]
AsgiSend = Callable[[MutableMapping[str, Any]], Awaitable[None]]
AsgiApp = Callable[[AsgiScope, AsgiReceive, AsgiSend], Awaitable[None]]


def to_asgi(handler: WebhookHandler) -> AsgiApp:
    """Adapts a handler to an ASGI app (uvicorn, hypercorn, or mounted in
    Starlette/FastAPI)."""

    async def app(scope: AsgiScope, receive: AsgiReceive, send: AsgiSend) -> None:
        if scope["type"] == "lifespan":
            while True:
                msg = await receive()
                if msg["type"] == "lifespan.startup":
                    await send({"type": "lifespan.startup.complete"})
                elif msg["type"] == "lifespan.shutdown":
                    await send({"type": "lifespan.shutdown.complete"})
                    return
        if scope["type"] != "http":
            return
        body = b""
        more = True
        while more:
            msg = await receive()
            body += msg.get("body", b"")
            more = msg.get("more_body", False)
        headers = {k.decode("latin-1"): v.decode("latin-1") for k, v in scope["headers"]}
        res = await handler(scope["method"], headers, body)
        await send(
            {
                "type": "http.response.start",
                "status": res.status,
                "headers": [(k.encode("latin-1"), v.encode("latin-1")) for k, v in res.headers.items()],
            }
        )
        await send({"type": "http.response.body", "body": res.body})

    return app
