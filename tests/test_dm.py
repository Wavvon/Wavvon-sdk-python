from __future__ import annotations

import os

import pytest

from wavvon import DmError, DmErrorReason, MemoryStore
from wavvon import _crypto as c
from wavvon.dm import MAX_SKIP, _Session, verify_envelope
from wavvon.wire import dr_envelope_signing_bytes


def pair() -> tuple[_Session, _Session]:
    a, b = os.urandom(32), os.urandom(32)
    a_pub, b_pub = c.x25519_pub(a), c.x25519_pub(b)
    alice = _Session.initiator(a, b_pub, "conv", os.urandom(32))
    # Bob learns Alice's ratchet key from her first message.
    bob = _Session.responder(b, a_pub, "conv", alice.dhs_pub, os.urandom(32))
    return alice, bob


def test_out_of_order_uses_the_skip_cache() -> None:
    alice, bob = pair()
    first_pub = alice.dhs_pub
    sealed = [(alice.seal(f"m{i}".encode()), first_pub) for i in range(3)]
    for i in (2, 0, 1):
        (ct, index, prev), pub = sealed[i]
        assert bob.open(pub, index, prev, ct) == f"m{i}".encode()


def test_reply_steps_the_ratchet_both_ways() -> None:
    alice, bob = pair()
    ct, i, p = alice.seal(b"ping")
    assert bob.open(alice.dhs_pub, i, p, ct) == b"ping"
    pub = bob.dhs_pub
    ct, i, p = bob.seal(b"pong")
    assert alice.open(pub, i, p, ct) == b"pong"
    ct, i, p = alice.seal(b"again")
    assert bob.open(alice.dhs_pub, i, p, ct) == b"again"


def test_too_many_skipped() -> None:
    alice, bob = pair()
    pub = alice.dhs_pub
    for _ in range(MAX_SKIP + 2):
        alice.seal(b"x")
    ct, i, p = alice.seal(b"late")
    with pytest.raises(DmError) as e:
        bob.open(pub, i, p, ct)
    assert e.value.reason is DmErrorReason.TOO_MANY_SKIPPED


def test_tampered_ciphertext_fails_closed() -> None:
    alice, bob = pair()
    ct, i, p = alice.seal(b"hi")
    with pytest.raises(DmError) as e:
        bob.open(alice.dhs_pub, i, p, ct[:-1] + bytes([ct[-1] ^ 1]))
    assert e.value.reason is DmErrorReason.DECRYPTION_FAILED


def test_envelope_must_be_signed_by_its_sender() -> None:
    from wavvon import identity_from_seed

    me, other = identity_from_seed(os.urandom(32)), identity_from_seed(os.urandom(32))
    sig = me.sign(dr_envelope_signing_bytes("conv", 0, 0, "aa", "bb")).hex()
    env = {
        "sender_pubkey": me.public_key,
        "v": 2,
        "message_index": 0,
        "prev_count": 0,
        "ciphertext_hex": "aa",
        "dh_pubkey_hex": "bb",
        "signature_hex": sig,
    }
    verify_envelope("conv", env, me.public_key)
    for bad_env, sender in ((env, other.public_key), ({**env, "ciphertext_hex": "ab"}, me.public_key)):
        with pytest.raises(DmError) as e:
            verify_envelope("conv", bad_env, sender)
        assert e.value.reason is DmErrorReason.NOT_SIGNED_BY_SENDER


def test_memory_store_roundtrip() -> None:
    s = MemoryStore()
    assert s.get("k") is None
    s.put("k", b"v")
    assert s.get("k") == b"v"
    s.delete("k")
    assert s.get("k") is None
