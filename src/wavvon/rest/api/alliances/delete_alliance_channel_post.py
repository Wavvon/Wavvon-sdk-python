from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    alliance_id: str,
    channel_id: str,
    post_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/alliances/{alliance_id}/channels/{channel_id}/posts/{post_id}".format(
            alliance_id=quote(str(alliance_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 403:
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
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retract a post the caller's hub authored

     The owning hub honours this only when the post's `author_hub` is the calling hub **and** its author
    matches — a hub can retract its own users' content, never anyone else's.

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    alliance_id: str,
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retract a post the caller's hub authored

     The owning hub honours this only when the post's `author_hub` is the calling hub **and** its author
    matches — a hub can retract its own users' content, never anyone else's.

    Args:
        alliance_id (str):
        channel_id (str):
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        channel_id=channel_id,
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
