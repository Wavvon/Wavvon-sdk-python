from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_events_response_200_item import ListEventsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    upcoming: bool | Unset = False,
    limit: int | Unset = 20,
    channel_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["upcoming"] = upcoming

    params["limit"] = limit

    params["channel_id"] = channel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListEventsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListEventsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListEventsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    upcoming: bool | Unset = False,
    limit: int | Unset = 20,
    channel_id: str | Unset = UNSET,
) -> Response[list[ListEventsResponse200Item]]:
    """List hub events with RSVP counts

    Args:
        upcoming (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 20.
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListEventsResponse200Item]]
    """

    kwargs = _get_kwargs(
        upcoming=upcoming,
        limit=limit,
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    upcoming: bool | Unset = False,
    limit: int | Unset = 20,
    channel_id: str | Unset = UNSET,
) -> list[ListEventsResponse200Item] | None:
    """List hub events with RSVP counts

    Args:
        upcoming (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 20.
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListEventsResponse200Item]
    """

    return sync_detailed(
        client=client,
        upcoming=upcoming,
        limit=limit,
        channel_id=channel_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    upcoming: bool | Unset = False,
    limit: int | Unset = 20,
    channel_id: str | Unset = UNSET,
) -> Response[list[ListEventsResponse200Item]]:
    """List hub events with RSVP counts

    Args:
        upcoming (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 20.
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListEventsResponse200Item]]
    """

    kwargs = _get_kwargs(
        upcoming=upcoming,
        limit=limit,
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    upcoming: bool | Unset = False,
    limit: int | Unset = 20,
    channel_id: str | Unset = UNSET,
) -> list[ListEventsResponse200Item] | None:
    """List hub events with RSVP counts

    Args:
        upcoming (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 20.
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListEventsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            upcoming=upcoming,
            limit=limit,
            channel_id=channel_id,
        )
    ).parsed
