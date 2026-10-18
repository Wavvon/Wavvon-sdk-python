from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_channel_posts_response_200 import SearchChannelPostsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    channel_id: str,
    *,
    q: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

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
) -> SearchChannelPostsResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchChannelPostsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchChannelPostsResponse200]:
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
) -> Response[SearchChannelPostsResponse200]:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChannelPostsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
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
) -> SearchChannelPostsResponse200 | None:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChannelPostsResponse200
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        q=q,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
) -> Response[SearchChannelPostsResponse200]:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChannelPostsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str,
) -> SearchChannelPostsResponse200 | None:
    """Full-text search within a forum channel

    Args:
        channel_id (str):
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChannelPostsResponse200
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            q=q,
        )
    ).parsed
