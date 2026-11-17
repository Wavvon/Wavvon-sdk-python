"""Signing bytes of the DM and DH-key envelopes (wire-format.md), each pinned by
a vector in Wavvon-server's wire-vectors.json."""

from __future__ import annotations

import struct
from collections.abc import Iterable, Mapping
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


def _u32(v: int) -> bytes:
    return struct.pack("<I", v)


def _u64(v: int) -> bytes:
    return struct.pack("<Q", v)


def _str(s: str) -> bytes:
    raw = s.encode("utf-8")
    return _u32(len(raw)) + raw


def _strs(v: Iterable[str]) -> bytes:
    items = list(v)
    return _u32(len(items)) + b"".join(_str(s) for s in items)


def dh_key_record_signing_bytes(pubkey: str, dh_pubkey_hex: str) -> bytes:
    """What a public key signs to publish its X25519 key."""
    return b"wavvon/dh-key/v1\0" + _str(pubkey) + _str(dh_pubkey_hex)


def dm_envelope_signing_bytes(conv_id: str, ciphertext_hex: str, nonce_hex: str, dh_pubkey_hex: str) -> bytes:
    """Signing input of a v1 1:1 envelope (dm-ciphertext/v1)."""
    return b"wavvon/dm-ciphertext/v1\0" + _str(conv_id) + _str(ciphertext_hex) + _str(nonce_hex) + _str(dh_pubkey_hex)


def dr_envelope_signing_bytes(
    conv_id: str, message_index: int, prev_count: int, ciphertext_hex: str, dh_pubkey_hex: str
) -> bytes:
    """Signing input of a double-ratchet envelope (dm-ciphertext/v2)."""
    return (
        b"wavvon/dm-ciphertext/v2\0"
        + _str(conv_id)
        + _u32(message_index)
        + _u32(prev_count)
        + _str(ciphertext_hex)
        + _str(dh_pubkey_hex)
    )


def group_dm_envelope_signing_bytes(
    conv_id: str, sender_key_version: int, iteration: int, ciphertext_hex: str, nonce_hex: str
) -> bytes:
    """Signing input of a group envelope. The integers are length-prefixed
    decimal strings, not raw integers."""
    return (
        b"wavvon/group-dm-ciphertext/v1\0"
        + _str(conv_id)
        + _str(str(sender_key_version))
        + _str(str(iteration))
        + _str(ciphertext_hex)
        + _str(nonce_hex)
    )


def sender_key_dist_signing_bytes(conv_id: str, version: int, recipients: Iterable[tuple[str, str]]) -> bytes:
    """Signing input of a sender-key distribution. `recipients` are
    `(public_key, wrapped_key_hex)` pairs; they are sorted here, so the order
    given does not matter."""
    out = b"wavvon/group-key-dist/v1\0" + _str(conv_id) + _str(str(version))
    for pub, wrapped in sorted(recipients, key=lambda r: r[0]):
        out += _str(pub) + _str(wrapped)
    return out


def dm_member_change_signing_bytes(
    conv_id: str, actor: str, added: Iterable[str], removed: Iterable[str], issued_at: int
) -> bytes:
    """What a group member signs to add members or to leave."""
    return (
        b"wavvon/dm-member-change/v1\0" + _str(conv_id) + _str(actor) + _strs(added) + _strs(removed) + _u64(issued_at)
    )


def federated_plaintext_dm_signing_bytes(conv_id: str, conv_type: str, content: str) -> bytes:
    """The v1 signing input of a plaintext DM."""
    return b"wavvon/federated-dm/v1\0" + _str(conv_id) + _str(conv_type) + _str(content)


def federated_plaintext_dm_v2_signing_bytes(
    conv_id: str, conv_type: str, content: str, message_id: str, created_at: int, members: Iterable[str]
) -> bytes:
    """The v2 signing input of a plaintext DM: it also covers the message id,
    the timestamp and the member set (sorted, de-duplicated)."""
    return (
        b"wavvon/federated-dm/v2\0"
        + _str(conv_id)
        + _str(conv_type)
        + _str(content)
        + _str(message_id)
        + _u64(created_at)
        + _strs(sorted(set(members)))
    )


def subkey_cert_signing_bytes(
    master: str,
    subkey: str,
    label: str,
    issued_at: int,
    not_after: int | None,
    fallback_hubs: Iterable[str],
) -> bytes:
    out = b"wavvon/subkey-cert/v1\0" + _str(master) + _str(subkey) + _str(label) + _u64(issued_at)
    out += b"\x00" if not_after is None else b"\x01" + _u64(not_after)
    return out + _strs(fallback_hubs)


def verify_signature(pubkey_hex: str, message: bytes, signature: bytes) -> bool:
    """Ed25519 verification by a hex public key; False for any malformed input."""
    try:
        pub = bytes.fromhex(pubkey_hex)
        if len(pub) != 32:
            return False
        Ed25519PublicKey.from_public_bytes(pub).verify(signature, message)
    except (ValueError, InvalidSignature):
        return False
    return True


def verify_subkey_cert(cert: Mapping[str, Any]) -> bool:
    """Whether the master key signed this SubkeyCert (the hub's JSON shape)."""
    try:
        msg = subkey_cert_signing_bytes(
            cert["master_pubkey"],
            cert["subkey_pubkey"],
            cert["device_label"],
            cert["issued_at"],
            cert.get("not_after"),
            cert.get("fallback_hubs") or [],
        )
        return verify_signature(cert["master_pubkey"], msg, bytes.fromhex(cert["signature"]))
    except (KeyError, TypeError, ValueError, struct.error):
        return False
