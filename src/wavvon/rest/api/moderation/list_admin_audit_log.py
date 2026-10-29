from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_admin_audit_log_response_200_item import (
    ListAdminAuditLogResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_type: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["event_type"] = event_type

    params["actor"] = actor

    params["since"] = since

    params["until"] = until

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/audit-log",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAdminAuditLogResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAdminAuditLogResponse200Item.from_dict(
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
) -> Response[list[ListAdminAuditLogResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_type: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[list[ListAdminAuditLogResponse200Item]]:
    """Hub audit log, newest first (admin)

     Pages backwards: each page holds entries older than `cursor`. Apps that replay the log forwards use
    `GET /me/events`.

    Args:
        event_type (str | Unset):
        actor (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminAuditLogResponse200Item]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        actor=actor,
        since=since,
        until=until,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    event_type: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> list[ListAdminAuditLogResponse200Item] | None:
    """Hub audit log, newest first (admin)

     Pages backwards: each page holds entries older than `cursor`. Apps that replay the log forwards use
    `GET /me/events`.

    Args:
        event_type (str | Unset):
        actor (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminAuditLogResponse200Item]
    """

    return sync_detailed(
        client=client,
        event_type=event_type,
        actor=actor,
        since=since,
        until=until,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_type: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[list[ListAdminAuditLogResponse200Item]]:
    """Hub audit log, newest first (admin)

     Pages backwards: each page holds entries older than `cursor`. Apps that replay the log forwards use
    `GET /me/events`.

    Args:
        event_type (str | Unset):
        actor (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAdminAuditLogResponse200Item]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        actor=actor,
        since=since,
        until=until,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    event_type: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> list[ListAdminAuditLogResponse200Item] | None:
    """Hub audit log, newest first (admin)

     Pages backwards: each page holds entries older than `cursor`. Apps that replay the log forwards use
    `GET /me/events`.

    Args:
        event_type (str | Unset):
        actor (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAdminAuditLogResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            event_type=event_type,
            actor=actor,
            since=since,
            until=until,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
