from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    channel_id: str,
    post_id: str,
    reply_id: str,
    emoji: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/channels/{channel_id}/posts/{post_id}/replies/{reply_id}/reactions/{emoji}".format(
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
            reply_id=quote(str(reply_id), safe=""),
            emoji=quote(str(emoji), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
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
    channel_id: str,
    post_id: str,
    reply_id: str,
    emoji: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Remove own reaction from a reply

    Args:
        channel_id (str):
        post_id (str):
        reply_id (str):
        emoji (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        reply_id=reply_id,
        emoji=emoji,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    channel_id: str,
    post_id: str,
    reply_id: str,
    emoji: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Remove own reaction from a reply

    Args:
        channel_id (str):
        post_id (str):
        reply_id (str):
        emoji (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        reply_id=reply_id,
        emoji=emoji,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
