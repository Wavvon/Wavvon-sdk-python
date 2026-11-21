"""A program in a voice channel (sdk-voice.md). It does exactly what the
desktop and web clients do: voice signalling rides one chat WebSocket, the
audio rides a WebRTC data channel, and every packet is sealed with a
per-sender key wrapped to each listener's DH key.

The module owns the mechanisms (key distribution and rotation, 20 ms pacing,
the replay watermark, the proximity rate limit). It decides nothing for the
program: mute, deafen, AFK moves and what to do with a changed DH key are
events and calls. Only a real interop constraint refuses input: an Opus packet
that is not exactly 20 ms.

Opus passthrough (`send_opus`, `Audio.opus`) needs no native library. PCM
(`send_pcm`, `Audio.pcm`) needs `pip install wavvon-sdk[opus]` and libopus."""

from __future__ import annotations

import asyncio
import os
from array import array
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from .. import _crypto as c
from ..errors import (
    DhKeyChangedError,
    DhKeyUnsignedError,
    RecipientHasNoKeyError,
    WavvonError,
)
from ._opus import FRAME_SAMPLES, OpusCodec, check_20ms
from ._rtc import RtcSession, TransportError

if TYPE_CHECKING:
    from ..client import WavvonClient
    from ..events import EventStream

FRAME_SECONDS = 0.020
# A program this far behind is re-anchored instead of bursting to catch up.
MAX_LAG_FRAMES = 3
# More than one position every 50 ms risks the hub's silent 30 ms rate drop.
POSITION_EVERY = 0.050
SPEAKING_IDLE = 0.200
STEP_TIMEOUT = 15.0
# Datagrams must fit one QUIC packet; the clients keep to about this.
MAX_PACKET = 1000

_PER_PEER = (RecipientHasNoKeyError, DhKeyChangedError, DhKeyUnsignedError)


# ---- events ----


@dataclass
class Participant:
    public_key: str
    sender_id: int
    display_name: str | None = None


@dataclass
class Zone:
    zone_id: str
    name: str
    coordinate_system: str
    """"2d" or "3d"."""
    attenuation: Any = None
    positions: dict[str, list[float]] = field(default_factory=dict)


@dataclass
class Audio:
    """One decrypted 20 ms packet from one speaker. Jitter buffering is the
    program's: frames arrive as they come, with `ts` and `ctr` to order by."""

    from_pubkey: str
    sender_id: int
    key_id: int
    ts: int
    """The 48 kHz sample clock, +960 per frame."""
    ctr: int
    whisper: bool
    opus: bytes
    pcm: array[float] | None = None
    """Decoded 48 kHz mono audio; None unless the opus extra is installed and requested."""


@dataclass
class Roster:
    """Who is in the room, after any change."""

    participants: list[Participant]


@dataclass
class Speaking:
    public_key: str
    speaking: bool


@dataclass
class Zones:
    """The room's zones, after any change."""

    zones: list[Zone]


@dataclass
class Position:
    zone_id: str
    public_key: str
    position: list[float]


@dataclass
class PositionRefused:
    """The hub refused a position update this program sent (an unknown zone, or a
    creator-only zone it did not create). The program decides what to do."""

    reason: str


@dataclass
class TalkGranted:
    """A moderator gave this program the floor; `may_speak` is now True."""


@dataclass
class MoveRequested:
    """A moderator, or the AFK sweep (`auto`), asks the program to move. The hub
    moves no one: the program decides."""

    target_channel_id: str
    target_channel_name: str
    source_channel_id: str
    event_id: str
    auto: bool


@dataclass
class Rejoining:
    """The socket dropped, which ended the room on the hub; the SDK is joining
    again with a fresh key."""


@dataclass
class KeySkipped:
    """A participant could not be given this program's key (no DH key published,
    or a changed one), so it cannot hear the program. Also reports a peer whose
    key could not be unwrapped for the same reason."""

    public_key: str
    reason: str
    error: Exception


@dataclass
class Unknown:
    """A voice_* message this SDK does not model."""

    raw: dict[str, Any]


@dataclass
class Failure:
    """Something went wrong inside the room that the program should know about;
    the room keeps running unless the error says otherwise."""

    error: Exception


VoiceEvent = (
    Audio
    | Roster
    | Speaking
    | Zones
    | Position
    | PositionRefused
    | TalkGranted
    | MoveRequested
    | Rejoining
    | KeySkipped
    | Unknown
    | Failure
)


# ---- errors ----


class VoiceError(WavvonError):
    """Base of the errors a voice room raises on purpose."""


class MayNotSpeakError(VoiceError):
    """Talk power is below the channel's threshold, so the relay would drop every
    datagram. Lifted by a TalkGranted event."""

    def __init__(self) -> None:
        super().__init__("may_speak is false in this channel")


class NotInRoomError(VoiceError):
    """After leave, or between a dropped socket and the rejoin."""

    def __init__(self) -> None:
        super().__init__("not in a voice room right now")


class BadFrameError(VoiceError):
    """Anything but exactly 20 ms of Opus (or 960 PCM samples)."""

    def __init__(self, detail: str) -> None:
        super().__init__(f"not a single 20 ms frame: {detail}")


class PacketTooLargeError(VoiceError):
    def __init__(self, size: int) -> None:
        super().__init__(f"a {size}-byte packet does not fit a datagram")
        self.size = size


class RefusedError(VoiceError):
    """A refusal from the hub (a failed voice_join, or an error frame for another voice message)."""

    def __init__(self, message: str) -> None:
        super().__init__(f"the hub refused: {message}")
        self.message = message


class UnknownZoneError(VoiceError):
    def __init__(self, zone_id: str) -> None:
        super().__init__(f"zone {zone_id} is not in this room")
        self.zone_id = zone_id


class BadPositionError(VoiceError):
    def __init__(self, got: int, want: int) -> None:
        super().__init__(f"position has {got} coordinates, the zone takes {want}")


# ---- parsing helpers ----


def _u16(m: dict[str, Any], k: str) -> int | None:
    v = m.get(k)
    if isinstance(v, bool) or not isinstance(v, int) or not 0 <= v <= 0xFFFF:
        return None
    return v


def _participant(raw: Any) -> Participant | None:
    if not isinstance(raw, dict):
        return None
    pub, sid = raw.get("public_key"), _u16(raw, "sender_id")
    if not isinstance(pub, str) or not pub or sid is None:
        return None
    name = raw.get("display_name")
    return Participant(pub, sid, name if isinstance(name, str) else None)


def _participants(raw: Any) -> list[Participant]:
    return [p for p in (_participant(x) for x in raw or []) if p is not None]


def _floats(raw: Any) -> list[float]:
    return [float(x) for x in raw or [] if isinstance(x, (int, float)) and not isinstance(x, bool)]


def _zone(raw: Any) -> Zone | None:
    if not isinstance(raw, dict) or not raw.get("zone_id"):
        return None
    positions = raw.get("positions")
    return Zone(
        zone_id=str(raw["zone_id"]),
        name=str(raw.get("name") or ""),
        coordinate_system=str(raw.get("coordinate_system") or ""),
        attenuation=raw.get("attenuation"),
        positions={k: _floats(p) for k, p in positions.items()} if isinstance(positions, dict) else {},
    )


@dataclass
class _OwnKey:
    key: bytes
    salt: bytes
    key_id: int
    ctr: int = 0


@dataclass
class _Pacing:
    next: float
    ts: int = 0


_END = object()


class Voice:
    """A joined voice room. Build it with `Voice.join` or `client.join_voice`.
    One task can `send_opus` while another reads events."""

    def __init__(self, client: WavvonClient, stream: EventStream, codec: OpusCodec | None, channel_id: str) -> None:
        self._client = client
        self._stream = stream
        self._codec = codec
        self._loop = asyncio.get_running_loop()
        self._inbox: asyncio.Queue[Any] = asyncio.Queue()
        self._events: asyncio.Queue[Any] = asyncio.Queue()
        self._tasks: set[asyncio.Task[Any]] = set()
        self._channel_id = channel_id
        self._sender_id = 0
        self._in_room = False
        self._may_speak = True
        self._muted = False
        self._deafened = False
        self._roster: dict[int, Participant] = {}
        self._own = _OwnKey(b"", b"", 0)
        self._remote: dict[tuple[str, int], tuple[bytes, bytes]] = {}
        self._marks: dict[tuple[int, int], int] = {}
        self._zones: list[Zone] = []
        self._sess: RtcSession | None = None
        self._pace: _Pacing | None = None
        self._speaking = False
        self._last_send = self._loop.time()
        self._position: tuple[str, list[float]] | None = None
        self._last_position = self._loop.time() - POSITION_EVERY
        self._dh: dict[str, bytes] = {}

    @classmethod
    async def join(
        cls,
        client: WavvonClient,
        channel_id: str,
        *,
        pcm: bool = False,
        music: bool = False,
        bitrate: int | None = None,
    ) -> Voice:
        """Publishes the DH key, joins the channel's voice room and opens the audio
        session. One room per client: the hub allows one per identity. `pcm` turns on
        PCM encode and decode (the opus extra); `music` and `bitrate` tune its encoder."""
        await client.require_capability("channels.voice")
        # Voice transport v3: a hub without it speaks only WebTransport, which
        # this SDK no longer carries.
        await client.require_capability("voice.webrtc")
        # Without a published key nobody wraps a voice key to this program and it
        # cannot unwrap theirs: it would be deaf and mute.
        await client.publish_dh_key()
        codec = OpusCodec(music=music, bitrate=bitrate) if pcm else None
        # A socket of its own: the hub ties the room to the connection, so this
        # one carries voice and nothing else the program reads.
        stream = client.connect()
        v = cls(client, stream, codec, channel_id)
        stream.on("*", v._inbox.put_nowait)
        try:
            async with asyncio.timeout(STEP_TIMEOUT):
                while (await v._inbox.get())["type"] != "hello":
                    pass
            await v._establish(channel_id)
        except BaseException:
            await stream.close()
            raise
        v._spawn(v._run())
        v._spawn(v._housekeeping())
        return v

    async def __aenter__(self) -> Voice:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.leave()

    def _spawn(self, coro: Any) -> None:
        task = self._loop.create_task(coro)
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

    def _emit(self, ev: VoiceEvent) -> None:
        self._events.put_nowait(ev)

    def _fail(self, err: Exception) -> None:
        self._emit(Failure(err))

    # ---- joining ----

    async def _establish(self, channel_id: str) -> None:
        """voice_join on an open socket: joined, audio connected, key offered. Used
        for the first join and again after every dropped socket."""
        async with asyncio.timeout(STEP_TIMEOUT):
            await self._stream.send({"type": "voice_join", "channel_id": channel_id})
            joined: dict[str, Any] | None = None
            while joined is None:
                ev = await self._inbox.get()
                if ev["type"] == "unknown" and ev.get("raw_type") == "voice_joined":
                    joined = ev["raw"]
                elif ev["type"] == "error" and ev.get("context") == "voice_join":
                    raise RefusedError(str(ev.get("message")))
            sess, deferred = await self._connect_transport(str(joined.get("voice_token")))
        sender_id = _u16(joined, "sender_id")
        if sender_id is None:
            await sess.close()
            raise VoiceError("sender_id out of range")
        parts = _participants(joined.get("participants"))
        me = self._client.identity.public_key
        others = [p.public_key for p in parts if p.public_key != me]
        # The key id never goes back: a rejoin must not reuse a (sender, key_id)
        # pair whose replay watermark listeners still hold.
        self._own = _OwnKey(os.urandom(32), os.urandom(4), self._own.key_id + 1)
        if joined.get("channel_id"):
            self._channel_id = str(joined["channel_id"])
        self._sender_id = sender_id
        # A hub without voice.talk omits the field; absence is not "muted".
        may = joined.get("may_speak")
        self._may_speak = may if isinstance(may, bool) else True
        self._roster = {p.sender_id: p for p in parts}
        self._remote = {}
        self._marks = {}
        self._pace = None
        self._speaking = False
        self._sess = sess
        self._in_room = True
        self._spawn(self._read_datagrams(sess))
        self._offer(others)
        # What arrived while the answer was awaited, a key bundle above all:
        # dropping it would leave this room unable to open that speaker.
        for ev in deferred:
            self._handle(ev)

    async def _connect_transport(self, token: str) -> tuple[RtcSession, list[dict[str, Any]]]:
        """Offers a WebRTC session bound by the voice token and waits for the hub's
        answer on the same socket, keeping every other event that arrives meanwhile."""
        sess, sdp = await RtcSession.offer()
        deferred: list[dict[str, Any]] = []
        try:
            await self._stream.send({"type": "voice_rtc_offer", "token": token, "sdp": sdp})
            answer: str | None = None
            while answer is None:
                ev = await self._inbox.get()
                if ev["type"] == "unknown" and ev.get("raw_type") == "voice_rtc_answer":
                    answer = str(ev["raw"].get("sdp") or "")
                elif ev["type"] == "error" and ev.get("context") == "voice_rtc_offer":
                    raise RefusedError(str(ev.get("message")))
                else:
                    deferred.append(ev)
            await sess.accept(answer)
        except BaseException:
            await sess.close()
            raise
        return sess, deferred

    async def _dh_for(self, pub: str) -> bytes:
        """A peer's DH key, looked up once per session: it is pinned, so a second
        answer would be the same or a refusal."""
        k = self._dh.get(pub)
        if k is None:
            k = self._dh[pub] = await self._client.peer_dh_key(pub)
        return k

    def _offer(self, to: list[str]) -> None:
        """Wraps the current sender key to each of `to` and sends one
        voice_key_offer. A peer without a usable DH key is skipped and
        reported, as every client does."""
        if to:
            self._spawn(self._do_offer(list(to), self._channel_id, self._own))

    async def _do_offer(self, to: list[str], channel: str, own: _OwnKey) -> None:
        bundles: list[dict[str, str]] = []
        my_dh = self._client._dh_secret()
        for pub in to:
            try:
                dh = await self._dh_for(pub)
            except _PER_PEER as e:
                self._emit(KeySkipped(pub, str(e), e))
                continue
            except Exception as e:
                self._fail(e)
                return
            nonce = os.urandom(12)
            try:
                ct = c.voice_key_wrap(my_dh, dh, channel, own.key, own.salt, own.key_id, nonce)
            except ValueError as e:
                self._fail(e)
                continue
            bundles.append({"recipient_pubkey": pub, "ciphertext_hex": ct.hex(), "nonce_hex": nonce.hex()})
        if not bundles:
            return
        try:
            await self._stream.send({"type": "voice_key_offer", "channel_id": channel, "bundles": bundles})
        except Exception as e:
            self._fail(e)

    def _unwrap(self, m: dict[str, Any]) -> None:
        frm, channel = str(m.get("from_pubkey") or ""), self._channel_id
        try:
            ct, nonce = bytes.fromhex(str(m.get("ciphertext_hex"))), bytes.fromhex(str(m.get("nonce_hex")))
        except ValueError:
            return
        if len(nonce) != 12:
            return
        self._spawn(self._do_unwrap(frm, channel, ct, nonce))

    async def _do_unwrap(self, frm: str, channel: str, ct: bytes, nonce: bytes) -> None:
        try:
            dh = await self._dh_for(frm)
        except _PER_PEER as e:
            self._emit(KeySkipped(frm, str(e), e))
            return
        except Exception as e:
            self._fail(e)
            return
        try:
            key, salt, key_id = c.voice_key_unwrap(self._client._dh_secret(), dh, channel, ct, nonce)
        except (c.DecryptionError, ValueError):
            return  # a bundle that does not open is dropped: there is no key to use
        # A new key for this pair restarts its counter.
        for p in self._roster.values():
            if p.public_key == frm:
                self._marks.pop((p.sender_id, key_id), None)
        self._remote[(frm, key_id)] = (key, salt)

    # ---- the room's socket ----

    async def _run(self) -> None:
        try:
            while True:
                ev = await self._inbox.get()
                if ev["type"] == "hello":
                    await self._rejoin()
                else:
                    self._handle(ev)
        finally:
            self._emit_end()

    def _emit_end(self) -> None:
        self._events.put_nowait(_END)

    async def _rejoin(self) -> None:
        """A second hello: the socket dropped and came back, so the hub already ran
        leave_voice and the old session is dead. Join again."""
        self._in_room = False
        sess, self._sess = self._sess, None
        if sess is not None:
            await sess.close()
        self._emit(Rejoining())
        try:
            await self._establish(self._channel_id)
        except Exception as e:
            self._fail(e)

    def _handle(self, ev: dict[str, Any]) -> None:
        t = ev["type"]
        if t == "error":
            ctx = str(ev.get("context") or "")
            if ctx == "voice_position_update":
                self._emit(PositionRefused(str(ev.get("message"))))
            elif ctx.startswith("voice"):
                self._fail(RefusedError(f"{ctx}: {ev.get('message')}"))
        elif t == "unknown" and str(ev.get("raw_type") or "").startswith("voice_"):
            m = ev.get("raw")
            if isinstance(m, dict):
                # Messages about another room are not this session's.
                if m.get("channel_id") in (None, "", self._channel_id):
                    self._handle_voice(str(ev["raw_type"]), m)

    def _roster_list(self) -> list[Participant]:
        return sorted(self._roster.values(), key=lambda p: p.sender_id)

    def _rotate_key(self) -> None:
        self._own = _OwnKey(os.urandom(32), os.urandom(4), self._own.key_id + 1)

    def _handle_voice(self, t: str, m: dict[str, Any]) -> None:
        me = self._client.identity.public_key
        if t == "voice_participant_joined":
            p = _participant(m.get("participant"))
            if p is not None:
                self._roster[p.sender_id] = p
                self._emit(Roster(self._roster_list()))
        elif t == "voice_participant_left":
            left = m.get("public_key")
            for sid, p in list(self._roster.items()):
                if p.public_key == left:
                    del self._roster[sid]
                    for mk in [mk for mk in self._marks if mk[0] == sid]:
                        del self._marks[mk]
            for rk in [rk for rk in self._remote if rk[0] == left]:
                del self._remote[rk]
            # Whoever left kept the key: a new one for the rest.
            self._rotate_key()
            self._emit(Roster(self._roster_list()))
            self._offer([p.public_key for p in self._roster.values() if p.public_key != me])
        elif t == "voice_roster_update":
            self._roster = {p.sender_id: p for p in _participants(m.get("participants"))}
            self._emit(Roster(self._roster_list()))
        elif t == "voice_participant_speaking":
            self._emit(Speaking(str(m.get("public_key") or ""), bool(m.get("speaking"))))
        elif t == "voice_key_request":
            newcomer, new_id = str(m.get("new_pubkey") or ""), _u16(m, "new_sender_id")
            if new_id is not None and new_id not in self._roster:
                self._roster[new_id] = Participant(newcomer, new_id)
            if newcomer and newcomer != me:
                self._offer([newcomer])
        elif t == "voice_key_received":
            from_id = _u16(m, "from_sender_id")
            if from_id is not None and from_id not in self._roster:
                self._roster[from_id] = Participant(str(m.get("from_pubkey") or ""), from_id)
            self._unwrap(m)
        elif t == "voice_talk_granted":
            if m.get("public_key") == me:
                self._may_speak = True
                self._emit(TalkGranted())
        elif t == "voice_move":
            self._emit(
                MoveRequested(
                    str(m.get("target_channel_id") or ""),
                    str(m.get("target_channel_name") or ""),
                    str(m.get("source_channel_id") or ""),
                    str(m.get("event_id") or ""),
                    bool(m.get("auto")),
                )
            )
        elif t == "voice_zone_state":
            self._zones = [z for z in (_zone(x) for x in m.get("zones") or []) if z is not None]
            self._emit(Zones(list(self._zones)))
        elif t == "voice_zone_created":
            z = _zone(m)
            if z is not None:
                self._zones = [x for x in self._zones if x.zone_id != z.zone_id] + [z]
                self._emit(Zones(list(self._zones)))
        elif t == "voice_zone_destroyed":
            self._zones = [x for x in self._zones if x.zone_id != m.get("zone_id")]
            self._emit(Zones(list(self._zones)))
        elif t == "voice_position_updated":
            pos, zone_id, who = _floats(m.get("position")), str(m.get("zone_id") or ""), str(m.get("pubkey") or "")
            for z in self._zones:
                if z.zone_id == zone_id:
                    z.positions = {**z.positions, who: pos}
            self._emit(Position(zone_id, who, pos))
        elif t == "voice_joined":
            pass
        else:
            self._emit(Unknown(m))

    # ---- audio in ----

    async def _read_datagrams(self, sess: RtcSession) -> None:
        while True:
            try:
                dg = await sess.receive_datagram()
            except TransportError as e:
                # After leave or during a rejoin the close is ours.
                ours = self._sess is sess and self._in_room
                if self._sess is sess:
                    self._sess = None
                if ours:
                    self._fail(VoiceError(f"transport: {e}"))
                return
            self._handle_datagram(dg)

    def _handle_datagram(self, dg: bytes) -> None:
        """Opens one downlink datagram: sender_id[2] || packet_type[1] || key_id[4] || ctr[8] || ts[4] || AEAD."""
        if len(dg) < 3 + 32 or self._deafened:
            return
        sender_id, whisper, sealed = int.from_bytes(dg[:2], "big"), dg[2] == 1, dg[3:]
        key_id, ctr = int.from_bytes(sealed[:4], "big"), int.from_bytes(sealed[4:12], "big")
        p = self._roster.get(sender_id)
        if p is None:
            return
        rk = self._remote.get((p.public_key, key_id))
        if rk is None:
            return
        mark = self._marks.get((sender_id, key_id))
        if mark is not None and ctr <= mark:
            return
        # The watermark moves only for a packet that opened: a forged one must
        # not be able to lock the real sender out.
        try:
            _, _, ts, opus = c.voice_packet_open(rk[0], rk[1], sealed)
        except c.DecryptionError:
            return
        self._marks[(sender_id, key_id)] = ctr
        frame = Audio(p.public_key, sender_id, key_id, ts, ctr, whisper, opus)
        if self._codec is not None:
            try:
                frame.pcm = self._codec.decode(sender_id, opus)
            except Exception as e:
                self._fail(VoiceError(f"opus codec: {e}"))
        self._emit(frame)

    async def _housekeeping(self) -> None:
        """Every 25 ms: ends a transmission that went quiet, and sends the trailing
        position if one is waiting and the hub's 30 ms limit is safely behind."""
        while True:
            await asyncio.sleep(0.025)
            msgs: list[dict[str, Any]] = []
            now = self._loop.time()
            if self._in_room:
                if self._speaking and now - self._last_send > SPEAKING_IDLE:
                    self._speaking = False
                    msgs.append({"type": "voice_speaking", "channel_id": self._channel_id, "speaking": False})
                if self._position is not None and now - self._last_position >= POSITION_EVERY:
                    zone_id, position = self._position
                    msgs.append({"type": "voice_position_update", "zone_id": zone_id, "position": position})
                    self._position = None
                    self._last_position = now
            for msg in msgs:
                try:
                    await self._stream.send(msg)
                except Exception as e:
                    self._fail(e)

    # ---- the program's side ----

    def __aiter__(self) -> Voice:
        return self

    async def __anext__(self) -> VoiceEvent:
        ev = await self.next()
        if ev is None:
            raise StopAsyncIteration
        return ev

    async def next(self) -> VoiceEvent | None:
        """The next thing that happened in the room, in order; None after `leave`.
        The queue behind it is unbounded: events must be read, or they pile up."""
        ev = await self._events.get()
        if ev is _END:
            self._events.put_nowait(_END)
            return None
        return ev  # type: ignore[no-any-return]

    @property
    def channel_id(self) -> str:
        """The room's channel (it may differ from the one asked for: a spawner room)."""
        return self._channel_id

    @property
    def sender_id(self) -> int:
        """This program's relay id in the room."""
        return self._sender_id

    @property
    def roster(self) -> list[Participant]:
        return self._roster_list()

    @property
    def zones(self) -> list[Zone]:
        return list(self._zones)

    @property
    def may_speak(self) -> bool:
        """False when the relay drops what this program sends; `send_*` then raises
        MayNotSpeakError until a TalkGranted event."""
        return self._may_speak

    def set_muted(self, muted: bool) -> None:
        """Local: the hub has no self-mute. It stops sending (calls to `send_*` still
        wait their slot and return) and ends the speaking indication."""
        self._muted = muted
        if muted and self._speaking:
            self._speaking = False
            self._spawn(self._try_send({"type": "voice_speaking", "channel_id": self._channel_id, "speaking": False}))

    def set_deafened(self, deafened: bool) -> None:
        """Local: it stops delivering Audio. Key distribution keeps running, so
        undeafening is instant."""
        self._deafened = deafened

    async def _try_send(self, msg: dict[str, Any]) -> None:
        try:
            await self._stream.send(msg)
        except Exception:
            pass

    async def send_opus(self, packet: bytes) -> None:
        """Sends one 20 ms Opus packet, held until its slot on a monotonic clock. A
        source that runs faster than real time is slowed to it; one that falls more
        than three frames behind is re-anchored, `ts` jumping by the slots it missed.
        A packet that is not exactly 20 ms is refused: desktop listeners could not
        play it."""
        try:
            check_20ms(packet)
        except ValueError as e:
            raise BadFrameError(str(e)) from e
        if len(packet) > MAX_PACKET:
            raise PacketTooLargeError(len(packet))
        if not self._in_room:
            raise NotInRoomError
        if not self._may_speak:
            raise MayNotSpeakError
        now = self._loop.time()
        if self._pace is None:
            self._pace = _Pacing(next=now)
        p = self._pace
        if now > p.next + FRAME_SECONDS * MAX_LAG_FRAMES:
            p.ts = (p.ts + FRAME_SAMPLES * int((now - p.next) / FRAME_SECONDS)) & 0xFFFFFFFF
            p.next = now
        slot, ts = p.next, p.ts
        p.next += FRAME_SECONDS
        p.ts = (p.ts + FRAME_SAMPLES) & 0xFFFFFFFF

        delay = slot - self._loop.time()
        if delay > 0:
            await asyncio.sleep(delay)

        sess = self._sess
        if not self._in_room or sess is None:
            raise NotInRoomError
        if self._muted:
            return
        own = self._own
        ctr = own.ctr
        own.ctr += 1
        started = not self._speaking
        self._speaking = True
        self._last_send = self._loop.time()
        sealed = c.voice_packet_seal(own.key, own.salt, own.key_id, ctr, ts, packet)
        if started:
            await self._stream.send({"type": "voice_speaking", "channel_id": self._channel_id, "speaking": True})
        sess.send_datagram(sealed)

    async def send_pcm(self, pcm: Sequence[float]) -> None:
        """Sends one 20 ms frame of 48 kHz mono PCM (960 samples), encoded and sent
        as `send_opus`. Needs the opus extra."""
        if self._codec is None:
            raise VoiceError("PCM is off: join with pcm=True (needs the opus extra)")
        if len(pcm) != FRAME_SAMPLES:
            raise BadFrameError(f"{len(pcm)} samples, not {FRAME_SAMPLES}")
        await self.send_opus(self._codec.encode(pcm))

    def set_position(self, zone_id: str, position: Sequence[float]) -> None:
        """Sets the latest position in a zone of this room. At most one reaches the
        hub every 50 ms (it silently drops one under 30 ms after the last); the
        newest is always the one sent. The zone and the number of coordinates are
        checked here. A refusal by the hub arrives as PositionRefused."""
        zone = next((z for z in self._zones if z.zone_id == zone_id), None)
        if zone is None:
            raise UnknownZoneError(zone_id)
        want = {"2d": 2, "3d": 3}.get(zone.coordinate_system, min(max(len(position), 1), 3))
        if len(position) != want:
            raise BadPositionError(len(position), want)
        self._position = (zone_id, [float(x) for x in position])

    async def create_zone(
        self,
        zone_id: str,
        name: str,
        coordinate_system: str = "2d",
        attenuation: dict[str, Any] | None = None,
        auth_mode: str = "any_channel_member",
    ) -> None:
        """Needs channels.manage on the channel. `attenuation` is the hub's
        {model, max_radius, ref_dist, rolloff} object; None takes the defaults.
        `auth_mode` is "creator_only" or "any_channel_member"."""
        await self._stream.send(
            {
                "type": "voice_zone_create",
                "zone_id": zone_id,
                "name": name,
                "coordinate_system": coordinate_system,
                "attenuation": attenuation or {},
                "auth_mode": auth_mode,
            }
        )

    async def destroy_zone(self, zone_id: str) -> None:
        await self._stream.send({"type": "voice_zone_destroy", "zone_id": zone_id})

    async def leave(self) -> None:
        """Sends voice_leave, then closes the audio session and the room's socket.
        Closing the WebTransport session alone would not leave the roster."""
        was_in = self._in_room
        self._in_room = False
        sess, self._sess = self._sess, None
        try:
            if was_in:
                if self._speaking:
                    await self._try_send({"type": "voice_speaking", "channel_id": self._channel_id, "speaking": False})
                await self._try_send({"type": "voice_leave", "channel_id": self._channel_id})
        finally:
            if sess is not None:
                await sess.close()
            # Lets the hub read voice_leave before the socket closes.
            await asyncio.sleep(0.1)
            for t in list(self._tasks):
                t.cancel()
            await self._stream.close()
            self._emit_end()
