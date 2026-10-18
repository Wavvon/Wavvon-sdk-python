from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_profile_response_200 import GetUserProfileResponse200
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{pubkey}/profile".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUserProfileResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUserProfileResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUserProfileResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetUserProfileResponse200]:
    """Get a user's hub profile (roles + badges)

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserProfileResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetUserProfileResponse200 | None:
    """Get a user's hub profile (roles + badges)

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserProfileResponse200
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetUserProfileResponse200]:
    """Get a user's hub profile (roles + badges)

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserProfileResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetUserProfileResponse200 | None:
    """Get a user's hub profile (roles + badges)

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserProfileResponse200
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
