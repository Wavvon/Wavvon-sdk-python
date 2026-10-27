from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

import httpx
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from .errors import AuthSchemeError, HubError
from .retry import RetryOptions, fetch_with_retry, is_transient_status

AUTH_CHALLENGE_SCHEME = "tagged-v1"
_AUTH_TAG = b"wavvon/auth-challenge/v1\0"


class Identity(Protocol):
    """A keypair the program holds. The seed never leaves this object."""

    @property
    def public_key(self) -> str:
        """Ed25519 public key, lowercase hex."""
        ...

    def sign(self, message: bytes) -> bytes: ...


class _SeedIdentity:
    def __init__(self, key: Ed25519PrivateKey) -> None:
        self._key = key
        self._public_key = key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()

    @property
    def public_key(self) -> str:
        return self._public_key

    def sign(self, message: bytes) -> bytes:
        return self._key.sign(message)

    def __repr__(self) -> str:
        return f"Identity({self._public_key})"


def identity_from_seed(seed: str | bytes) -> Identity:
    """Builds an Identity from a 32-byte Ed25519 seed (hex or bytes) that the
    operator keeps in a file or environment variable. The SDK never sends the
    seed anywhere; only signatures leave the process."""
    secret = bytes.fromhex(seed.strip()) if isinstance(seed, str) else bytes(seed)
    if len(secret) != 32:
        raise ValueError("an Ed25519 seed is 32 bytes")
    return _SeedIdentity(Ed25519PrivateKey.from_private_bytes(secret))


def auth_challenge_signing_bytes(challenge: bytes, scheme: str | None) -> bytes:
    """The bytes a client signs to answer a challenge (wire-format.md, "Auth
    challenge answer"): the `tagged-v1` domain prefix plus the challenge. Any
    other scheme, or none, is refused rather than signed raw, so this can never
    be used to sign arbitrary bytes."""
    if scheme != AUTH_CHALLENGE_SCHEME:
        raise AuthSchemeError(f"unsupported auth challenge scheme {scheme!r}; only {AUTH_CHALLENGE_SCHEME} is signed")
    return _AUTH_TAG + challenge


@dataclass(frozen=True)
class Session:
    token: str
    scope: str
    """"member", or "lobby" on a hub that holds newcomers back."""
    canonical_pubkey: str
    """The identity the hub attributes this session's actions to."""


async def authenticate(
    hub_url: str,
    identity: Identity,
    *,
    invite_code: str | None = None,
    retry: RetryOptions | None = None,
    http: httpx.AsyncClient | None = None,
) -> Session:
    """Challenge, sign, verify. A transient failure at either step restarts from
    a fresh challenge, because the hub drops a pending challenge as soon as
    verify reads it. `invite_code` is needed once, on an invite_only hub.
    `http` is used as given and left open; without it one is made and closed."""
    if http is None:
        async with httpx.AsyncClient(timeout=None) as own:
            return await authenticate(hub_url, identity, invite_code=invite_code, retry=retry, http=own)
    base = hub_url.rstrip("/")

    async def attempt() -> httpx.Response:
        ch = await http.post(f"{base}/auth/challenge", json={"public_key": identity.public_key})
        if ch.status_code >= 300:
            return ch
        body: dict[str, Any] = ch.json()
        challenge: str = body["challenge"]
        signature = identity.sign(auth_challenge_signing_bytes(bytes.fromhex(challenge), body.get("scheme")))
        verify: dict[str, Any] = {
            "public_key": identity.public_key,
            "challenge": challenge,
            "signature": signature.hex(),
        }
        if invite_code is not None:
            verify["invite_code"] = invite_code
        return await http.post(f"{base}/auth/verify", json=verify)

    res = await fetch_with_retry(attempt, retry)
    if res.status_code >= 300 or is_transient_status(res.status_code):
        raise HubError(res.status_code, res.text)
    out: dict[str, Any] = res.json()
    return Session(
        token=out["token"],
        scope=out.get("scope") or "member",
        canonical_pubkey=out.get("canonical_pubkey") or identity.public_key,
    )
