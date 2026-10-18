from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_detail import PostDetail
from ...types import Response


def _get_kwargs(
    alliance_id: str,
    channel_id: str,
    post_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alliances/{alliance_id}/channels/{channel_id}/posts/{post_id}".format(
            alliance_id=quote(str(alliance_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostDetail | None:
    if response.status_code == 200:
        response_200 = PostDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PostDetail]:
    """One post with its replies, from an alliance-shared forum channel

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        channel_id=channel_id,
        post_id=post_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PostDetail | None:
    """One post with its replies, from an alliance-shared forum channel

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDetail
    """

    return sync_detailed(
        alliance_id=alliance_id,
        channel_id=channel_id,
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PostDetail]:
    """One post with its replies, from an alliance-shared forum channel

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        channel_id=channel_id,
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PostDetail | None:
    """One post with its replies, from an alliance-shared forum channel

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDetail
    """

    return (
        await asyncio_detailed(
            alliance_id=alliance_id,
            channel_id=channel_id,
            post_id=post_id,
            client=client,
        )
    ).parsed
