"""The DM and DH-key vectors of Wavvon-server's wire-vectors.json: signing
bytes, signatures and the encryption itself (sdk-dm.md section 6)."""

from __future__ import annotations

from typing import Any

from test_conformance import file, vector  # noqa: F401

from wavvon import _crypto as c
from wavvon import wire
from wavvon.auth import identity_from_seed
from wavvon.dm import _Session


def sign_check(v: dict[str, Any], signing: bytes, key: str = "signature") -> None:
    assert signing.hex() == v["signing_bytes"]
    assert identity_from_seed(v["inputs"]["signer_seed"]).sign(signing).hex() == v[key]


def dh(seed: str) -> bytes:
    return c.dh_secret_from_seed(bytes.fromhex(seed))


def test_master_dh_pubkey(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "master_dh_pubkey")
    assert c.x25519_pub(dh(v["inputs"]["seed"])).hex() == v["dh_pubkey"]


def test_dh_key_record(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dh_key_record")
    i = v["inputs"]
    sign_check(v, wire.dh_key_record_signing_bytes(i["pubkey"], i["dh_pubkey"]))


def test_dm_envelope(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dm_envelope")
    i = v["inputs"]
    sign_check(
        v, wire.dm_envelope_signing_bytes(i["conversation_id"], i["ciphertext"], i["nonce"], i["sender_dh_pubkey"])
    )


def test_dr_envelope(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dr_envelope")
    i = v["inputs"]
    sign_check(
        v,
        wire.dr_envelope_signing_bytes(
            i["conversation_id"], i["message_index"], i["prev_count"], i["ciphertext"], i["dh_pubkey"]
        ),
    )


def test_group_dm_envelope(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "group_dm_envelope")
    i = v["inputs"]
    sign_check(
        v,
        wire.group_dm_envelope_signing_bytes(
            i["conversation_id"], i["sender_key_version"], i["iteration"], i["ciphertext"], i["nonce"]
        ),
    )


def test_sender_key_dist(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "sender_key_dist")
    i = v["inputs"]
    recipients = [(r[0], r[1]) for r in i["recipients"]]
    sign_check(v, wire.sender_key_dist_signing_bytes(i["conversation_id"], i["version"], recipients))


def test_dm_member_change(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dm_member_change")
    i = v["inputs"]
    sign_check(
        v,
        wire.dm_member_change_signing_bytes(i["conversation_id"], i["actor"], i["added"], i["removed"], i["timestamp"]),
    )


def test_federated_plaintext_dm_v2(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "federated_plaintext_dm_v2")
    i = v["inputs"]
    sign_check(
        v,
        wire.federated_plaintext_dm_v2_signing_bytes(
            i["conversation_id"], i["kind"], i["content"], i["message_id"], i["created_at"], i["members"]
        ),
    )


def test_federated_plaintext_dm_v1(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "federated_plaintext_dm")
    i = v["inputs"]
    sign_check(v, wire.federated_plaintext_dm_signing_bytes(i["conversation_id"], i["kind"], i["content"]))


def test_subkey_cert(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "subkey_cert")
    i = v["inputs"]
    signing = wire.subkey_cert_signing_bytes(
        i["master_pubkey"], i["subkey_pubkey"], i["device_label"], i["issued_at"], i["not_after"], i["fallback_hubs"]
    )
    sign_check(v, signing)
    cert = {**{k: i[k] for k in i if k != "signer_seed"}, "signature": v["signature"]}
    assert wire.verify_subkey_cert(cert)
    assert not wire.verify_subkey_cert({**cert, "device_label": "phone"})


def test_dm_key_v1(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dm_key_v1")
    i = v["inputs"]
    a, b = dh(i["alice_seed"]), dh(i["bob_seed"])
    key = c.dm_key_v1(a, c.x25519_pub(b), i["conversation_id"])
    assert key.hex() == v["key"]
    assert c.dm_key_v1(b, c.x25519_pub(a), i["conversation_id"]) == key
    ct = c.aead_seal(key, bytes.fromhex(i["nonce"]), i["plaintext"].encode())
    assert ct.hex() == v["ciphertext"]


def test_dr_session(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "dr_session")
    i = v["inputs"]
    conv = i["conversation_id"]
    a, b = dh(i["alice_seed"]), dh(i["bob_seed"])
    a_pub, b_pub = c.x25519_pub(a), c.x25519_pub(b)
    a_eph, b_eph = bytes.fromhex(i["alice_eph_secret"]), bytes.fromhex(i["bob_eph_secret"])

    assert c.dr_root_key(a, b_pub, conv).hex() == v["rk0"]
    init = c.dr_initiator_init(a, b_pub, conv, a_eph)
    assert init.eph_pub.hex() == v["alice_eph_pub"]
    assert (init.rk.hex(), init.cks.hex()) == (v["alice_rk"], v["alice_cks"])
    mk, nxt = c.dr_kdf_ck(init.cks)
    assert (mk.hex(), nxt.hex()) == (v["message_key"], v["next_cks"])
    assert c.dr_nonce(mk).hex() == v["nonce"]
    ct = c.dr_message_seal(mk, i["plaintext"].encode())
    assert ct.hex() == v["ciphertext"]

    resp = c.dr_responder_init(b, a_pub, conv, init.eph_pub, b_eph)
    assert resp.ckr is not None
    assert (resp.rk.hex(), resp.ckr.hex(), resp.cks.hex()) == (v["bob_rk"], v["bob_ckr"], v["bob_cks"])
    assert resp.eph_pub.hex() == v["bob_eph_pub"]
    reply_key, _ = c.dr_kdf_ck(resp.cks)
    assert reply_key.hex() == v["reply_message_key"]
    reply = c.dr_message_seal(reply_key, i["reply_plaintext"].encode())
    assert reply.hex() == v["reply_ciphertext"]

    step_rk, step_ckr = c.dr_kdf_rk(init.rk, c.x25519(a_eph, resp.eph_pub))
    assert (step_rk.hex(), step_ckr.hex()) == (v["reply_step_rk"], v["reply_step_ckr"])

    # The same exchange through the session state machine, both sides.
    bob = _Session.responder(b, a_pub, conv, v["alice_eph_pub"], b_eph)
    alice = _Session.initiator(a, b_pub, conv, a_eph)
    assert bob.open(v["alice_eph_pub"], 0, 0, ct) == i["plaintext"].encode()
    assert alice.open(v["bob_eph_pub"], 0, 0, reply) == i["reply_plaintext"].encode()


def test_group_ratchet(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "group_ratchet")
    i = v["inputs"]
    chain = bytes.fromhex(i["chain_key"])
    assert c.group_msg_key(chain, i["iteration"]).hex() == v["message_key"]
    assert c.group_next_chain_key(chain, i["iteration"]).hex() == v["next_chain_key"]
    assert c.group_nonce(i["iteration"]).hex() == v["nonce"]
    ct, nonce, _ = c.group_message_seal(chain, i["iteration"], i["plaintext"].encode())
    assert (nonce.hex(), ct.hex()) == (v["nonce"], v["ciphertext"])
    assert c.group_message_open(chain, i["iteration"], i["iteration"], nonce, ct) == i["plaintext"].encode()
    # From an earlier held iteration the chain is walked forward to the message.
    early = bytes.fromhex(i["chain_key"])
    ct0, nonce0, _ = c.group_message_seal(early, 0, b"x")
    assert c.group_message_open(early, 0, 0, nonce0, ct0) == b"x"
    ahead = c.group_next_chain_key(early, 0)
    ct1, nonce1, _ = c.group_message_seal(ahead, 1, b"y")
    assert c.group_message_open(early, 0, 1, nonce1, ct1) == b"y"


def test_group_key_wrap(file: dict[str, Any]) -> None:  # noqa: F811
    v = vector(file, "group_key_wrap")
    i = v["inputs"]
    s, r = dh(i["sender_seed"]), dh(i["recipient_seed"])
    nonce, chain = bytes.fromhex(i["nonce"]), bytes.fromhex(i["chain_key"])
    wrapped = c.group_key_wrap(s, c.x25519_pub(r), i["conversation_id"], chain, i["iteration"], nonce)
    assert wrapped.hex() == v["ciphertext"]
    assert c.group_key_unwrap(r, c.x25519_pub(s), i["conversation_id"], nonce, wrapped) == (chain, i["iteration"])
