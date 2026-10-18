from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_detail import PostDetail
from ...models.update_channel_post_body import UpdateChannelPostBody
from ...types import Response


def _get_kwargs(
    channel_id: str,
    post_id: str,
    *,
    body: UpdateChannelPostBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/channels/{channel_id}/posts/{post_id}".format(
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateChannelPostBody,
) -> Response[PostDetail]:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        body=body,
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
    body: UpdateChannelPostBody,
) -> PostDetail | None:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody):

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
        body=body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelPostBody,
) -> Response[PostDetail]:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDetail]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelPostBody,
) -> PostDetail | None:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody):

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
            body=body,
        )
    ).parsed
