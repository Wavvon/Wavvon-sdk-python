from __future__ import annotations

import asyncio
import json
from typing import Any

from wavvon import ConnectionState, EventStream, RetryOptions, WebSocketLike, WsEvent, parse_frame

FAST = RetryOptions(base_delay=0.001, max_delay=0.001)


def test_parse_frame_types_known_frames() -> None:
    assert parse_frame(json.dumps({"type": "replay_unavailable", "earliest_seq": 5, "earliest_at": 1}))["type"] == (
        "replay_unavailable"
    )


def test_parse_frame_delivers_unknown_types_with_the_raw_payload() -> None:
    raw = {"type": "voice_zone_created", "zone_id": "z"}
    assert parse_frame(json.dumps(raw)) == {"type": "unknown", "raw_type": "voice_zone_created", "raw": raw}


def test_parse_frame_delivers_garbage_and_binary_as_unknown() -> None:
    assert parse_frame("{nope") == {"type": "unknown", "raw_type": "", "raw": "{nope"}
    assert parse_frame(b"\x01")["type"] == "unknown"
    assert parse_frame(json.dumps([1]))["type"] == "unknown"


class FakeSocket:
    """A scripted socket: the test pushes frames, `close` ends the connection."""

    def __init__(self, url: str) -> None:
        self.url = url
        self.sent: list[Any] = []
        self.inbox: asyncio.Queue[str | None] = asyncio.Queue()

    async def send(self, message: str) -> None:
        self.sent.append(json.loads(message))

    async def recv(self) -> str | bytes:
        frame = await self.inbox.get()
        if frame is None:
            raise ConnectionError("closed")
        return frame

    async def close(self) -> None:
        self.inbox.put_nowait(None)

    def frame(self, obj: Any) -> None:
        self.inbox.put_nowait(json.dumps(obj))


class Sockets:
    def __init__(self) -> None:
        self.all: list[FakeSocket] = []

    async def connect(self, url: str) -> WebSocketLike:
        s = FakeSocket(url)
        self.all.append(s)
        return s


async def tick() -> None:
    await asyncio.sleep(0.02)


def hub_event(seq: int) -> dict[str, Any]:
    return {"type": "hub_event", "seq": seq, "event": "member.joined", "hub_url": "h", "at": 1, "payload": {}}


async def test_resumes_from_the_last_seq_and_drops_replay_duplicates() -> None:
    sockets = Sockets()
    reauths = 0

    async def url() -> str:
        return "ws://hub/ws?token=t"

    async def reauth() -> None:
        nonlocal reauths
        reauths += 1

    stream = EventStream(url=url, reauthenticate=reauth, ws_connect=sockets.connect, retry=FAST)
    states: list[ConnectionState] = []
    stream.on_state_change(states.append)
    got: list[WsEvent] = []
    stream.on("*", got.append)
    await tick()

    first = sockets.all[0]
    first.frame({"type": "hello", "live_seq": 10})
    first.frame(hub_event(11))
    first.frame(hub_event(12))
    await tick()
    assert first.sent == []
    await first.close()
    await tick()

    second = sockets.all[1]
    second.frame({"type": "hello", "live_seq": 20})
    second.frame(hub_event(12))
    second.frame(hub_event(13))
    second.frame({"type": "replay_unavailable", "earliest_seq": 1, "earliest_at": 2})
    await tick()
    assert second.sent == [{"type": "resume", "since_seq": 12}]

    assert [e["seq"] for e in got if e["type"] == "hub_event"] == [11, 12, 13]
    assert any(e["type"] == "replay_unavailable" for e in got)
    assert states == ["open", "reconnecting", "open"]
    assert reauths == 0
    await stream.close()


async def test_reauthenticates_when_a_connection_dies_before_hello() -> None:
    sockets = Sockets()
    reauths = 0

    async def url() -> str:
        return "ws://hub/ws"

    async def reauth() -> None:
        nonlocal reauths
        reauths += 1

    stream = EventStream(url=url, reauthenticate=reauth, ws_connect=sockets.connect, retry=FAST, since_seq=4)
    await tick()
    await sockets.all[0].close()
    await tick()
    assert reauths == 1
    s = sockets.all[1]
    s.frame({"type": "hello", "live_seq": 9})
    await tick()
    assert s.sent == [{"type": "resume", "since_seq": 4}]
    await stream.close()
    assert stream.state == "closed"


async def test_a_failing_handler_does_not_kill_the_stream_and_async_handlers_run() -> None:
    sockets = Sockets()
    seen: list[str] = []

    async def url() -> str:
        return "ws://hub/ws"

    async def reauth() -> None:
        pass

    def boom(_: WsEvent) -> None:
        raise RuntimeError("handler bug")

    async def record(e: WsEvent) -> None:
        seen.append(e["type"])

    stream = EventStream(url=url, reauthenticate=reauth, ws_connect=sockets.connect, retry=FAST)
    stream.on("unknown", boom)
    stream.on("unknown", record)
    await tick()
    sockets.all[0].frame({"type": "hello", "live_seq": 1})
    sockets.all[0].frame({"type": "brand_new"})
    sockets.all[0].frame({"type": "brand_new"})
    await tick()
    assert seen == ["unknown", "unknown"]
    assert stream.state == "open"
    await stream.close()
