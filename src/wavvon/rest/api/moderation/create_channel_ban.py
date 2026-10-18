from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_channel_ban_body import CreateChannelBanBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    body: CreateChannelBanBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/channels/{channel_id}/bans".format(
            channel_id=quote(str(channel_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateChannelBanBody | Unset = UNSET,
) -> Response[Any]:
    """Ban a user from a channel (ban_members)

     The only channel-ban write path. A duplicate family under /moderation/channels/{id}/bans was folded
    in on 2026-08-08; this route used to hardcode `reason` to null on insert, silently erasing a reason
    written through the other one.

    Args:
        channel_id (str):
        body (CreateChannelBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateChannelBanBody | Unset = UNSET,
) -> Response[Any]:
    """Ban a user from a channel (ban_members)

     The only channel-ban write path. A duplicate family under /moderation/channels/{id}/bans was folded
    in on 2026-08-08; this route used to hardcode `reason` to null on insert, silently erasing a reason
    written through the other one.

    Args:
        channel_id (str):
        body (CreateChannelBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
