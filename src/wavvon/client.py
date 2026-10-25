from __future__ import annotations

import asyncio
import json
import re
from collections.abc import Callable, Mapping, Sequence
from typing import Any, Literal, TypedDict, TypeVar, cast
from urllib.parse import quote

import httpx

from .auth import Identity, Session, authenticate, identity_from_seed
from .errors import HubError, ReplayUnavailableError, UnsupportedByHubError
from .events import EventStream, HubEvent, WebSocketConnect
from .rest.api.apps import (
    list_me_events,
    set_me_app_commands,
    set_me_app_profile,
    set_me_app_subscriptions,
)
from .rest.client import Client as RestClient
from .rest.models.app_command_def import AppCommandDef
from .rest.models.app_subscription import AppSubscription as AppSubscription
from .rest.models.set_me_app_commands_body import SetMeAppCommandsBody
from .rest.models.set_me_app_profile_body import SetMeAppProfileBody
from .rest.models.set_me_app_subscriptions_body import SetMeAppSubscriptionsBody
from .rest.types import Response
from .retry import RetryOptions, fetch_with_retry

AppProfile = SetMeAppProfileBody
AppCommand = AppCommandDef

SessionState = Literal["signed-out", "authenticating", "ready"]

T = TypeVar("T")


class HubInfo(TypedDict, total=False):
    """GET /info. Kept as the hub's own JSON: a generated model would refuse an
    enum value this SDK does not know yet."""

    name: str
    icon: str | None
    public_key: str
    version: str
    capabilities: list[str]
    canonical_url: str
    invite_only: bool
    farm_url: str | None


class _AuthedTransport(httpx.AsyncBaseTransport):
    """Adds the bearer, retries transient failures and re-authenticates once on 401."""

    def __init__(self, client: WavvonClient, inner: httpx.AsyncBaseTransport) -> None:
        self._client = client
        self._inner = inner

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        body = await request.aread()

        async def send(token: str) -> httpx.Response:
            async def attempt() -> httpx.Response:
                req = httpx.Request(
                    request.method, request.url, headers=request.headers, content=body, extensions=request.extensions
                )
                req.headers["Authorization"] = f"Bearer {token}"
                res = await self._inner.handle_async_request(req)
                await res.aread()
                return res

            return await fetch_with_retry(attempt, self._client._retry)

        session = await self._client.login()
        res = await send(session.token)
        if res.status_code != 401:
            return res
        await res.aclose()
        return await send((await self._client._relogin(session.token)).token)

    async def aclose(self) -> None:
        pass  # the inner transport belongs to WavvonClient._plain


def ok(result: Response[T]) -> T:
    """Generated-call result -> parsed body, or a HubError carrying the hub's own
    words. Where the spec gives a response no schema, the decoded JSON body."""
    if result.status_code >= 300:
        raise HubError(int(result.status_code), result.content.decode("utf-8", "replace"))
    if result.parsed is None and result.content:
        try:
            return cast(T, json.loads(result.content))
        except ValueError:
            pass
    return cast(T, result.parsed)


class WavvonClient:
    """A program's connection to one hub: a session that renews itself, the
    generated REST client (`rest`), capability checks, app registration and
    the event stream. Use as `async with WavvonClient(...) as client:`.

    `seed` is a 32-byte Ed25519 seed (hex or bytes) and is never sent
    anywhere; pass `identity` instead to sign elsewhere. `invite_code` admits
    the program on an invite_only hub. `transport` and `ws_connect` are seams
    for tests and custom networking."""

    def __init__(
        self,
        hub_url: str,
        *,
        seed: str | bytes | None = None,
        identity: Identity | None = None,
        invite_code: str | None = None,
        retry: RetryOptions | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        ws_connect: WebSocketConnect | None = None,
    ) -> None:
        self.hub_url = hub_url.rstrip("/")
        if identity is not None:
            self.identity = identity
        elif seed is not None:
            self.identity = identity_from_seed(seed)
        else:
            raise ValueError("WavvonClient needs a seed or an identity")
        self._invite_code = invite_code
        self._retry = retry
        self._transport = transport or httpx.AsyncHTTPTransport()
        self._ws_connect = ws_connect
        self._session: Session | None = None
        self._logging_in: asyncio.Future[Session] | None = None
        self._info: HubInfo | None = None
        self._state: SessionState = "signed-out"
        self._state_handlers: list[Callable[[SessionState], None]] = []
        self._plain = httpx.AsyncClient(base_url=self.hub_url, transport=self._transport, timeout=None)
        self.rest = RestClient(base_url=self.hub_url)
        """Typed REST client generated from openapi.yaml; pass it as `client=`
        to any function under `wavvon.api`. Bearer, retry and re-auth are built in."""
        self.rest.set_async_httpx_client(
            httpx.AsyncClient(base_url=self.hub_url, transport=_AuthedTransport(self, self._transport), timeout=None)
        )

    async def __aenter__(self) -> WavvonClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self.rest.get_async_httpx_client().aclose()
        await self._plain.aclose()

    @property
    def state(self) -> SessionState:
        return self._state

    def on_state_change(self, fn: Callable[[SessionState], None]) -> Callable[[], None]:
        """ "authenticating" after a dead session is the reconnecting state of REST."""
        self._state_handlers.append(fn)
        return lambda: self._state_handlers.remove(fn)

    @property
    def canonical_pubkey(self) -> str | None:
        """The identity the hub attributes this program's actions to."""
        return self._session.canonical_pubkey if self._session else None

    async def login(self) -> Session:
        """The current session, logging in if there is none."""
        return self._session or await self._relogin(None)

    async def _relogin(self, stale_token: str | None) -> Session:
        # Someone else already replaced the token this caller saw fail.
        if self._session and self._session.token != stale_token:
            return self._session
        if self._logging_in is None:
            self._logging_in = asyncio.ensure_future(self._do_login())
        return await asyncio.shield(self._logging_in)

    async def _do_login(self) -> Session:
        self._set_state("authenticating")
        try:
            self._session = await authenticate(
                self.hub_url,
                self.identity,
                invite_code=self._invite_code,
                retry=self._retry,
                http=self._plain,
            )
            self._set_state("ready")
            return self._session
        except BaseException:
            self._session = None
            self._set_state("signed-out")
            raise
        finally:
            self._logging_in = None

    def _set_state(self, s: SessionState) -> None:
        if s == self._state:
            return
        self._state = s
        for fn in list(self._state_handlers):
            fn(s)

    async def info(self, refresh: bool = False) -> HubInfo:
        """GET /info, cached; `refresh` re-reads it."""
        if self._info is None or refresh:
            res = await fetch_with_retry(lambda: self._plain.get("/info"), self._retry)
            if res.status_code >= 300:
                raise HubError(res.status_code, res.text)
            self._info = cast(HubInfo, res.json())
        return self._info

    async def has_capability(self, name: str) -> bool:
        """Whether the hub advertises `name`. Capabilities, never versions."""
        return name in ((await self.info()).get("capabilities") or [])

    async def require_capability(self, name: str) -> None:
        """Raises UnsupportedByHubError unless the hub advertises `name`."""
        if not await self.has_capability(name):
            raise UnsupportedByHubError(name)

    # ---- app registration (apps.md §2), gated on `apps.register` ----

    async def set_app_profile(self, profile: AppProfile | Mapping[str, Any]) -> None:
        """Register or replace this identity's app profile. Do it before `connect()`."""
        await self.require_capability("apps.register")
        body = profile if isinstance(profile, AppProfile) else AppProfile.from_dict(profile)
        ok(await set_me_app_profile.asyncio_detailed(client=self.rest, body=body))

    async def set_app_commands(self, commands: Sequence[AppCommand | Mapping[str, Any]]) -> None:
        await self.require_capability("apps.register")
        items = [c if isinstance(c, AppCommand) else AppCommand.from_dict(c) for c in commands]
        ok(await set_me_app_commands.asyncio_detailed(client=self.rest, body=SetMeAppCommandsBody(commands=items)))

    async def set_app_subscriptions(self, subscriptions: Sequence[AppSubscription | Mapping[str, Any]]) -> None:
        """A `message.*` subscription must name its channels."""
        await self.require_capability("apps.register")
        items = [s if isinstance(s, AppSubscription) else AppSubscription.from_dict(s) for s in subscriptions]
        body = SetMeAppSubscriptionsBody(subscriptions=items)
        ok(await set_me_app_subscriptions.asyncio_detailed(client=self.rest, body=body))

    # ---- events ----

    def connect(self, *, since_seq: int | None = None) -> EventStream:
        """Opens the hub WebSocket in the running event loop. Reconnects,
        re-authenticates and resumes on its own. `since_seq` replays hub events
        after that seq on the first connect (an app persisting its position);
        without it the stream starts from now."""

        async def url() -> str:
            token = (await self.login()).token
            return f"{re.sub(r'^http', 'ws', self.hub_url)}/ws?token={quote(token, safe='')}"

        async def reauthenticate() -> None:
            await self._relogin(self._session.token if self._session else None)

        return EventStream(
            url=url, reauthenticate=reauthenticate, ws_connect=self._ws_connect, retry=self._retry, since_seq=since_seq
        )

    async def poll_events(self, cursor: int | None = None, limit: int | None = None) -> list[HubEvent]:
        """GET /me/events: the polling transport, for a program that holds no socket.

        Returns the same hub_event envelopes the socket replays, oldest first.
        Nothing is acknowledged: pass the last `seq` handled as `cursor`. No
        cursor starts at the beginning of the hub's 72-hour window; a cursor
        older than it raises ReplayUnavailableError."""
        kwargs: dict[str, int] = {}
        if cursor is not None:
            kwargs["cursor"] = cursor
        if limit is not None:
            kwargs["limit"] = limit
        res = await list_me_events.asyncio_detailed(client=self.rest, **kwargs)
        if res.status_code == 410:
            gone = json.loads(res.content)
            raise ReplayUnavailableError(int(gone["earliest_seq"]), int(gone["earliest_at"]))
        if res.status_code >= 300:
            raise HubError(int(res.status_code), res.content.decode("utf-8", "replace"))
        try:
            rows = json.loads(res.content)
        except ValueError:
            rows = None
        if not isinstance(rows, list):
            raise HubError(200, "GET /me/events answered without an array")
        return cast(list[HubEvent], rows)
