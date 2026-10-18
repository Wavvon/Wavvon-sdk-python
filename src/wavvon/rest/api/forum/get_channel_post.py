from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_detail import PostDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    post_id: str,
    *,
    after: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["after"] = after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/channels/{channel_id}/posts/{post_id}".format(
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
        "params": params,
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
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[PostDetail]:
    """Get a post with a page of replies

    Args:
        channel_id (str):
        post_id (str):
        after (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        after=after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> PostDetail | None:
    """Get a post with a page of replies

    Args:
        channel_id (str):
        post_id (str):
        after (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDetail
    """

    return sync_detailed(
        channel_id=channel_id,
        post_id=post_id,
        client=client,
        after=after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[PostDetail]:
    """Get a post with a page of replies

    Args:
        channel_id (str):
        post_id (str):
        after (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        after=after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> PostDetail | None:
    """Get a post with a page of replies

    Args:
        channel_id (str):
        post_id (str):
        after (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDetail
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            post_id=post_id,
            client=client,
            after=after,
            limit=limit,
        )
    ).parsed
