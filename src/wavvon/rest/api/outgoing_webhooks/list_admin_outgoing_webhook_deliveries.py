from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_admin_outgoing_webhook_deliveries_response_200_item import (
    ListAdminOutgoingWebhookDeliveriesResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: str | Unset = UNSET,
    success: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["event_type"] = event_type

    params["success"] = success

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/outgoing-webhooks/{id}/deliveries".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAdminOutgoingWebhookDeliveriesResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                ListAdminOutgoingWebhookDeliveriesResponse200Item.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListAdminOutgoingWebhookDeliveriesResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: str | Unset = UNSET,
    success: bool | Unset = UNSET,
) -> Response[list[ListAdminOutgoingWebhookDeliveriesResponse200Item]]:
    """List recent delivery attempts for an outgoing webhook (admin)

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (str | Unset):
        success (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminOutgoingWebhookDeliveriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        event_type=event_type,
        success=success,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: str | Unset = UNSET,
    success: bool | Unset = UNSET,
) -> list[ListAdminOutgoingWebhookDeliveriesResponse200Item] | None:
    """List recent delivery attempts for an outgoing webhook (admin)

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (str | Unset):
        success (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminOutgoingWebhookDeliveriesResponse200Item]
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        offset=offset,
        event_type=event_type,
        success=success,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: str | Unset = UNSET,
    success: bool | Unset = UNSET,
) -> Response[list[ListAdminOutgoingWebhookDeliveriesResponse200Item]]:
    """List recent delivery attempts for an outgoing webhook (admin)

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (str | Unset):
        success (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminOutgoingWebhookDeliveriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        event_type=event_type,
        success=success,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: str | Unset = UNSET,
    success: bool | Unset = UNSET,
) -> list[ListAdminOutgoingWebhookDeliveriesResponse200Item] | None:
    """List recent delivery attempts for an outgoing webhook (admin)

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (str | Unset):
        success (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminOutgoingWebhookDeliveriesResponse200Item]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            offset=offset,
            event_type=event_type,
            success=success,
        )
    ).parsed
