from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certification import Certification
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/identity/{pubkey}/certs".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Certification] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Certification.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Certification]]:
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
) -> Response[list[Certification]]:
    """List valid certs for a user (public)

     Returns non-revoked, non-expired certs this hub issued for the user plus cross-hub certs deposited
    into the user's portfolio. Used by receiving hubs to pull certs directly from the issuer.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Certification]]
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
) -> list[Certification] | None:
    """List valid certs for a user (public)

     Returns non-revoked, non-expired certs this hub issued for the user plus cross-hub certs deposited
    into the user's portfolio. Used by receiving hubs to pull certs directly from the issuer.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Certification]
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Certification]]:
    """List valid certs for a user (public)

     Returns non-revoked, non-expired certs this hub issued for the user plus cross-hub certs deposited
    into the user's portfolio. Used by receiving hubs to pull certs directly from the issuer.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Certification]]
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
) -> list[Certification] | None:
    """List valid certs for a user (public)

     Returns non-revoked, non-expired certs this hub issued for the user plus cross-hub certs deposited
    into the user's portfolio. Used by receiving hubs to pull certs directly from the issuer.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Certification]
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
