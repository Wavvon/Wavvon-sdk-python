from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hub_event import HubEvent
from ...models.list_me_events_response_410 import ListMeEventsResponse410
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/me/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListMeEventsResponse410 | list[HubEvent] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HubEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 410:
        response_410 = ListMeEventsResponse410.from_dict(response.json())

        return response_410

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListMeEventsResponse410 | list[HubEvent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ListMeEventsResponse410 | list[HubEvent]]:
    """Poll the hub events the caller subscribed to

     The polling transport for a program holding no WebSocket. It reads the audit log that WebSocket
    `Resume` replays, so each item is the same `hub_event` envelope the socket pushes: events of the
    caller's subscribed types after `cursor`, in channels it can read, oldest first. Nothing is queued
    or acknowledged; pass the last `seq` seen as `cursor`. Without one, the poll starts at the beginning
    of the 72-hour window.

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMeEventsResponse410 | list[HubEvent]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 100,
) -> ListMeEventsResponse410 | list[HubEvent] | None:
    """Poll the hub events the caller subscribed to

     The polling transport for a program holding no WebSocket. It reads the audit log that WebSocket
    `Resume` replays, so each item is the same `hub_event` envelope the socket pushes: events of the
    caller's subscribed types after `cursor`, in channels it can read, oldest first. Nothing is queued
    or acknowledged; pass the last `seq` seen as `cursor`. Without one, the poll starts at the beginning
    of the 72-hour window.

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMeEventsResponse410 | list[HubEvent]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ListMeEventsResponse410 | list[HubEvent]]:
    """Poll the hub events the caller subscribed to

     The polling transport for a program holding no WebSocket. It reads the audit log that WebSocket
    `Resume` replays, so each item is the same `hub_event` envelope the socket pushes: events of the
    caller's subscribed types after `cursor`, in channels it can read, oldest first. Nothing is queued
    or acknowledged; pass the last `seq` seen as `cursor`. Without one, the poll starts at the beginning
    of the 72-hour window.

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMeEventsResponse410 | list[HubEvent]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 100,
) -> ListMeEventsResponse410 | list[HubEvent] | None:
    """Poll the hub events the caller subscribed to

     The polling transport for a program holding no WebSocket. It reads the audit log that WebSocket
    `Resume` replays, so each item is the same `hub_event` envelope the socket pushes: events of the
    caller's subscribed types after `cursor`, in channels it can read, oldest first. Nothing is queued
    or acknowledged; pass the last `seq` seen as `cursor`. Without one, the poll starts at the beginning
    of the 72-hour window.

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMeEventsResponse410 | list[HubEvent]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
