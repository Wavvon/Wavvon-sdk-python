"""The program's X25519 key and its peers': publish, look up, verify, pin. One
key serves DMs and voice (sdk-voice.md section 2, sdk-dm.md section 1)."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote

from .errors import DhKeyChangedError, DhKeyUnsignedError, HubError, RecipientHasNoKeyError
from .wire import dh_key_record_signing_bytes, verify_signature

if TYPE_CHECKING:
    from .client import WavvonClient


def _pin_key(pubkey: str) -> str:
    return "dh-pin/" + pubkey


async def _fetch_record(client: WavvonClient, pubkey: str) -> str | None:
    """None when the hub has no key for `pubkey`. A record `pubkey` did not
    sign is DhKeyUnsignedError, never "no key"."""
    try:
        rec = await client.json_call("GET", f"/identity/{quote(pubkey, safe='')}/dh-key")
    except HubError as e:
        if e.status == 404:
            return None
        raise
    dh = rec.get("dh_pubkey_hex") if isinstance(rec, dict) else None
    if not dh:
        return None
    try:
        sig = bytes.fromhex(rec.get("signature_hex") or "")
    except ValueError:
        sig = b""
    if not verify_signature(pubkey, dh_key_record_signing_bytes(pubkey, dh), sig):
        raise DhKeyUnsignedError(pubkey)
    return str(dh)


async def publish_dh_key(client: WavvonClient) -> bool:
    own = client.identity.public_key
    dh = client.dh_public_key_hex()
    try:
        if await _fetch_record(client, own) == dh:
            return False
    except DhKeyUnsignedError:
        pass
    sig = client.identity.sign(dh_key_record_signing_bytes(own, dh)).hex()
    await client.json_call(
        "PUT", f"/identity/{quote(own, safe='')}/dh-key", json={"dh_pubkey_hex": dh, "signature_hex": sig}
    )
    return True


async def peer_dh_key(client: WavvonClient, pubkey: str) -> bytes:
    dh = await _fetch_record(client, pubkey)
    if dh is None:
        raise RecipientHasNoKeyError(pubkey)
    try:
        raw = bytes.fromhex(dh)
    except ValueError:
        raw = b""
    if len(raw) != 32:
        raise HubError(200, f"DH key of {pubkey} is not 32 bytes of hex")
    pinned = client.store.get(_pin_key(pubkey))
    if pinned is None:
        client.store.put(_pin_key(pubkey), dh.encode())
    elif pinned.decode() != dh:
        raise DhKeyChangedError(pubkey, pinned.decode(), dh)
    return raw


async def accept_dh_key(client: WavvonClient, pubkey: str) -> None:
    dh = await _fetch_record(client, pubkey)
    if dh is None:
        raise RecipientHasNoKeyError(pubkey)
    client.store.put(_pin_key(pubkey), dh.encode())
