from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_channel_my_permissions_response_200 import (
    GetChannelMyPermissionsResponse200,
)
from ...types import Response


def _get_kwargs(
    channel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/channels/{channel_id}/my-permissions".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetChannelMyPermissionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetChannelMyPermissionsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetChannelMyPermissionsResponse200]:
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
) -> Response[GetChannelMyPermissionsResponse200]:
    """Caller's resolved effective permissions on a channel

     Not gated on manage_roles — any member may see their own effective channel-scoped permission set
    (hub-wide baseline + ancestor-chain overwrite cascade). `is_admin` short-circuits every check.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChannelMyPermissionsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetChannelMyPermissionsResponse200 | None:
    """Caller's resolved effective permissions on a channel

     Not gated on manage_roles — any member may see their own effective channel-scoped permission set
    (hub-wide baseline + ancestor-chain overwrite cascade). `is_admin` short-circuits every check.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChannelMyPermissionsResponse200
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetChannelMyPermissionsResponse200]:
    """Caller's resolved effective permissions on a channel

     Not gated on manage_roles — any member may see their own effective channel-scoped permission set
    (hub-wide baseline + ancestor-chain overwrite cascade). `is_admin` short-circuits every check.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChannelMyPermissionsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetChannelMyPermissionsResponse200 | None:
    """Caller's resolved effective permissions on a channel

     Not gated on manage_roles — any member may see their own effective channel-scoped permission set
    (hub-wide baseline + ancestor-chain overwrite cascade). `is_admin` short-circuits every check.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChannelMyPermissionsResponse200
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
