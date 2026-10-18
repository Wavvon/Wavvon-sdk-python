from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_permissions_response_200 import ListPermissionsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/permissions",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListPermissionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListPermissionsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListPermissionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListPermissionsResponse200]:
    """The permission catalogue this hub can express

     Every permission id with its scope, so clients render the roles and channel-overwrite screens from
    the server that enforces them rather than from their own copy. Readable by any member: it is what
    the hub can express, not what the caller holds.

    Gated by the `permissions.catalogue` capability — a hub without it uses the older snake_case ids,
    which share no spelling with these.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPermissionsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ListPermissionsResponse200 | None:
    """The permission catalogue this hub can express

     Every permission id with its scope, so clients render the roles and channel-overwrite screens from
    the server that enforces them rather than from their own copy. Readable by any member: it is what
    the hub can express, not what the caller holds.

    Gated by the `permissions.catalogue` capability — a hub without it uses the older snake_case ids,
    which share no spelling with these.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPermissionsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListPermissionsResponse200]:
    """The permission catalogue this hub can express

     Every permission id with its scope, so clients render the roles and channel-overwrite screens from
    the server that enforces them rather than from their own copy. Readable by any member: it is what
    the hub can express, not what the caller holds.

    Gated by the `permissions.catalogue` capability — a hub without it uses the older snake_case ids,
    which share no spelling with these.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPermissionsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ListPermissionsResponse200 | None:
    """The permission catalogue this hub can express

     Every permission id with its scope, so clients render the roles and channel-overwrite screens from
    the server that enforces them rather than from their own copy. Readable by any member: it is what
    the hub can express, not what the caller holds.

    Gated by the `permissions.catalogue` capability — a hub without it uses the older snake_case ids,
    which share no spelling with these.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPermissionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
