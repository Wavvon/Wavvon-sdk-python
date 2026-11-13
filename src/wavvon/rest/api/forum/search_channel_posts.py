from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_channel_posts_response_200_item import (
    SearchChannelPostsResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/channels/{channel_id}/posts/search".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[SearchChannelPostsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SearchChannelPostsResponse200Item.from_dict(
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
) -> Response[list[SearchChannelPostsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[list[SearchChannelPostsResponse200Item]]:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SearchChannelPostsResponse200Item]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> list[SearchChannelPostsResponse200Item] | None:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SearchChannelPostsResponse200Item]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        q=q,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[list[SearchChannelPostsResponse200Item]]:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SearchChannelPostsResponse200Item]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> list[SearchChannelPostsResponse200Item] | None:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SearchChannelPostsResponse200Item]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            q=q,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
