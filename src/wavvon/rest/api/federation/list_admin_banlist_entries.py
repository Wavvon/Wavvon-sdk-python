from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_admin_banlist_entries_response_200_item import (
    ListAdminBanlistEntriesResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["source"] = source

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/banlist/entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAdminBanlistEntriesResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAdminBanlistEntriesResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListAdminBanlistEntriesResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[ListAdminBanlistEntriesResponse200Item]]:
    """List synced federated ban entries (admin)

    Args:
        source (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminBanlistEntriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        source=source,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    source: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[ListAdminBanlistEntriesResponse200Item] | None:
    """List synced federated ban entries (admin)

    Args:
        source (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminBanlistEntriesResponse200Item]
    """

    return sync_detailed(
        client=client,
        source=source,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[ListAdminBanlistEntriesResponse200Item]]:
    """List synced federated ban entries (admin)

    Args:
        source (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminBanlistEntriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        source=source,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    source: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[ListAdminBanlistEntriesResponse200Item] | None:
    """List synced federated ban entries (admin)

    Args:
        source (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminBanlistEntriesResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            source=source,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
