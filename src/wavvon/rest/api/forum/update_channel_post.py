from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.update_channel_post_body import UpdateChannelPostBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    post_id: str,
    *,
    body: UpdateChannelPostBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/channels/{channel_id}/posts/{post_id}".format(
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
) -> Any:
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
    body: UpdateChannelPostBody | Unset = UNSET,
) -> Response[Any]:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody | Unset):

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
    body: UpdateChannelPostBody | Unset = UNSET,
) -> Response[Any]:
    """Edit a post's title and/or body (author or manage_posts)

    Args:
        channel_id (str):
        post_id (str):
        body (UpdateChannelPostBody | Unset):

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
