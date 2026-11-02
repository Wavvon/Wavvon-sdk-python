from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_hub_pending_response_200_item import ListHubPendingResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hub/pending",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListHubPendingResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListHubPendingResponse200Item.from_dict(
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
) -> Response[list[ListHubPendingResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[ListHubPendingResponse200Item]]:
    """List users awaiting approval (admin)

     Oldest first — the queue is worked from the front, so the cursor moves
    forward through the list rather than back like the newest-first ones.
    Paged only on hubs advertising `list.cursor.lists`.

    Args:
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListHubPendingResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[ListHubPendingResponse200Item] | None:
    """List users awaiting approval (admin)

     Oldest first — the queue is worked from the front, so the cursor moves
    forward through the list rather than back like the newest-first ones.
    Paged only on hubs advertising `list.cursor.lists`.

    Args:
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListHubPendingResponse200Item]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[ListHubPendingResponse200Item]]:
    """List users awaiting approval (admin)

     Oldest first — the queue is worked from the front, so the cursor moves
    forward through the list rather than back like the newest-first ones.
    Paged only on hubs advertising `list.cursor.lists`.

    Args:
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListHubPendingResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[ListHubPendingResponse200Item] | None:
    """List users awaiting approval (admin)

     Oldest first — the queue is worked from the front, so the cursor moves
    forward through the list rather than back like the newest-first ones.
    Paged only on hubs advertising `list.cursor.lists`.

    Args:
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListHubPendingResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
