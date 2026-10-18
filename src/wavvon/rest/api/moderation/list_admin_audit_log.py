from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_admin_audit_log_response_200 import ListAdminAuditLogResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_type: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["event_type"] = event_type

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
) -> ListAdminAuditLogResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAdminAuditLogResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListAdminAuditLogResponse200]:
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
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ListAdminAuditLogResponse200]:
    """Cursor-paginated hub audit log (admin)

    Args:
        event_type (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAdminAuditLogResponse200]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
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
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> ListAdminAuditLogResponse200 | None:
    """Cursor-paginated hub audit log (admin)

    Args:
        event_type (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAdminAuditLogResponse200
    """

    return sync_detailed(
        client=client,
        event_type=event_type,
        since=since,
        until=until,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_type: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ListAdminAuditLogResponse200]:
    """Cursor-paginated hub audit log (admin)

    Args:
        event_type (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAdminAuditLogResponse200]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
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
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 50,
) -> ListAdminAuditLogResponse200 | None:
    """Cursor-paginated hub audit log (admin)

    Args:
        event_type (str | Unset):
        since (int | Unset):
        until (int | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAdminAuditLogResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            event_type=event_type,
            since=since,
            until=until,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
