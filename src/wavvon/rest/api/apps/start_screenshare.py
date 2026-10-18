from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_screenshare_body import StartScreenshareBody
from ...models.start_screenshare_response_200 import StartScreenshareResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: StartScreenshareBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/screenshare/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StartScreenshareResponse200 | None:
    if response.status_code == 200:
        response_200 = StartScreenshareResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | StartScreenshareResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartScreenshareBody,
) -> Response[Any | StartScreenshareResponse200]:
    """Register a video stream in a channel

     Registers a new screen-share stream for the calling identity and broadcasts `screen_share_started`
    to all channel subscribers, for a client (typically an app) that pushes frames without the WS start
    handshake. After this call the caller pushes `screen_share_chunk` binary envelopes over its WS
    connection using the returned `stream_id`. Requires `voice.join` in the channel; streams started
    this way count against a hub-wide budget.

    Args:
        body (StartScreenshareBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartScreenshareResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: StartScreenshareBody,
) -> Any | StartScreenshareResponse200 | None:
    """Register a video stream in a channel

     Registers a new screen-share stream for the calling identity and broadcasts `screen_share_started`
    to all channel subscribers, for a client (typically an app) that pushes frames without the WS start
    handshake. After this call the caller pushes `screen_share_chunk` binary envelopes over its WS
    connection using the returned `stream_id`. Requires `voice.join` in the channel; streams started
    this way count against a hub-wide budget.

    Args:
        body (StartScreenshareBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartScreenshareResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartScreenshareBody,
) -> Response[Any | StartScreenshareResponse200]:
    """Register a video stream in a channel

     Registers a new screen-share stream for the calling identity and broadcasts `screen_share_started`
    to all channel subscribers, for a client (typically an app) that pushes frames without the WS start
    handshake. After this call the caller pushes `screen_share_chunk` binary envelopes over its WS
    connection using the returned `stream_id`. Requires `voice.join` in the channel; streams started
    this way count against a hub-wide budget.

    Args:
        body (StartScreenshareBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartScreenshareResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartScreenshareBody,
) -> Any | StartScreenshareResponse200 | None:
    """Register a video stream in a channel

     Registers a new screen-share stream for the calling identity and broadcasts `screen_share_started`
    to all channel subscribers, for a client (typically an app) that pushes frames without the WS start
    handshake. After this call the caller pushes `screen_share_chunk` binary envelopes over its WS
    connection using the returned `stream_id`. Requires `voice.join` in the channel; streams started
    this way count against a hub-wide budget.

    Args:
        body (StartScreenshareBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartScreenshareResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
