"""Key derivations and AEADs behind E2E DMs and voice, byte for byte as in
Wavvon-server crates/identity/src/{dm,voice}.rs, pinned by the dm_key_v1,
dr_session, group_ratchet, group_key_wrap, voice_key_wrap and voice_packet_*
vectors. Secrets and public keys are raw 32-byte X25519 values; every
ciphertext is AES-256-GCM with the tag appended. The functions are pure:
nonces and ephemeral scalars are arguments."""

from __future__ import annotations

import hashlib
import struct
from dataclasses import dataclass

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


class DecryptionError(Exception):
    """An AEAD did not open."""


def x25519(secret: bytes, pub: bytes) -> bytes:
    return X25519PrivateKey.from_private_bytes(secret).exchange(X25519PublicKey.from_public_bytes(pub))


def x25519_pub(secret: bytes) -> bytes:
    return X25519PrivateKey.from_private_bytes(secret).public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)


def dh_secret_from_seed(seed: bytes) -> bytes:
    """SHA-512(seed)[0..32], clamped (vector master_dh_pubkey)."""
    s = bytearray(hashlib.sha512(seed).digest()[:32])
    s[0] &= 248
    s[31] &= 127
    s[31] |= 64
    return bytes(s)


def hkdf(ikm: bytes, salt: bytes | None, info: str, length: int = 32) -> bytes:
    return HKDF(algorithm=hashes.SHA256(), length=length, salt=salt, info=info.encode()).derive(ikm)


def aead_seal(key: bytes, nonce: bytes, plaintext: bytes, aad: bytes | None = None) -> bytes:
    return AESGCM(key).encrypt(nonce, plaintext, aad)


def aead_open(key: bytes, nonce: bytes, ciphertext: bytes, aad: bytes | None = None) -> bytes:
    if len(nonce) != 12:
        raise DecryptionError("nonce must be 12 bytes")
    try:
        return AESGCM(key).decrypt(nonce, ciphertext, aad)
    except InvalidTag as e:
        raise DecryptionError("decryption failed") from e


def be32(v: int) -> bytes:
    return struct.pack(">I", v)


# ---- 1:1 v1 (static key; receive only) ----


def dm_key_v1(my_secret: bytes, peer_pub: bytes, conv_id: str) -> bytes:
    return hkdf(x25519(my_secret, peer_pub), conv_id.encode(), "wavvon/dm-key/v1")


# ---- 1:1 v2 double ratchet ----


def dr_root_key(my_static: bytes, their_static: bytes, conv_id: str) -> bytes:
    return hkdf(x25519(my_static, their_static), conv_id.encode(), "wavvon/dr-init/v2")


def dr_kdf_rk(rk: bytes, dh_out: bytes) -> tuple[bytes, bytes]:
    out = hkdf(dh_out, rk, "wavvon/dr-rk/v2", 64)
    return out[:32], out[32:]


def dr_kdf_ck(ck: bytes) -> tuple[bytes, bytes]:
    out = hkdf(ck, None, "wavvon/dr-ck-step/v2", 64)
    return out[:32], out[32:]


def dr_nonce(msg_key: bytes) -> bytes:
    return hkdf(msg_key, None, "wavvon/dr-nonce/v2", 12)


def dr_message_seal(msg_key: bytes, plaintext: bytes) -> bytes:
    return aead_seal(msg_key, dr_nonce(msg_key), plaintext)


def dr_message_open(msg_key: bytes, ciphertext: bytes) -> bytes:
    return aead_open(msg_key, dr_nonce(msg_key), ciphertext)


@dataclass
class DrInit:
    rk: bytes
    cks: bytes
    ckr: bytes | None
    eph_pub: bytes


def dr_initiator_init(my_static: bytes, their_static: bytes, conv_id: str, eph: bytes) -> DrInit:
    rk0 = dr_root_key(my_static, their_static, conv_id)
    rk, cks = dr_kdf_rk(rk0, x25519(eph, their_static))
    return DrInit(rk, cks, None, x25519_pub(eph))


def dr_responder_init(my_static: bytes, their_static: bytes, conv_id: str, incoming_dhr: bytes, eph: bytes) -> DrInit:
    rk0 = dr_root_key(my_static, their_static, conv_id)
    rk1, ckr = dr_kdf_rk(rk0, x25519(my_static, incoming_dhr))
    rk, cks = dr_kdf_rk(rk1, x25519(eph, incoming_dhr))
    return DrInit(rk, cks, ckr, x25519_pub(eph))


# ---- group sender-key ratchet ----


def group_msg_key(chain: bytes, iteration: int) -> bytes:
    return hkdf(chain, be32(iteration), "wavvon/group-msg/v1")


def group_next_chain_key(chain: bytes, iteration: int) -> bytes:
    return hkdf(chain, be32(iteration), "wavvon/group-chain/v1")


def group_nonce(iteration: int) -> bytes:
    return b"\0" * 8 + be32(iteration)


def group_message_seal(chain: bytes, iteration: int, plaintext: bytes) -> tuple[bytes, bytes, bytes]:
    """Returns the ciphertext, the nonce and the chain key for iteration + 1;
    the caller stores that before reusing the chain."""
    nonce = group_nonce(iteration)
    return aead_seal(group_msg_key(chain, iteration), nonce, plaintext), nonce, group_next_chain_key(chain, iteration)


def group_message_open(chain: bytes, held: int, iteration: int, nonce: bytes, ciphertext: bytes) -> bytes:
    """`chain` is the chain key at iteration `held`; an earlier message cannot be read."""
    if iteration < held:
        raise DecryptionError("the chain was already advanced past this message")
    ck = chain
    for i in range(held, iteration):
        ck = group_next_chain_key(ck, i)
    return aead_open(group_msg_key(ck, iteration), nonce, ciphertext)


def _group_wrap_key(my_secret: bytes, peer_pub: bytes, conv_id: str) -> bytes:
    return hkdf(x25519(my_secret, peer_pub), conv_id.encode(), "wavvon/group-key-dist/v1")


def group_key_wrap(
    my_secret: bytes, recipient_pub: bytes, conv_id: str, chain: bytes, iteration: int, nonce: bytes
) -> bytes:
    return aead_seal(_group_wrap_key(my_secret, recipient_pub, conv_id), nonce, chain + be32(iteration))


def group_key_unwrap(
    my_secret: bytes, sender_pub: bytes, conv_id: str, nonce: bytes, wrapped: bytes
) -> tuple[bytes, int]:
    plain = aead_open(_group_wrap_key(my_secret, sender_pub, conv_id), nonce, wrapped)
    if len(plain) < 36:
        raise DecryptionError("bad wrapped chain key")
    return plain[:32], int(struct.unpack(">I", plain[32:36])[0])
