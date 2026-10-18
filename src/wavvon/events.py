from __future__ import annotations

import asyncio
import inspect
import json
import logging
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any, Literal, Protocol, TypedDict, cast

from .retry import RetryOptions, backoff_delay

if TYPE_CHECKING:
    from .webhooks import Embed, GameLaunchCard

log = logging.getLogger("wavvon")

# Server -> client frames this SDK knows (ws-protocol.md, checked against
# Wavvon-server crates/hub/src/routes/chat_models.rs). Every other `type`
# arrives as UnknownEvent with the raw frame.


class Message(TypedDict, total=False):
    id: str
    channel_id: str
    sender: str
    sender_name: str | None
    content: str
    created_at: int
    edited_at: int | None
    attachments: list[dict[str, Any]]
    reactions: list[dict[str, Any]]
    reply_to: dict[str, Any]
    visible_to_pubkey: str
    reply_count: int
    embeds: list[Embed]
    game: GameLaunchCard


class _HubEventBase(TypedDict):
    type: Literal["hub_event"]
    seq: int
    event: str
    """e.g. `member.joined`, `message.created`."""
    hub_url: str
    at: int
    payload: dict[str, Any]


class HubEvent(_HubEventBase, total=False):
    """One envelope for live push, replay and outgoing webhooks (apps.md §5).
    The optional fields come with replay only, when the audit row has them."""

    actor_pubkey: str
    target_pubkey: str
    channel_id: str
    replayed: bool


class HelloEvent(TypedDict):
    type: Literal["hello"]
    live_seq: int


class ErrorEvent(TypedDict):
    type: Literal["error"]
    context: str
    message: str


class _PongBase(TypedDict):
    type: Literal["pong"]
    nonce: int


class PongEvent(_PongBase, total=False):
    outbound_loss_pct: float


class MessageEvent(TypedDict):
    type: Literal["message", "message_edited"]
    channel_id: str
    message: Message


class MessageRefEvent(TypedDict):
    type: Literal["message_deleted", "message_pinned", "message_unpinned"]
    channel_id: str
    message_id: str


class ReactionsUpdatedEvent(TypedDict):
    type: Literal["reactions_updated"]
    channel_id: str
    message_id: str
    reactions: list[dict[str, Any]]


class TypingEvent(TypedDict):
    type: Literal["typing"]
    channel_id: str
    public_key: str
    display_name: str | None
    typing: bool


class DmEvent(TypedDict):
    type: Literal["dm"]
    conversation_id: str
    sender: str
    sender_name: str | None
    content: str
    timestamp: int


class ReplayCompleteEvent(TypedDict):
    type: Literal["replay_complete"]
    replayed: int
    live_from_seq: int


class ReplayUnavailableEvent(TypedDict):
    type: Literal["replay_unavailable"]
    earliest_seq: int
    earliest_at: int


class AppLaunchEvent(TypedDict):
    type: Literal["app_launch"]
    app_id: str
    title: str
    description: str
    channel_id: str


class AppOpenEvent(TypedDict):
    type: Literal["app_open"]
    app_id: str
    channel_id: str
    mini_app_url: str
    session_token: str
    requires_camera: bool


class AppCloseEvent(TypedDict):
    type: Literal["app_close"]
    app_id: str
    channel_id: str


class _MiniAppMessageBase(TypedDict):
    type: Literal["mini_app_message"]
    app_id: str
    channel_id: str
    payload: str


class MiniAppMessageEvent(_MiniAppMessageBase, total=False):
    from_pubkey: str


class UnknownEvent(TypedDict):
    """A frame of a type this SDK does not model (or not JSON at all). Never swallowed."""

    type: Literal["unknown"]
    raw_type: str
    """The frame's own `type`, "binary" for a binary frame, "" if unparseable."""
    raw: Any


KnownEvent = (
    HelloEvent
    | ErrorEvent
    | PongEvent
    | MessageEvent
    | MessageRefEvent
    | ReactionsUpdatedEvent
    | TypingEvent
    | DmEvent
    | HubEvent
    | ReplayCompleteEvent
    | ReplayUnavailableEvent
    | AppLaunchEvent
    | AppOpenEvent
    | AppCloseEvent
    | MiniAppMessageEvent
)
WsEvent = KnownEvent | UnknownEvent

KNOWN_TYPES = frozenset(
    {
        "hello",
        "error",
        "pong",
        "message",
        "message_edited",
        "message_deleted",
        "message_pinned",
        "message_unpinned",
        "reactions_updated",
        "typing",
        "dm",
        "hub_event",
        "replay_complete",
        "replay_unavailable",
        "app_launch",
        "app_open",
        "app_close",
        "mini_app_message",
    }
)


def parse_frame(data: str | bytes) -> WsEvent:
    """Turns one WebSocket frame into a typed event."""
    if not isinstance(data, str):
        return {"type": "unknown", "raw_type": "binary", "raw": data}
    try:
        frame = json.loads(data)
    except ValueError:
        return {"type": "unknown", "raw_type": "", "raw": data}
    t = frame.get("type") if isinstance(frame, dict) else None
    if isinstance(t, str) and t in KNOWN_TYPES:
        return cast(KnownEvent, frame)
    return {"type": "unknown", "raw_type": t if isinstance(t, str) else "", "raw": frame}


ConnectionState = Literal["connecting", "open", "reconnecting", "closed"]


class WebSocketLike(Protocol):
    """The subset of a websockets connection this SDK uses."""

    async def send(self, message: str) -> None: ...
    async def recv(self) -> str | bytes: ...
    async def close(self) -> None: ...


WebSocketConnect = Callable[[str], Awaitable[WebSocketLike]]
Handler = Callable[[Any], Any]


async def _default_connect(url: str) -> WebSocketLike:
    from websockets.asyncio.client import connect

    return cast(WebSocketLike, await connect(url))


class EventStream:
    """One hub WebSocket that reconnects on its own. Tracks the last hub_event
    seq and sends `resume` after every reconnect, so an app misses nothing
    inside the hub's 72-hour window; `replay_unavailable` is delivered like any
    other event when it falls outside. The hub only honours `resume` (and only
    pushes hub_event) for an identity whose app profile existed when the
    socket connected: register the profile first.

    Handlers run in the read loop; a coroutine a handler returns is scheduled
    as a task. A handler that raises is logged and does not kill the stream."""

    def __init__(
        self,
        *,
        url: Callable[[], Awaitable[str]],
        reauthenticate: Callable[[], Awaitable[None]],
        ws_connect: WebSocketConnect | None = None,
        retry: RetryOptions | None = None,
        since_seq: int | None = None,
    ) -> None:
        self._url = url
        self._reauthenticate = reauthenticate
        self._connect = ws_connect or _default_connect
        self._retry = retry
        self._handlers: dict[str, list[Handler]] = {}
        self._state_handlers: list[Callable[[ConnectionState], None]] = []
        self._ws: WebSocketLike | None = None
        self._state: ConnectionState = "connecting"
        self._stopped = False
        self._tasks: set[asyncio.Task[Any]] = set()
        self.last_seq: int | None = since_seq
        """Highest hub_event seq seen (or the hub's live seq at first connect)."""
        self._runner = asyncio.get_running_loop().create_task(self._run())

    @property
    def state(self) -> ConnectionState:
        return self._state

    def on_state_change(self, fn: Callable[[ConnectionState], None]) -> Callable[[], None]:
        self._state_handlers.append(fn)
        return lambda: self._state_handlers.remove(fn)

    def on(self, type: str, fn: Handler) -> Callable[[], None]:
        """Subscribe to one event type, "unknown", or "*" for everything. Returns an unsubscribe."""
        self._handlers.setdefault(type, []).append(fn)
        return lambda: self._handlers[type].remove(fn)

    async def send(self, message: dict[str, Any]) -> None:
        """Send a client frame (ws-protocol.md): subscribe, typing, ping, ..."""
        if self._ws is None or self._state != "open":
            raise RuntimeError(f"socket is {self._state}, not open")
        await self._ws.send(json.dumps(message))

    async def announce_app(self, channel_id: str, title: str, description: str) -> None:
        """Mini-app host: show a launch card in a channel."""
        await self.send({"type": "app_announce", "channel_id": channel_id, "title": title, "description": description})

    async def dismiss_app(self, channel_id: str) -> None:
        """Mini-app host: close the session; clients dismiss their webviews."""
        await self.send({"type": "app_dismiss", "channel_id": channel_id})

    async def send_mini_app_message(self, app_id: str, channel_id: str, to_pubkey: str, payload: str) -> None:
        """Mini-app host: relay an opaque payload to one joined player's mini-app.
        Players' messages arrive as `mini_app_message` events with `from_pubkey`."""
        await self.send(
            {
                "type": "mini_app_message",
                "app_id": app_id,
                "channel_id": channel_id,
                "payload": payload,
                "to_pubkey": to_pubkey,
            }
        )

    async def close(self) -> None:
        self._stopped = True
        ws = self._ws
        self._runner.cancel()
        if ws is not None:
            try:
                await ws.close()
            except Exception:
                pass
        self._set_state("closed")

    def _set_state(self, s: ConnectionState) -> None:
        if s == self._state:
            return
        self._state = s
        for fn in list(self._state_handlers):
            fn(s)

    def _emit(self, event: WsEvent) -> None:
        for key in (event["type"], "*"):
            for fn in list(self._handlers.get(key, [])):
                try:
                    result = fn(event)
                    if inspect.isawaitable(result):
                        task = asyncio.ensure_future(result)
                        self._tasks.add(task)
                        task.add_done_callback(self._task_done)
                except Exception:
                    log.exception("wavvon: event handler for %s raised", key)

    def _task_done(self, task: asyncio.Task[Any]) -> None:
        self._tasks.discard(task)
        if not task.cancelled() and task.exception() is not None:
            log.error("wavvon: async event handler raised", exc_info=task.exception())

    async def _run(self) -> None:
        attempt = 0
        while not self._stopped:
            greeted = False
            try:
                ws = await self._connect(await self._url())
            except Exception as e:
                log.debug("wavvon: socket connect failed: %r", e)
            else:
                self._ws = ws
                try:
                    while True:
                        event = parse_frame(await ws.recv())
                        if event["type"] == "hello":
                            greeted = True
                            attempt = 0
                            self._set_state("open")
                            if self.last_seq is None:
                                self.last_seq = event["live_seq"]
                            else:
                                await ws.send(json.dumps({"type": "resume", "since_seq": self.last_seq}))
                        elif event["type"] == "hub_event":
                            # Live events that arrived during a replay are flushed
                            # after it and can repeat what the replay carried.
                            if self.last_seq is not None and event["seq"] <= self.last_seq:
                                continue
                            self.last_seq = event["seq"]
                        self._emit(event)
                except Exception as e:
                    log.debug("wavvon: socket closed: %r", e)
                finally:
                    self._ws = None
            if self._stopped:
                return
            self._set_state("reconnecting")
            attempt += 1
            await asyncio.sleep(backoff_delay(attempt, self._retry))
            if not greeted:
                # A refused upgrade and a dropped one look alike from here; a
                # fresh session costs one login and rules out the token.
                try:
                    await self._reauthenticate()
                except Exception as e:
                    log.debug("wavvon: re-authentication failed: %r", e)
