from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invite import Invite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_inactive: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/invites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Invite] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Invite.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Invite]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[Invite]]:
    """List active invites (manage_invites)

     Newest first, and only the invites that can still admit someone — an expired or used-up one is
    returned only with `include_inactive=true`. Paged only on hubs advertising `list.cursor.lists`.

    Args:
        include_inactive (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Invite]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
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
    include_inactive: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[Invite] | None:
    """List active invites (manage_invites)

     Newest first, and only the invites that can still admit someone — an expired or used-up one is
    returned only with `include_inactive=true`. Paged only on hubs advertising `list.cursor.lists`.

    Args:
        include_inactive (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Invite]
    """

    return sync_detailed(
        client=client,
        include_inactive=include_inactive,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> Response[list[Invite]]:
    """List active invites (manage_invites)

     Newest first, and only the invites that can still admit someone — an expired or used-up one is
    returned only with `include_inactive=true`. Paged only on hubs advertising `list.cursor.lists`.

    Args:
        include_inactive (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Invite]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = False,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,
) -> list[Invite] | None:
    """List active invites (manage_invites)

     Newest first, and only the invites that can still admit someone — an expired or used-up one is
    returned only with `include_inactive=true`. Paged only on hubs advertising `list.cursor.lists`.

    Args:
        include_inactive (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Invite]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_inactive=include_inactive,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
