from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.begin_webauthn_registration_body import BeginWebauthnRegistrationBody
from ...models.begin_webauthn_registration_response_200 import (
    BeginWebauthnRegistrationResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BeginWebauthnRegistrationBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/webauthn/begin",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BeginWebauthnRegistrationResponse200 | None:
    if response.status_code == 200:
        response_200 = BeginWebauthnRegistrationResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BeginWebauthnRegistrationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BeginWebauthnRegistrationBody | Unset = UNSET,
) -> Response[BeginWebauthnRegistrationResponse200]:
    """Start WebAuthn passkey registration

     Excludes credentials the user already has so re-registering the same authenticator is blocked.

    Args:
        body (BeginWebauthnRegistrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BeginWebauthnRegistrationResponse200]
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
    body: BeginWebauthnRegistrationBody | Unset = UNSET,
) -> BeginWebauthnRegistrationResponse200 | None:
    """Start WebAuthn passkey registration

     Excludes credentials the user already has so re-registering the same authenticator is blocked.

    Args:
        body (BeginWebauthnRegistrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BeginWebauthnRegistrationResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BeginWebauthnRegistrationBody | Unset = UNSET,
) -> Response[BeginWebauthnRegistrationResponse200]:
    """Start WebAuthn passkey registration

     Excludes credentials the user already has so re-registering the same authenticator is blocked.

    Args:
        body (BeginWebauthnRegistrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BeginWebauthnRegistrationResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BeginWebauthnRegistrationBody | Unset = UNSET,
) -> BeginWebauthnRegistrationResponse200 | None:
    """Start WebAuthn passkey registration

     Excludes credentials the user already has so re-registering the same authenticator is blocked.

    Args:
        body (BeginWebauthnRegistrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BeginWebauthnRegistrationResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
