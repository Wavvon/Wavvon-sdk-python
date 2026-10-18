from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_admin_banlist_source_body import CreateAdminBanlistSourceBody
from ...models.create_admin_banlist_source_response_201 import (
    CreateAdminBanlistSourceResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAdminBanlistSourceBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/banlist/sources",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAdminBanlistSourceResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateAdminBanlistSourceResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAdminBanlistSourceResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminBanlistSourceBody | Unset = UNSET,
) -> Response[CreateAdminBanlistSourceResponse201]:
    """Add a ban list source and trigger an immediate sync (admin)

    Args:
        body (CreateAdminBanlistSourceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAdminBanlistSourceResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminBanlistSourceBody | Unset = UNSET,
) -> CreateAdminBanlistSourceResponse201 | None:
    """Add a ban list source and trigger an immediate sync (admin)

    Args:
        body (CreateAdminBanlistSourceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAdminBanlistSourceResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminBanlistSourceBody | Unset = UNSET,
) -> Response[CreateAdminBanlistSourceResponse201]:
    """Add a ban list source and trigger an immediate sync (admin)

    Args:
        body (CreateAdminBanlistSourceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAdminBanlistSourceResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminBanlistSourceBody | Unset = UNSET,
) -> CreateAdminBanlistSourceResponse201 | None:
    """Add a ban list source and trigger an immediate sync (admin)

    Args:
        body (CreateAdminBanlistSourceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAdminBanlistSourceResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
