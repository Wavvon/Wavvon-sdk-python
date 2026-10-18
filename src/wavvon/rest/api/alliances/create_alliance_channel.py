from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_alliance_channel_body import CreateAllianceChannelBody
from ...types import Response


def _get_kwargs(
    alliance_id: str,
    *,
    body: CreateAllianceChannelBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alliances/{alliance_id}/channels".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateAllianceChannelBody,
) -> Response[Any]:
    """Share a channel into the alliance (alliance manager + channels.manage)

     Needs **both**: the right to act on this alliance (`alliances.manage` or the alliance's own grant
    list) and `channels.manage` on the channel being shared — sharing exposes a channel to people
    outside this hub, so managing one federation link must not be enough to do it alone. Also the way
    the per-share policies are changed: re-sharing a channel with `forum_remote_write` or
    `voice_remote_join` set updates that policy. An omitted policy is left as it stands, so a re-share
    to flip `include_descendants` does not silently reset one. `include_descendants` is NOT omit-safe —
    it always takes the value sent.

    Args:
        alliance_id (str):
        body (CreateAllianceChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateAllianceChannelBody,
) -> Response[Any]:
    """Share a channel into the alliance (alliance manager + channels.manage)

     Needs **both**: the right to act on this alliance (`alliances.manage` or the alliance's own grant
    list) and `channels.manage` on the channel being shared — sharing exposes a channel to people
    outside this hub, so managing one federation link must not be enough to do it alone. Also the way
    the per-share policies are changed: re-sharing a channel with `forum_remote_write` or
    `voice_remote_join` set updates that policy. An omitted policy is left as it stands, so a re-share
    to flip `include_descendants` does not silently reset one. `include_descendants` is NOT omit-safe —
    it always takes the value sent.

    Args:
        alliance_id (str):
        body (CreateAllianceChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
