from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_auth_device_token_body import CreateAuthDeviceTokenBody
from ...models.create_auth_device_token_response_200 import (
    CreateAuthDeviceTokenResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAuthDeviceTokenBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/device-token/create",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAuthDeviceTokenResponse200 | None:
    if response.status_code == 200:
        response_200 = CreateAuthDeviceTokenResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAuthDeviceTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthDeviceTokenBody | Unset = UNSET,
) -> Response[CreateAuthDeviceTokenResponse200]:
    """Mint a long-lived "trust this device" token

     Requires an existing session (e.g. right after a WebAuthn assertion).

    Args:
        body (CreateAuthDeviceTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAuthDeviceTokenResponse200]
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
    body: CreateAuthDeviceTokenBody | Unset = UNSET,
) -> CreateAuthDeviceTokenResponse200 | None:
    """Mint a long-lived "trust this device" token

     Requires an existing session (e.g. right after a WebAuthn assertion).

    Args:
        body (CreateAuthDeviceTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAuthDeviceTokenResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthDeviceTokenBody | Unset = UNSET,
) -> Response[CreateAuthDeviceTokenResponse200]:
    """Mint a long-lived "trust this device" token

     Requires an existing session (e.g. right after a WebAuthn assertion).

    Args:
        body (CreateAuthDeviceTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAuthDeviceTokenResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthDeviceTokenBody | Unset = UNSET,
) -> CreateAuthDeviceTokenResponse200 | None:
    """Mint a long-lived "trust this device" token

     Requires an existing session (e.g. right after a WebAuthn assertion).

    Args:
        body (CreateAuthDeviceTokenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAuthDeviceTokenResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
