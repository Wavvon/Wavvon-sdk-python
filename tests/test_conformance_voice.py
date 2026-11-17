"""The voice vectors of Wavvon-server's wire-vectors.json (sdk-voice.md section 2)."""

from __future__ import annotations

from typing import Any

import pytest
from test_conformance import file, vector  # noqa: F401

from wavvon import _crypto as c


def dh(seed: str) -> bytes:
    return c.dh_secret_from_seed(bytes.fromhex(seed))


def test_voice_key_wrap(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "voice_key_wrap")
    i = v["inputs"]
    s, r = dh(i["sender_seed"]), dh(i["recipient_seed"])
    key, salt = bytes.fromhex(i["sender_key"]), bytes.fromhex(i["nonce_salt"])
    nonce = bytes.fromhex(i["wrap_nonce"])
    wrapped = c.voice_key_wrap(s, c.x25519_pub(r), i["channel_id"], key, salt, i["key_id"], nonce)
    assert wrapped.hex() == v["ciphertext"]
    assert c.voice_key_unwrap(r, c.x25519_pub(s), i["channel_id"], wrapped, nonce) == (key, salt, i["key_id"])


@pytest.mark.parametrize("name", ["voice_packet_ctr0", "voice_packet_ctr7"])
def test_voice_packet(file: dict[str, Any], name: str) -> None:  # noqa: F811
    v = vector(file, name)
    i = v["inputs"]
    key, salt, opus = bytes.fromhex(i["sender_key"]), bytes.fromhex(i["nonce_salt"]), bytes.fromhex(i["opus"])
    packet = c.voice_packet_seal(key, salt, i["key_id"], i["counter"], i["timestamp"], opus)
    assert packet.hex() == v["packet"]
    assert c.voice_packet_open(key, salt, packet) == (i["key_id"], i["counter"], i["timestamp"], opus)


def test_voice_packet_header_is_authenticated(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "voice_packet_ctr0")
    i = v["inputs"]
    packet = bytearray.fromhex(v["packet"])
    packet[15] ^= 1  # ts is in the AAD
    with pytest.raises(c.DecryptionError):
        c.voice_packet_open(bytes.fromhex(i["sender_key"]), bytes.fromhex(i["nonce_salt"]), bytes(packet))
