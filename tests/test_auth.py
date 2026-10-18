from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from wavvon import (
    AuthSchemeError,
    HubError,
    RetryOptions,
    auth_challenge_signing_bytes,
    authenticate,
    identity_from_seed,
)

SEED = "5a" * 32
C32 = bytes([9]) * 32
FAST = RetryOptions(base_delay=0.001, max_delay=0.001)


def test_tagged_v1_prefixes_the_tag() -> None:
    b = auth_challenge_signing_bytes(C32, "tagged-v1")
    assert b[:25] == b"wavvon/auth-challenge/v1\0"
    assert b[25:] == C32


def test_raw_only_at_exactly_32_bytes() -> None:
    assert auth_challenge_signing_bytes(C32) == C32
    assert auth_challenge_signing_bytes(C32, None) == C32
    for n in (31, 64):
        with pytest.raises(AuthSchemeError):
            auth_challenge_signing_bytes(bytes(n))


def test_unknown_scheme_is_refused() -> None:
    for scheme in ("tagged-v2", ""):
        with pytest.raises(AuthSchemeError):
            auth_challenge_signing_bytes(C32, scheme)


def test_seed_as_hex_or_bytes() -> None:
    assert identity_from_seed(SEED).public_key == identity_from_seed(bytes.fromhex(SEED)).public_key
    with pytest.raises(ValueError):
        identity_from_seed("abcd")


class FakeHub:
    """Answers the challenge flow; `fail_verify` counts transient verifies."""

    def __init__(self, scheme: str | None = None, fail_verify: int = 0, verify_status: int | None = None) -> None:
        self.scheme = scheme
        self.fail_verify = fail_verify
        self.verify_status = verify_status
        self.challenges: list[str] = []
        self.verify: list[dict[str, Any]] = []
        self.http = httpx.AsyncClient(transport=httpx.MockTransport(self.handle))

    def handle(self, req: httpx.Request) -> httpx.Response:
        body = json.loads(req.content)
        if req.url.path == "/auth/challenge":
            ch = bytes([len(self.challenges) + 1]) * 32
            self.challenges.append(ch.hex())
            out: dict[str, Any] = {"challenge": ch.hex()}
            if self.scheme is not None:
                out["scheme"] = self.scheme
            return httpx.Response(200, json=out)
        self.verify.append(body)
        if self.fail_verify > 0:
            self.fail_verify -= 1
            return httpx.Response(503, text="busy")
        if self.verify_status:
            return httpx.Response(self.verify_status, text="This hub requires an invite code")
        msg = auth_challenge_signing_bytes(bytes.fromhex(body["challenge"]), self.scheme)
        try:
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(body["public_key"])).verify(
                bytes.fromhex(body["signature"]), msg
            )
        except InvalidSignature:
            return httpx.Response(401, text="Invalid signature")
        return httpx.Response(200, json={"token": "tok", "scope": "member", "canonical_pubkey": body["public_key"]})


async def test_logs_in_with_tagged_v1_and_passes_the_invite() -> None:
    hub = FakeHub("tagged-v1")
    s = await authenticate("http://hub/", identity_from_seed(SEED), invite_code="inv", http=hub.http)
    assert s.token == "tok"
    assert hub.verify[0]["invite_code"] == "inv"


async def test_restarts_from_a_fresh_challenge_after_a_transient_verify_failure() -> None:
    hub = FakeHub("tagged-v1", fail_verify=2)
    await authenticate("http://hub", identity_from_seed(SEED), retry=FAST, http=hub.http)
    assert len(hub.challenges) == 3
    assert len({v["challenge"] for v in hub.verify}) == 3


async def test_definitive_refusal_is_hub_error() -> None:
    hub = FakeHub("tagged-v1", verify_status=403)
    with pytest.raises(HubError) as e:
        await authenticate("http://hub", identity_from_seed(SEED), http=hub.http)
    assert e.value.status == 403


async def test_raw_scheme_login() -> None:
    hub = FakeHub(None)
    assert (await authenticate("http://hub", identity_from_seed(SEED), http=hub.http)).token == "tok"


async def test_never_sends_the_seed() -> None:
    hub = FakeHub("tagged-v1")
    await authenticate("http://hub", identity_from_seed(SEED), invite_code="x", http=hub.http)
    assert SEED not in json.dumps(hub.verify)
