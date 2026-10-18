from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attest_recovery_rotation_request_body import (
    AttestRecoveryRotationRequestBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: AttestRecoveryRotationRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/recovery/rotation-request/{id}/attest".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 409:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttestRecoveryRotationRequestBody,
) -> Response[Any]:
    """A recovery contact vouches for an open rotation request

     The signature is over the canonical `wavvon/recovery-attestation/v1` bundle bytes. Signed with the
    **roster** identity key the hub knows the contact by, never a derived multi-device master key.
    Deduped per contact; reaching the owner's threshold flips the request from `pending` to
    `ready_for_review` for admin action.

    Args:
        id (str):
        body (AttestRecoveryRotationRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttestRecoveryRotationRequestBody,
) -> Response[Any]:
    """A recovery contact vouches for an open rotation request

     The signature is over the canonical `wavvon/recovery-attestation/v1` bundle bytes. Signed with the
    **roster** identity key the hub knows the contact by, never a derived multi-device master key.
    Deduped per contact; reaching the owner's threshold flips the request from `pending` to
    `ready_for_review` for admin action.

    Args:
        id (str):
        body (AttestRecoveryRotationRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
