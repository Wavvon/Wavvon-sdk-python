from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_admin_reports_response_200_item import (
    ListAdminReportsResponse200Item,
)
from ...models.list_admin_reports_status import ListAdminReportsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListAdminReportsStatus | Unset = ListAdminReportsStatus.PENDING,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAdminReportsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAdminReportsResponse200Item.from_dict(
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
) -> Response[list[ListAdminReportsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListAdminReportsStatus | Unset = ListAdminReportsStatus.PENDING,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[list[ListAdminReportsResponse200Item]]:
    """List message reports (admin)

    Args:
        status (ListAdminReportsStatus | Unset):  Default: ListAdminReportsStatus.PENDING.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminReportsResponse200Item]]
    """

    kwargs = _get_kwargs(
        status=status,
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
    status: ListAdminReportsStatus | Unset = ListAdminReportsStatus.PENDING,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> list[ListAdminReportsResponse200Item] | None:
    """List message reports (admin)

    Args:
        status (ListAdminReportsStatus | Unset):  Default: ListAdminReportsStatus.PENDING.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminReportsResponse200Item]
    """

    return sync_detailed(
        client=client,
        status=status,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListAdminReportsStatus | Unset = ListAdminReportsStatus.PENDING,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[list[ListAdminReportsResponse200Item]]:
    """List message reports (admin)

    Args:
        status (ListAdminReportsStatus | Unset):  Default: ListAdminReportsStatus.PENDING.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminReportsResponse200Item]]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: ListAdminReportsStatus | Unset = ListAdminReportsStatus.PENDING,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> list[ListAdminReportsResponse200Item] | None:
    """List message reports (admin)

    Args:
        status (ListAdminReportsStatus | Unset):  Default: ListAdminReportsStatus.PENDING.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminReportsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
