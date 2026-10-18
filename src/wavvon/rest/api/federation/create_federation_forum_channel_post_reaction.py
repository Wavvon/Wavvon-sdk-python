from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_federation_forum_channel_post_reaction_body import (
    CreateFederationForumChannelPostReactionBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    post_id: str,
    *,
    body: CreateFederationForumChannelPostReactionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/federation/forum/channels/{channel_id}/posts/{post_id}/reactions".format(
            channel_id=quote(str(channel_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateFederationForumChannelPostReactionBody | Unset = UNSET,
) -> Response[Any]:
    """A peer hub adds one of its users' reactions to a post

    Args:
        channel_id (str):
        post_id (str):
        body (CreateFederationForumChannelPostReactionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    channel_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateFederationForumChannelPostReactionBody | Unset = UNSET,
) -> Response[Any]:
    """A peer hub adds one of its users' reactions to a post

    Args:
        channel_id (str):
        post_id (str):
        body (CreateFederationForumChannelPostReactionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        post_id=post_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
