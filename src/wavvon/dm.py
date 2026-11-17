"""End-to-end encrypted DMs for a program (sdk-dm.md): 1:1 double ratchet (v2
send, v2 and v1 receive) and group sender keys. Nothing here ever falls back
to plaintext: that is the separate, explicit `send_plaintext`."""

from __future__ import annotations

import asyncio
import json
import os
import time
import uuid
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

from . import _crypto as c
from .errors import (
    DhKeyChangedError,
    DhKeyUnsignedError,
    DmError,
    DmErrorReason,
    RecipientHasNoKeyError,
)
from .wire import (
    dm_envelope_signing_bytes,
    dm_member_change_signing_bytes,
    dr_envelope_signing_bytes,
    federated_plaintext_dm_signing_bytes,
    federated_plaintext_dm_v2_signing_bytes,
    group_dm_envelope_signing_bytes,
    sender_key_dist_signing_bytes,
    verify_signature,
    verify_subkey_cert,
)

if TYPE_CHECKING:
    from .client import WavvonClient

MAX_SKIP = 1000
_PLAIN_CACHE = 2048
_SEEN_CAP = 4096

_PER_MESSAGE = (DmError, RecipientHasNoKeyError, DhKeyChangedError, DhKeyUnsignedError)

Envelope = dict[str, Any]


@dataclass
class DmPlaintext:
    """What a DM carries inside its ciphertext."""

    content: str = ""
    attachments: list[Any] = field(default_factory=list)
    """Descriptors as the clients write them. Omitted from the wire when empty."""

    def to_json(self) -> bytes:
        body: dict[str, Any] = {"content": self.content}
        if self.attachments:
            body["attachments"] = self.attachments
        return json.dumps(body, separators=(",", ":")).encode()


@dataclass
class Conversation:
    id: str
    conv_type: str
    """"dm" for 1:1, "group" otherwise."""
    members: list[str]

    @staticmethod
    def from_json(v: dict[str, Any]) -> Conversation:
        return Conversation(id=v["id"], conv_type=v.get("conv_type", ""), members=list(v.get("members") or []))


@dataclass
class DmMessage:
    """One message of a conversation as read. `error` is per message: a program
    keeps going past one it cannot read. A row the hub stored in the clear has
    `encrypted` False; what to do about that is the program's call."""

    id: str
    conversation_id: str
    sender: str
    sender_name: str | None
    created_at: int
    encrypted: bool
    content: DmPlaintext = field(default_factory=DmPlaintext)
    """Valid when `error` is None."""
    error: Exception | None = None
    """Why it could not be read: a DmError, or a missing or changed key of the sender."""


@dataclass
class SkippedMember:
    public_key: str
    error: Exception
    """RecipientHasNoKeyError, DhKeyChangedError or DhKeyUnsignedError."""


@dataclass
class Distribution:
    """Who got a group sender key and who was skipped (no DH key, a changed
    key). A skipped member cannot read messages under that key."""

    version: int
    delivered: list[str] = field(default_factory=list)
    skipped: list[SkippedMember] = field(default_factory=list)


@dataclass
class Sent:
    """A message the hub accepted."""

    id: str
    created_at: int
    distribution: Distribution | None = None
    """Set when this send created the group sender key first."""


def _err(reason: DmErrorReason, detail: str = "") -> DmError:
    return DmError(reason, detail)


def _h32(s: Any) -> bytes:
    try:
        b = bytes.fromhex(s)
    except (ValueError, TypeError):
        b = b""
    if len(b) != 32:
        raise _err(DmErrorReason.MALFORMED, "expected 32 bytes of hex")
    return b


def _crypto_err(e: Exception) -> DmError:
    return _err(DmErrorReason.MALFORMED, str(e))


def _random32() -> bytes:
    return os.urandom(32)


class _Session:
    """A double-ratchet session, persisted as JSON in the desktop client's shape."""

    def __init__(self, d: dict[str, Any]) -> None:
        self.rk: str = d["rk"]
        self.cks: str | None = d.get("cks")
        self.ckr: str | None = d.get("ckr")
        self.ns: int = d.get("ns", 0)
        self.nr: int = d.get("nr", 0)
        self.pn: int = d.get("pn", 0)
        self.dhs_priv: str = d["dhs_priv"]
        self.dhs_pub: str = d["dhs_pub"]
        self.dhr: str | None = d.get("dhr")
        self.mkskipped: dict[str, str] = dict(d.get("mkskipped") or {})

    @staticmethod
    def initiator(my_static: bytes, their_static: bytes, conv: str, eph: bytes) -> _Session:
        try:
            i = c.dr_initiator_init(my_static, their_static, conv, eph)
        except ValueError as e:
            raise _crypto_err(e) from e
        return _Session({"rk": i.rk.hex(), "cks": i.cks.hex(), "dhs_priv": eph.hex(), "dhs_pub": i.eph_pub.hex()})

    @staticmethod
    def responder(my_static: bytes, their_static: bytes, conv: str, incoming_dhr: str, eph: bytes) -> _Session:
        inc = _h32(incoming_dhr)
        try:
            i = c.dr_responder_init(my_static, their_static, conv, inc, eph)
        except ValueError as e:
            raise _crypto_err(e) from e
        assert i.ckr is not None
        return _Session(
            {
                "rk": i.rk.hex(),
                "cks": i.cks.hex(),
                "ckr": i.ckr.hex(),
                "dhs_priv": eph.hex(),
                "dhs_pub": i.eph_pub.hex(),
                "dhr": incoming_dhr,
            }
        )

    def seal(self, plaintext: bytes) -> tuple[bytes, int, int]:
        """Seals, advancing the sending chain; returns ciphertext, message_index, prev_count."""
        if self.cks is None:
            raise _err(DmErrorReason.NO_SESSION)
        mk, nxt = c.dr_kdf_ck(_h32(self.cks))
        ct = c.dr_message_seal(mk, plaintext)
        index, prev = self.ns, self.pn
        self.cks = nxt.hex()
        self.ns += 1
        return ct, index, prev

    def open(self, dh_pub: str, index: int, prev: int, ct: bytes) -> bytes:
        """The receive algorithm of e2e-encryption.md "1:1 DM Encryption - v2":
        skipped-key cache, DH-ratchet step on a new remote key, chain advance.
        The caller works on a fresh copy and keeps it only on success."""

        def opened(mk: bytes) -> bytes:
            try:
                return c.dr_message_open(mk, ct)
            except c.DecryptionError as e:
                raise _err(DmErrorReason.DECRYPTION_FAILED) from e

        slot = f"{dh_pub}:{index}"
        if slot in self.mkskipped:
            return opened(_h32(self.mkskipped.pop(slot)))
        if self.dhr != dh_pub:
            if self.ckr is not None:
                self._skip(self.dhr or "", _h32(self.ckr), self.nr, prev)
            their = _h32(dh_pub)
            try:
                rk, ckr = c.dr_kdf_rk(_h32(self.rk), c.x25519(_h32(self.dhs_priv), their))
                new_priv = _random32()
                rk, cks = c.dr_kdf_rk(rk, c.x25519(new_priv, their))
                pub = c.x25519_pub(new_priv)
            except ValueError as e:
                raise _crypto_err(e) from e
            self.rk, self.cks = rk.hex(), cks.hex()
            self.pn, self.ns, self.nr = self.ns, 0, 0
            self.dhr, self.ckr = dh_pub, ckr.hex()
            self.dhs_priv, self.dhs_pub = new_priv.hex(), pub.hex()
        if self.ckr is None:
            raise _err(DmErrorReason.NO_SESSION)
        ckr = self._skip(dh_pub, _h32(self.ckr), self.nr, index)
        mk, nxt = c.dr_kdf_ck(ckr)
        plain = opened(mk)
        self.ckr = nxt.hex()
        self.nr = index + 1
        return plain

    def _skip(self, dh: str, ck: bytes, frm: int, to: int) -> bytes:
        """Caches the message keys of chain `dh` from `frm` up to (not including)
        `to`; returns the chain key at `to`."""
        if len(self.mkskipped) + max(to - frm, 0) > MAX_SKIP:
            raise _err(DmErrorReason.TOO_MANY_SKIPPED)
        for n in range(frm, to):
            mk, ck = c.dr_kdf_ck(ck)
            self.mkskipped[f"{dh}:{n}"] = mk.hex()
        return ck


def _u32(env: Envelope, k: str) -> int | None:
    v = env.get(k)
    if isinstance(v, bool) or not isinstance(v, int) or not 0 <= v < 2**32:
        return None
    return v


def _must_u32(env: Envelope, k: str) -> int:
    v = _u32(env, k)
    if v is None:
        raise _err(DmErrorReason.MALFORMED, f"{k} missing")
    return v


def _hex_field(env: Envelope, k: str) -> bytes:
    try:
        return bytes.fromhex(str(env.get(k) or ""))
    except ValueError as e:
        raise _err(DmErrorReason.MALFORMED, f"{k} is not hex") from e


def verify_envelope(conv: str, env: Envelope, sender: str) -> None:
    """Checks that `sender` (the member the hub names) signed the envelope:
    directly, or through a device whose SubkeyCert `sender` issued. The hub
    checked too; a program does not rely on that."""
    bad = _err(DmErrorReason.NOT_SIGNED_BY_SENDER)
    if env.get("sender_pubkey") != sender:
        raise bad

    def text(k: str) -> str:
        return str(env.get(k) or "")

    if "sender_key_version" in env:
        version, iteration = _u32(env, "sender_key_version"), _u32(env, "iteration")
        if version is None or iteration is None:
            raise bad
        signed = group_dm_envelope_signing_bytes(conv, version, iteration, text("ciphertext_hex"), text("nonce_hex"))
    elif env.get("v") == 2:
        index, prev = _u32(env, "message_index"), _u32(env, "prev_count")
        if index is None or prev is None:
            raise bad
        signed = dr_envelope_signing_bytes(conv, index, prev, text("ciphertext_hex"), text("dh_pubkey_hex"))
    else:
        signed = dm_envelope_signing_bytes(conv, text("ciphertext_hex"), text("nonce_hex"), text("dh_pubkey_hex"))
    try:
        sig = bytes.fromhex(text("signature_hex"))
    except ValueError:
        raise bad from None
    signer = sender
    cert = env.get("signer_cert")
    if cert is not None:
        if not isinstance(cert, dict) or cert.get("master_pubkey") != sender or not verify_subkey_cert(cert):
            raise bad
        signer = str(cert["subkey_pubkey"])
    if not verify_signature(signer, signed, sig):
        raise bad


def _parse_plaintext(raw: bytes) -> DmPlaintext:
    try:
        v = json.loads(raw)
        return DmPlaintext(content=str(v.get("content", "")), attachments=list(v.get("attachments") or []))
    except (ValueError, AttributeError, TypeError) as e:
        raise _err(DmErrorReason.MALFORMED, f"plaintext JSON: {e}") from e


class Dms:
    """A program's DMs. Obtain it with `WavvonClient.dms()`."""

    def __init__(self, client: WavvonClient) -> None:
        self._c = client
        self._lock = asyncio.Lock()  # one ratchet is never advanced by two tasks at once
        self._plain: OrderedDict[str, DmPlaintext] = OrderedDict()
        self._seen: OrderedDict[str, None] = OrderedDict()

    def _me(self) -> str:
        return self._c.identity.public_key

    def _get(self, key: str) -> dict[str, Any] | None:
        raw = self._c.store.get(key)
        if raw is None:
            return None
        try:
            v = json.loads(raw)
        except ValueError as e:
            raise ValueError(f"wavvon: state {key} is not valid: {e}") from e
        return v  # type: ignore[no-any-return]

    def _put(self, key: str, v: Any) -> None:
        self._c.store.put(key, json.dumps(v if isinstance(v, dict) else v.__dict__).encode())

    # ---- conversations and sending ----

    async def conversation(self, conv: str) -> Conversation:
        return Conversation.from_json(await self._c.json_call("GET", f"/conversations/{quote(conv, safe='')}"))

    async def conversations(self) -> list[Conversation]:
        """Every conversation, paged to exhaustion where the hub pages (capability list.cursor.lists)."""
        paged = await self._c.has_capability("list.cursor.lists")
        out: list[Conversation] = []
        while True:
            params: dict[str, Any] = {}
            if paged:
                params["limit"] = 500
                if out:
                    params["cursor"] = out[-1].id
            page = await self._c.json_call("GET", "/conversations", params=params)
            out += [Conversation.from_json(v) for v in page]
            if not paged or len(page) < 500:
                return out

    async def create_conversation(self, members: list[str]) -> Conversation:
        """Creates a conversation with `members` (the others; the hub adds the
        caller). A 1:1 with a member you already talk to is returned, not duplicated."""
        return Conversation.from_json(await self._c.json_call("POST", "/conversations", json={"members": members}))

    async def send_text(self, conv: str, text: str) -> Sent:
        return await self.send(conv, DmPlaintext(content=text))

    async def send(self, conv: str, message: DmPlaintext) -> Sent:
        """Encrypts and sends: the double ratchet in a 1:1, the sender-key chain
        in a group. Raises RecipientHasNoKeyError or DhKeyChangedError rather
        than ever sending in the clear."""
        async with self._lock:
            cv = await self.conversation(conv)
            dist: Distribution | None = None
            if cv.conv_type == "dm":
                body = await self._seal_dr(cv, message.to_json())
            else:
                body, dist = await self._seal_group(cv, message.to_json())
            sent = await self._post(conv, body)
            sent.distribution = dist
            return sent

    async def send_plaintext(self, conv: str, content: str) -> Sent:
        """The explicit, signed plaintext DM. Whether to ever call it is the
        program's decision; `send` never does."""
        cv = await self.conversation(conv)
        v2 = await self._c.has_capability("dms.plaintext.v2")
        message_id = str(uuid.uuid4())
        created_at = int(time.time())
        if v2:
            signing = federated_plaintext_dm_v2_signing_bytes(
                conv, cv.conv_type, content, message_id, created_at, cv.members
            )
        else:
            signing = federated_plaintext_dm_signing_bytes(conv, cv.conv_type, content)
        body: dict[str, Any] = {
            "content": content,
            "attachments": [],
            "plaintext_signature": self._c.identity.sign(signing).hex(),
        }
        if v2:
            body["message_id"] = message_id
            body["created_at"] = created_at
        return await self._post(conv, body)

    async def _post(self, conv: str, body: Any) -> Sent:
        v = await self._c.json_call("POST", f"/conversations/{quote(conv, safe='')}/messages", json=body)
        return Sent(id=v["id"], created_at=v.get("created_at", 0))

    async def _seal_dr(self, cv: Conversation, plaintext: bytes) -> dict[str, Any]:
        me = self._me()
        peer = next((m for m in cv.members if m != me), None)
        if peer is None:
            raise _err(DmErrorReason.MALFORMED, "conversation has no other member")
        key = f"dr/{cv.id}"
        stored = self._get(key)
        if stored is None:
            their = await self._c.peer_dh_key(peer)
            session = _Session.initiator(self._c._dh_secret(), their, cv.id, _random32())
        else:
            session = _Session(stored)
        dh_pub = session.dhs_pub
        ct, index, prev = session.seal(plaintext)
        # Persisted before the POST: a key is never used twice, and a failed
        # send leaves a gap the receiver skips over.
        self._put(key, session)
        ct_hex = ct.hex()
        sig = self._c.identity.sign(dr_envelope_signing_bytes(cv.id, index, prev, ct_hex, dh_pub)).hex()
        return {
            "encrypted_envelope": {
                "sender_pubkey": me,
                "conv_id": cv.id,
                "ciphertext_hex": ct_hex,
                "nonce_hex": "",
                "dh_pubkey_hex": dh_pub,
                "signature_hex": sig,
                "v": 2,
                "message_index": index,
                "prev_count": prev,
            }
        }

    async def _seal_group(self, cv: Conversation, plaintext: bytes) -> tuple[dict[str, Any], Distribution | None]:
        own = self._get(f"group-own/{cv.id}")
        dist: Distribution | None = None
        if own is None:
            own, dist = await self._new_chain(cv, 1)
        iteration, version = own["iteration"], own["version"]
        ct, nonce, nxt = c.group_message_seal(_h32(own["chain_key"]), iteration, plaintext)
        own["chain_key"] = nxt.hex()
        own["iteration"] = iteration + 1
        self._put(f"group-own/{cv.id}", own)
        ct_hex, nonce_hex = ct.hex(), nonce.hex()
        sig = self._c.identity.sign(group_dm_envelope_signing_bytes(cv.id, version, iteration, ct_hex, nonce_hex)).hex()
        return {
            "group_encrypted_envelope": {
                "sender_pubkey": self._me(),
                "conv_id": cv.id,
                "sender_key_version": version,
                "iteration": iteration,
                "ciphertext_hex": ct_hex,
                "nonce_hex": nonce_hex,
                "signature_hex": sig,
            }
        }, dist

    async def _new_chain(self, cv: Conversation, version: int) -> tuple[dict[str, Any], Distribution]:
        """A fresh chain at `version`, distributed to every other member and
        stored once the hub accepted the distribution."""
        own = {"version": version, "chain_key": _random32().hex(), "iteration": 0}
        dist = await self._distribute(cv, own)
        self._put(f"group-own/{cv.id}", own)
        return own, dist

    async def _distribute(self, cv: Conversation, own: dict[str, Any]) -> Distribution:
        me, my_dh = self._me(), self._c._dh_secret()
        chain = _h32(own["chain_key"])
        dist = Distribution(version=own["version"])
        blobs: list[dict[str, Any]] = []
        pairs: list[tuple[str, str]] = []
        for member in cv.members:
            if member == me:
                continue
            try:
                their = await self._c.peer_dh_key(member)
            except _PER_MESSAGE as e:
                dist.skipped.append(SkippedMember(member, e))
                continue
            nonce = os.urandom(12)
            try:
                wrapped = c.group_key_wrap(my_dh, their, cv.id, chain, own["iteration"], nonce).hex()
            except ValueError as e:
                raise _crypto_err(e) from e
            blobs.append(
                {
                    "recipient_pubkey": member,
                    "wrapped_key_hex": wrapped,
                    "wrap_nonce_hex": nonce.hex(),
                    "iteration": own["iteration"],
                }
            )
            pairs.append((member, wrapped))
            dist.delivered.append(member)
        sig = self._c.identity.sign(sender_key_dist_signing_bytes(cv.id, own["version"], pairs)).hex()
        await self._c.json_call(
            "PUT",
            f"/conversations/{quote(cv.id, safe='')}/sender-keys",
            json={"sender_key_version": own["version"], "recipients": blobs, "signature_hex": sig},
        )
        return dist

    async def rotate_group_key(self, conv: str) -> Distribution:
        """Makes a new sender key (version + 1) and re-distributes it to the
        members now in the conversation, so someone who left cannot read what
        follows. Earlier messages stay readable: peers keep a chain per version."""
        async with self._lock:
            cv = await self.conversation(conv)
            old = self._get(f"group-own/{conv}")
            _, dist = await self._new_chain(cv, old["version"] + 1 if old else 1)
            return dist

    async def handle_event(self, event: dict[str, Any]) -> Distribution | None:
        """Rotates the sender key on a `dm_member_changed` event when this
        program holds one for that conversation; None for every other event.
        Call it with the events you read, or call `rotate_group_key` yourself."""
        if event.get("type") != "dm_member_changed":
            return None
        conv = event.get("conversation_id")
        if not isinstance(conv, str) or self._get(f"group-own/{conv}") is None:
            return None
        return await self.rotate_group_key(conv)

    async def _signed_change(self, conv: str, added: list[str], removed: list[str]) -> dict[str, Any] | None:
        """The signed membership change the hub's dms.group.signedmembers wants; None on a hub without it."""
        if not await self._c.has_capability("dms.group.signedmembers"):
            return None
        issued_at = int(time.time())
        sig = self._c.identity.sign(dm_member_change_signing_bytes(conv, self._me(), added, removed, issued_at))
        return {"issued_at": issued_at, "signature": sig.hex()}

    async def add_members(self, conv: str, members: list[str]) -> None:
        """Adds members (one request each, as the hub takes them), then rotates
        the sender key if this program holds one."""
        for m in members:
            body: dict[str, Any] = {"public_key": m}
            signed = await self._signed_change(conv, [m], [])
            if signed is not None:
                body["signed"] = signed
            await self._c.json_call("POST", f"/conversations/{quote(conv, safe='')}/members", json=body)
        if self._get(f"group-own/{conv}") is not None:
            await self.rotate_group_key(conv)

    async def leave(self, conv: str) -> None:
        """Leaves a group. The hub lets a member remove only themselves."""
        me = self._me()
        signed = await self._signed_change(conv, [], [me])
        await self._c.json_call(
            "DELETE", f"/conversations/{quote(conv, safe='')}/members/{quote(me, safe='')}", json=signed
        )

    # ---- receiving ----

    async def messages(self, conv: str, *, limit: int | None = None, cursor: str | None = None) -> list[DmMessage]:
        """A page of a conversation, each message decrypted. Transient hub
        failures raise; a message that cannot be read is that message's `error`."""
        params: dict[str, Any] = {}
        if limit:
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        return [await self._read_row(conv, row) for row in await self._rows(conv, params)]

    async def poll(self, conv: str) -> list[DmMessage]:
        """The messages this handle has not returned yet. The first call for a
        conversation returns its newest page, so a program that only wants what
        arrives from now on calls `skip_existing` first. The hub's `dm` event
        says a message arrived; `poll` fetches it."""
        out: list[DmMessage] = []
        for row in await self._rows(conv, {"limit": 100}):
            if row["id"] in self._seen:
                continue
            out.append(await self._read_row(conv, row))
            self._mark_seen(row["id"])
        return out

    async def skip_existing(self, conv: str) -> None:
        """Marks what is in the conversation now as delivered, without decrypting it."""
        for row in await self._rows(conv, {"limit": 100}):
            self._mark_seen(row["id"])

    async def _rows(self, conv: str, params: dict[str, Any]) -> list[dict[str, Any]]:
        rows = await self._c.json_call("GET", f"/conversations/{quote(conv, safe='')}/messages", params=params)
        return list(rows or [])

    def _mark_seen(self, mid: str) -> None:
        self._seen[mid] = None
        while len(self._seen) > _SEEN_CAP:
            self._seen.popitem(last=False)

    async def _read_row(self, conv: str, row: dict[str, Any]) -> DmMessage:
        m = DmMessage(
            id=row["id"],
            conversation_id=row.get("conversation_id", conv),
            sender=row["sender"],
            sender_name=row.get("sender_name"),
            created_at=row.get("created_at", 0),
            encrypted=row.get("encrypted_envelope") is not None or row.get("group_encrypted_envelope") is not None,
        )
        try:
            m.content = await self._open_row(conv, row)
        except _PER_MESSAGE as e:
            m.error = e
        return m

    async def _open_row(self, conv: str, row: dict[str, Any]) -> DmPlaintext:
        hit = self._plain.get(row["id"])
        if hit is not None:
            return hit
        async with self._lock:
            env: Envelope | None = row.get("encrypted_envelope")
            group: Envelope | None = row.get("group_encrypted_envelope")
            e = env if env is not None else group
            if e is not None:
                verify_envelope(conv, e, row["sender"])
                if row["sender"] == self._me():
                    raise _err(DmErrorReason.OWN_MESSAGE)
                if group is not None:
                    raw = await self._open_group(conv, e, row["sender"])
                elif e.get("v") == 2:
                    raw = await self._open_dr(conv, e, row["sender"])
                else:
                    raw = self._open_v1(conv, e)
                plain = _parse_plaintext(raw)
            else:
                plain = DmPlaintext(content=row.get("content") or "", attachments=list(row.get("attachments") or []))
            self._plain[row["id"]] = plain
            while len(self._plain) > _PLAIN_CACHE:
                self._plain.popitem(last=False)
            return plain

    def _open_v1(self, conv: str, env: Envelope) -> bytes:
        their = _h32(env.get("dh_pubkey_hex"))
        try:
            key = c.dm_key_v1(self._c._dh_secret(), their, conv)
            return c.aead_open(key, _hex_field(env, "nonce_hex"), _hex_field(env, "ciphertext_hex"))
        except c.DecryptionError as e:
            raise _err(DmErrorReason.DECRYPTION_FAILED) from e
        except ValueError as e:
            raise _crypto_err(e) from e

    async def _open_dr(self, conv: str, env: Envelope, sender: str) -> bytes:
        key = f"dr/{conv}"
        dh_pub = str(env.get("dh_pubkey_hex") or "")
        stored = self._get(key)
        if stored is None:
            # First inbound message of a conversation this side never sent in:
            # responder-init from the sender's published key.
            their = await self._c.peer_dh_key(sender)
            session = _Session.responder(self._c._dh_secret(), their, conv, dh_pub, _random32())
        else:
            session = _Session(stored)
        index = _must_u32(env, "message_index")
        prev = _u32(env, "prev_count") or 0
        plain = session.open(dh_pub, index, prev, _hex_field(env, "ciphertext_hex"))
        self._put(key, session)
        return plain

    async def _open_group(self, conv: str, env: Envelope, sender: str) -> bytes:
        version, iteration = _must_u32(env, "sender_key_version"), _must_u32(env, "iteration")
        key = f"group-peer/{conv}/{sender}/{version}"
        chain = self._get(key)
        if chain is None:
            await self._refresh_sender_keys(conv)
            chain = self._get(key)
        if chain is None:
            raise _err(DmErrorReason.KEY_NOT_FOUND, f"{sender} at version {version}")
        if chain["iteration"] > iteration:
            raise _err(DmErrorReason.CHAIN_ADVANCED)
        try:
            return c.group_message_open(
                _h32(chain["chain_key"]),
                chain["iteration"],
                iteration,
                _hex_field(env, "nonce_hex"),
                _hex_field(env, "ciphertext_hex"),
            )
        except c.DecryptionError as e:
            raise _err(DmErrorReason.DECRYPTION_FAILED) from e

    async def _refresh_sender_keys(self, conv: str) -> None:
        """Unwraps the sender keys the hub holds for this program and stores the
        ones not held yet. A sender whose DH key is missing or changed is skipped:
        its messages then report KEY_NOT_FOUND."""
        entries = await self._c.json_call("GET", f"/conversations/{quote(conv, safe='')}/sender-keys")
        my_dh = self._c._dh_secret()
        for e in entries or []:
            try:
                wrapped, nonce = bytes.fromhex(e["wrapped_key_hex"]), bytes.fromhex(e["wrap_nonce_hex"])
                sender, version = e["sender_pubkey"], e["sender_key_version"]
            except (KeyError, ValueError, TypeError):
                continue
            key = f"group-peer/{conv}/{sender}/{version}"
            if not sender or self._c.store.get(key) is not None:
                continue
            try:
                their = await self._c.peer_dh_key(sender)
            except _PER_MESSAGE:
                continue
            try:
                chain, iteration = c.group_key_unwrap(my_dh, their, conv, nonce, wrapped)
            except (c.DecryptionError, ValueError):
                continue
            self._put(key, {"chain_key": chain.hex(), "iteration": iteration})
