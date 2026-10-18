from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_recovery_rotation_request_response_200 import (
    GetRecoveryRotationRequestResponse200,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recovery/rotation-request/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRecoveryRotationRequestResponse200 | None:
    if response.status_code == 200:
        response_200 = GetRecoveryRotationRequestResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRecoveryRotationRequestResponse200]:
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
) -> Response[GetRecoveryRotationRequestResponse200]:
    """The bundle a recovery contact signs, plus progress

     No session required: a contact learns the request id out of band and may not hold an account on this
    hub at all. See recovery-attestation.md §2.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecoveryRotationRequestResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetRecoveryRotationRequestResponse200 | None:
    """The bundle a recovery contact signs, plus progress

     No session required: a contact learns the request id out of band and may not hold an account on this
    hub at all. See recovery-attestation.md §2.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecoveryRotationRequestResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetRecoveryRotationRequestResponse200]:
    """The bundle a recovery contact signs, plus progress

     No session required: a contact learns the request id out of band and may not hold an account on this
    hub at all. See recovery-attestation.md §2.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecoveryRotationRequestResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetRecoveryRotationRequestResponse200 | None:
    """The bundle a recovery contact signs, plus progress

     No session required: a contact learns the request id out of band and may not hold an account on this
    hub at all. See recovery-attestation.md §2.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecoveryRotationRequestResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
