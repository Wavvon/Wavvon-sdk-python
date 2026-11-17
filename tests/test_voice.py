from __future__ import annotations

import asyncio
import os
from typing import Any

import pytest

from wavvon import WavvonClient
from wavvon import _crypto as c
from wavvon.voice import Audio, BadFrameError, BadPositionError, UnknownZoneError, Voice
from wavvon.voice._opus import check_20ms, opus_duration_micros
from wavvon.voice.session import Participant, Zone, _OwnKey


def test_opus_durations() -> None:
    assert opus_duration_micros(b"\xf8" + b"x" * 10) == 20_000  # CELT FB 20 ms, one frame
    assert opus_duration_micros(b"\xf9\x00\x00") == 40_000  # code 1: two 20 ms frames
    assert opus_duration_micros(bytes([(1 << 3) | 0, 0])) == 20_000  # SILK NB 20 ms
    check_20ms(b"\xf8abc")
    with pytest.raises(ValueError):
        check_20ms(b"\xf9abc")
    with pytest.raises(ValueError):
        check_20ms(b"")


class _FakeStream:
    def __init__(self) -> None:
        self.sent: list[dict[str, Any]] = []

    async def send(self, msg: dict[str, Any]) -> None:
        self.sent.append(msg)

    async def close(self) -> None:
        pass


class _FakeSession:
    def __init__(self) -> None:
        self.datagrams: list[bytes] = []

    def send_datagram(self, b: bytes) -> None:
        self.datagrams.append(b)

    async def close(self) -> None:
        pass


def room() -> tuple[Voice, _FakeStream, _FakeSession]:
    client = WavvonClient("http://localhost:1", seed=os.urandom(32))
    stream, sess = _FakeStream(), _FakeSession()
    v = Voice(client, stream, None, "chan")  # type: ignore[arg-type]
    v._sess = sess  # type: ignore[assignment]
    v._in_room = True
    v._own = _OwnKey(os.urandom(32), os.urandom(4), 1)
    return v, stream, sess


async def test_send_is_paced_and_ts_advances() -> None:
    v, stream, sess = room()
    started = asyncio.get_running_loop().time()
    for _ in range(6):
        await v.send_opus(b"\xf8" + b"x" * 20)
    took = asyncio.get_running_loop().time() - started
    assert 0.08 <= took < 0.3  # five 20 ms slots after the first
    assert len(sess.datagrams) == 6
    headers = [c.voice_packet_open(v._own.key, v._own.salt, d)[:3] for d in sess.datagrams]
    assert [h[1] for h in headers] == list(range(6))
    assert [h[2] for h in headers] == [960 * n for n in range(6)]
    assert [m["speaking"] for m in stream.sent if m["type"] == "voice_speaking"] == [True]


async def test_refuses_what_listeners_cannot_play() -> None:
    v, _, sess = room()
    with pytest.raises(BadFrameError):
        await v.send_opus(b"\xf9\x00\x00")
    assert sess.datagrams == []


async def test_muted_sends_nothing_but_keeps_pace() -> None:
    v, _, sess = room()
    v.set_muted(True)
    await v.send_opus(b"\xf8abc")
    assert sess.datagrams == []


async def test_receive_replay_watermark_and_forgery() -> None:
    v, _, _ = room()
    key, salt = os.urandom(32), os.urandom(4)
    v._roster = {7: Participant("peer", 7)}
    v._remote = {("peer", 1): (key, salt)}

    def downlink(ctr: int, body: bytes = b"\xf8hello") -> bytes:
        return (7).to_bytes(2, "big") + b"\x00" + c.voice_packet_seal(key, salt, 1, ctr, 960 * ctr, body)

    v._handle_datagram(downlink(0))
    v._handle_datagram(downlink(0))  # replay
    forged = bytearray(downlink(5))
    forged[-1] ^= 1
    v._handle_datagram(bytes(forged))  # must not move the watermark
    v._handle_datagram(downlink(1))
    got = [v._events.get_nowait() for _ in range(v._events.qsize())]
    assert [(e.ctr, e.opus) for e in got if isinstance(e, Audio)] == [(0, b"\xf8hello"), (1, b"\xf8hello")]
    v.set_deafened(True)
    v._handle_datagram(downlink(2))
    assert v._events.empty()


async def test_position_checks_and_coalescing() -> None:
    v, _, _ = room()
    v._zones = [Zone("z", "zone", "2d")]
    with pytest.raises(UnknownZoneError):
        v.set_position("nope", [1, 2])
    with pytest.raises(BadPositionError):
        v.set_position("z", [1, 2, 3])
    for i in range(5):
        v.set_position("z", [float(i), 0.0])
    assert v._position == ("z", [4.0, 0.0])
