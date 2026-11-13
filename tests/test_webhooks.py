from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any

import httpx
import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from wavvon import (
    AppResponse,
    SlashInvocation,
    WebhookVerificationError,
    create_dispatch_handler,
    outgoing_webhook_signing_key,
    to_asgi,
    verify_dispatch,
    verify_outgoing_webhook,
    webhook_delivery_signing_bytes,
)

HUB_KEY = Ed25519PrivateKey.from_private_bytes(bytes([5]) * 32)
HUB_PUB = HUB_KEY.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()
NOW = 1_700_000_000

SLASH = json.dumps(
    {
        "type": "slash_command",
        "hub_url": "https://h",
        "channel_id": "c",
        "message_id_hint": "m",
        "author": {"pubkey": "p"},
        "command": "echo",
        "args_raw": "hi there",
        "args_tokens": ["hi", "there"],
    }
)


def signed(body: str, ts: int = NOW) -> dict[str, str]:
    sig = HUB_KEY.sign(webhook_delivery_signing_bytes(ts, body.encode()))
    return {"X-Wavvon-Hub-Pubkey": HUB_PUB, "X-Wavvon-Signature-V1": sig.hex(), "X-Wavvon-Timestamp": str(ts)}


def test_accepts_a_correctly_signed_invocation() -> None:
    inv = verify_dispatch(signed(SLASH), SLASH, HUB_PUB, now=NOW)
    assert inv["type"] == "slash_command"
    assert inv["command"] == "echo"


def test_refuses_tampering_staleness_missing_v1_and_a_foreign_hub() -> None:
    h = signed(SLASH)
    with pytest.raises(WebhookVerificationError):
        verify_dispatch(h, SLASH.replace("echo", "ban"), HUB_PUB, now=NOW)
    with pytest.raises(WebhookVerificationError):
        verify_dispatch(h, SLASH, HUB_PUB, now=NOW + 301)
    assert verify_dispatch(h, SLASH, HUB_PUB, now=NOW + 300)["type"] == "slash_command"
    no_v1 = {k: v for k, v in h.items() if k != "X-Wavvon-Signature-V1"}
    with pytest.raises(WebhookVerificationError):
        verify_dispatch(no_v1, SLASH, HUB_PUB, now=NOW)
    other = (
        Ed25519PrivateKey.from_private_bytes(bytes([6]) * 32).public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
    )
    with pytest.raises(WebhookVerificationError):
        verify_dispatch(h, SLASH, other.hex(), now=NOW)


def test_delivers_an_unknown_dispatch_type() -> None:
    body = json.dumps({"type": "modal_submit", "x": 1})
    d = verify_dispatch(signed(body), body, HUB_PUB, now=NOW)
    assert d["type"] == "unknown"
    assert d["raw_type"] == "modal_submit"


def echo(inv: SlashInvocation) -> AppResponse:
    return {"reply": {"body": inv["args_raw"]}, "ephemeral": True}


HANDLER = create_dispatch_handler(hub_public_key=HUB_PUB, now=NOW, on_slash_command=echo)


async def test_handler_answers_a_verified_invocation() -> None:
    res = await HANDLER("POST", signed(SLASH), SLASH.encode())
    assert res.status == 200
    assert json.loads(res.body) == {"reply": {"body": "hi there"}, "ephemeral": True}


async def test_handler_answers_401_to_an_unverified_one() -> None:
    assert (await HANDLER("POST", {}, SLASH.encode())).status == 401
    assert (await HANDLER("GET", {}, b"")).status == 405


async def test_asgi_adapter() -> None:
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=to_asgi(HANDLER)), base_url="http://app") as http:
        res = await http.post("/hook", content=SLASH, headers=signed(SLASH))
        assert res.status_code == 200
        assert res.json()["reply"]["body"] == "hi there"
        assert (await http.post("/hook", content=SLASH)).status_code == 401


SECRET = "BwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwc"
EVENT_BODY = json.dumps(
    {"type": "hub_event", "seq": 3, "event": "member.joined", "hub_url": "h", "at": NOW, "payload": {}}
)


def outgoing_headers() -> dict[str, Any]:
    key = outgoing_webhook_signing_key(SECRET)
    sig = hmac.new(key, webhook_delivery_signing_bytes(NOW, EVENT_BODY.encode()), hashlib.sha256).hexdigest()
    return {"x-wavvon-signature-v1": sig, "x-wavvon-timestamp": str(NOW)}


def test_outgoing_accepts_the_secret_as_shown_and_as_bytes() -> None:
    assert verify_outgoing_webhook(outgoing_headers(), EVENT_BODY, SECRET, now=NOW)["seq"] == 3
    headers = httpx.Headers(outgoing_headers())
    assert verify_outgoing_webhook(headers, EVENT_BODY, bytes([7]) * 32, now=NOW)["seq"] == 3


def test_outgoing_refuses_the_wrong_secret_or_a_replay() -> None:
    with pytest.raises(WebhookVerificationError):
        verify_outgoing_webhook(outgoing_headers(), EVENT_BODY, "AAAA", now=NOW)
    with pytest.raises(WebhookVerificationError):
        verify_outgoing_webhook(outgoing_headers(), EVENT_BODY, SECRET, now=NOW - 400)
