from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ticket: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ticket"] = ticket

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ws",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 101:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 429:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ticket: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[Any]:
    """Realtime WebSocket endpoint

     Upgrades to a WebSocket carrying all realtime traffic. Authenticate
    with a single-use `ticket` from `POST /ws/ticket` (hubs advertising
    the `ws.ticket` capability), or with the `token` query parameter
    (the session token itself, which then sits in the URL). The upgrade
    is rejected with `401`/`403` on invalid, expired, or banned
    credentials, and `429` when the identity already holds the maximum
    number of open sockets.

    The full message catalogue — every client→server and server→client
    JSON message with exact field names and types — is documented in
    [`docs/ws-protocol.md`](docs/ws-protocol.md) (see also the
    "WebSocket protocol" section of this file's description).

    Args:
        ticket (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ticket=ticket,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ticket: str | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[Any]:
    """Realtime WebSocket endpoint

     Upgrades to a WebSocket carrying all realtime traffic. Authenticate
    with a single-use `ticket` from `POST /ws/ticket` (hubs advertising
    the `ws.ticket` capability), or with the `token` query parameter
    (the session token itself, which then sits in the URL). The upgrade
    is rejected with `401`/`403` on invalid, expired, or banned
    credentials, and `429` when the identity already holds the maximum
    number of open sockets.

    The full message catalogue — every client→server and server→client
    JSON message with exact field names and types — is documented in
    [`docs/ws-protocol.md`](docs/ws-protocol.md) (see also the
    "WebSocket protocol" section of this file's description).

    Args:
        ticket (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ticket=ticket,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
