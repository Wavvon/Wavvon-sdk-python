"""Asserts the tier-1 vectors from Wavvon-server's wire-vectors.json, the one
authority for every signed byte sequence (sdk.md §4). The file is read, never
copied in: point WAVVON_WIRE_VECTORS at a pinned copy, or keep the default
sibling checkout."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import sys
from pathlib import Path
from typing import Any

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from wavvon import (
    auth_challenge_signing_bytes,
    identity_from_seed,
    outgoing_webhook_signing_key,
    verify_dispatch,
    verify_outgoing_webhook,
    webhook_delivery_signing_bytes,
)

PATH = Path(os.environ.get("WAVVON_WIRE_VECTORS", "../../server/crates/identity/wire-vectors.json")).resolve()


def resolve_refs(v: Any, fixtures: dict[str, str]) -> Any:
    """ "@name" anywhere in the file means fixtures[name]."""
    if isinstance(v, str) and v.startswith("@"):
        return fixtures[v[1:]]
    if isinstance(v, list):
        return [resolve_refs(x, fixtures) for x in v]
    if isinstance(v, dict):
        return {k: resolve_refs(x, fixtures) for k, x in v.items()}
    return v


@pytest.fixture(scope="module")
def file() -> dict[str, Any]:
    if not PATH.exists():
        if os.environ.get("CI"):
            pytest.fail(f"wire vectors missing at {PATH}")
        bar = "!" * 72
        print(
            f"\n{bar}\n!! CONFORMANCE VECTORS NOT FOUND at {PATH}\n"
            f"!! The tier-1 wire vectors were NOT checked. Set WAVVON_WIRE_VECTORS.\n{bar}",
            file=sys.stderr,
        )
        pytest.skip(f"CONFORMANCE VECTORS NOT FOUND at {PATH}")
    data: dict[str, Any] = json.loads(PATH.read_text("utf-8"))
    return data


def vector(file: dict[str, Any], name: str) -> dict[str, Any]:
    v: dict[str, Any] = resolve_refs(file["vectors"][name], file["fixtures"])
    return v


def test_format_1(file: dict[str, Any]) -> None:
    assert file["format"] == 1


def test_auth_challenge(file: dict[str, Any]) -> None:
    v = vector(file, "auth_challenge")
    signing = auth_challenge_signing_bytes(bytes.fromhex(v["inputs"]["challenge"]), "tagged-v1")
    assert signing.hex() == v["signing_bytes"]
    assert identity_from_seed(v["inputs"]["signer_seed"]).sign(signing).hex() == v["signature"]


def test_webhook_delivery_hub(file: dict[str, Any]) -> None:
    v = vector(file, "webhook_delivery_hub")
    i = v["inputs"]
    body = i["body"].encode()
    signing = webhook_delivery_signing_bytes(i["timestamp"], body)
    assert signing.hex() == v["signing_bytes"]
    assert identity_from_seed(i["hub_seed"]).public_key == v["hub_pubkey"]
    key = Ed25519PrivateKey.from_private_bytes(bytes.fromhex(i["hub_seed"]))
    assert key.sign(signing).hex() == v["signature_v1"]
    assert key.sign(body).hex() == v["signature_legacy"]

    h = v["headers"]
    headers = {
        h["hub_pubkey"]: v["hub_pubkey"],
        h["signature_v1"]: v["signature_v1"],
        h["signature_legacy"]: v["signature_legacy"],
        h["timestamp"]: str(i["timestamp"]),
    }
    assert verify_dispatch(headers, body, v["hub_pubkey"], now=i["timestamp"])["type"] == "slash_command"


def test_webhook_delivery_outgoing(file: dict[str, Any]) -> None:
    v = vector(file, "webhook_delivery_outgoing")
    i = v["inputs"]
    assert i["hkdf_salt"] == "wavvon-webhook-signing"
    assert i["hkdf_info"] == ""
    key = outgoing_webhook_signing_key(i["secret_as_shown"])
    assert key.hex() == v["signing_key"]
    assert outgoing_webhook_signing_key(bytes.fromhex(i["raw_secret"])).hex() == v["signing_key"]

    body = i["body"].encode()
    signing = webhook_delivery_signing_bytes(i["timestamp"], body)
    assert signing.hex() == v["signing_bytes"]
    assert hmac.new(key, signing, hashlib.sha256).hexdigest() == v["signature_v1"]
    assert hmac.new(key, body, hashlib.sha256).hexdigest() == v["signature_legacy"]

    h = v["headers"]
    headers = {
        h["signature_v1"]: v["signature_v1"],
        h["signature_legacy"]: v["signature_legacy"],
        h["timestamp"]: str(i["timestamp"]),
        h["webhook_id"]: "wh_test",
    }
    assert verify_outgoing_webhook(headers, body, i["secret_as_shown"], now=i["timestamp"])["type"] == "hub_event"
