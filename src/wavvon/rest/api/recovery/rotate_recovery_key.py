from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rotate_recovery_key_body import RotateRecoveryKeyBody
from ...models.rotate_recovery_key_response_201 import RotateRecoveryKeyResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RotateRecoveryKeyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/recovery/rotate-key",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RotateRecoveryKeyResponse201 | None:
    if response.status_code == 201:
        response_201 = RotateRecoveryKeyResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RotateRecoveryKeyResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RotateRecoveryKeyBody | Unset = UNSET,
) -> Response[RotateRecoveryKeyResponse201]:
    """Open a key-rotation request with inline attestations

     Called by the NEW key — no Bearer token required. Attestations from configured recovery contacts are
    validated; once the count reaches the owner's threshold the request flips to `ready_for_review` for
    admin action.

    Args:
        body (RotateRecoveryKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateRecoveryKeyResponse201]
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
    body: RotateRecoveryKeyBody | Unset = UNSET,
) -> RotateRecoveryKeyResponse201 | None:
    """Open a key-rotation request with inline attestations

     Called by the NEW key — no Bearer token required. Attestations from configured recovery contacts are
    validated; once the count reaches the owner's threshold the request flips to `ready_for_review` for
    admin action.

    Args:
        body (RotateRecoveryKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateRecoveryKeyResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RotateRecoveryKeyBody | Unset = UNSET,
) -> Response[RotateRecoveryKeyResponse201]:
    """Open a key-rotation request with inline attestations

     Called by the NEW key — no Bearer token required. Attestations from configured recovery contacts are
    validated; once the count reaches the owner's threshold the request flips to `ready_for_review` for
    admin action.

    Args:
        body (RotateRecoveryKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateRecoveryKeyResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RotateRecoveryKeyBody | Unset = UNSET,
) -> RotateRecoveryKeyResponse201 | None:
    """Open a key-rotation request with inline attestations

     Called by the NEW key — no Bearer token required. Attestations from configured recovery contacts are
    validated; once the count reaches the owner's threshold the request flips to `ready_for_review` for
    admin action.

    Args:
        body (RotateRecoveryKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateRecoveryKeyResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
