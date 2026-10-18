from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_info import UserInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 200,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[UserInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[UserInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 200,
    cursor: str | Unset = UNSET,
) -> Response[list[UserInfo]]:
    """List hub members (paginated)

     Members the hub knows, ordered by display name then public key. Page with `cursor` — pass the
    `public_key` of the last row of the previous page — until a short page comes back. Before 2026-08-08
    this capped at a hardcoded 50 rows with no way to reach row 51.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 200.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[UserInfo]]
    """

    kwargs = _get_kwargs(
        q=q,
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
    q: str | Unset = UNSET,
    limit: int | Unset = 200,
    cursor: str | Unset = UNSET,
) -> list[UserInfo] | None:
    """List hub members (paginated)

     Members the hub knows, ordered by display name then public key. Page with `cursor` — pass the
    `public_key` of the last row of the previous page — until a short page comes back. Before 2026-08-08
    this capped at a hardcoded 50 rows with no way to reach row 51.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 200.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[UserInfo]
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 200,
    cursor: str | Unset = UNSET,
) -> Response[list[UserInfo]]:
    """List hub members (paginated)

     Members the hub knows, ordered by display name then public key. Page with `cursor` — pass the
    `public_key` of the last row of the previous page — until a short page comes back. Before 2026-08-08
    this capped at a hardcoded 50 rows with no way to reach row 51.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 200.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[UserInfo]]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 200,
    cursor: str | Unset = UNSET,
) -> list[UserInfo] | None:
    """List hub members (paginated)

     Members the hub knows, ordered by display name then public key. Page with `cursor` — pass the
    `public_key` of the last row of the previous page — until a short page comes back. Before 2026-08-08
    this capped at a hardcoded 50 rows with no way to reach row 51.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 200.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[UserInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
