from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_recovery_requests_to_attest_response_200_item import (
    ListRecoveryRequestsToAttestResponse200Item,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recovery/requests/to-attest",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListRecoveryRequestsToAttestResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListRecoveryRequestsToAttestResponse200Item.from_dict(
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
) -> Response[list[ListRecoveryRequestsToAttestResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[ListRecoveryRequestsToAttestResponse200Item]]:
    """Open rotation requests that name the caller as a recovery contact

     Pending requests whose old key designated the caller, directly or by master key, as a recovery
    contact, and which the caller has not attested yet. Advertised by the `recovery.attest.requests`
    capability; a `recovery_attestation_requested` WebSocket event (`request_id`) tells a connected
    contact when one opens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListRecoveryRequestsToAttestResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> list[ListRecoveryRequestsToAttestResponse200Item] | None:
    """Open rotation requests that name the caller as a recovery contact

     Pending requests whose old key designated the caller, directly or by master key, as a recovery
    contact, and which the caller has not attested yet. Advertised by the `recovery.attest.requests`
    capability; a `recovery_attestation_requested` WebSocket event (`request_id`) tells a connected
    contact when one opens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListRecoveryRequestsToAttestResponse200Item]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[ListRecoveryRequestsToAttestResponse200Item]]:
    """Open rotation requests that name the caller as a recovery contact

     Pending requests whose old key designated the caller, directly or by master key, as a recovery
    contact, and which the caller has not attested yet. Advertised by the `recovery.attest.requests`
    capability; a `recovery_attestation_requested` WebSocket event (`request_id`) tells a connected
    contact when one opens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListRecoveryRequestsToAttestResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> list[ListRecoveryRequestsToAttestResponse200Item] | None:
    """Open rotation requests that name the caller as a recovery contact

     Pending requests whose old key designated the caller, directly or by master key, as a recovery
    contact, and which the caller has not attested yet. Advertised by the `recovery.attest.requests`
    capability; a `recovery_attestation_requested` WebSocket event (`request_id`) tells a connected
    contact when one opens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListRecoveryRequestsToAttestResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
