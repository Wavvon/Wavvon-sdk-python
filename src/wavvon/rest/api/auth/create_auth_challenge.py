from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_auth_challenge_body import CreateAuthChallengeBody
from ...models.create_auth_challenge_response_200 import CreateAuthChallengeResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAuthChallengeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/challenge",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAuthChallengeResponse200 | None:
    if response.status_code == 200:
        response_200 = CreateAuthChallengeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAuthChallengeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthChallengeBody,
) -> Response[CreateAuthChallengeResponse200]:
    """Request an auth challenge

     Returns a random 32-byte nonce, hex-encoded, valid for 60 seconds.
    The client signs it with its Ed25519 private key (see `scheme`) and
    submits it to `POST /auth/verify`.

    Args:
        body (CreateAuthChallengeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAuthChallengeResponse200]
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
    body: CreateAuthChallengeBody,
) -> CreateAuthChallengeResponse200 | None:
    """Request an auth challenge

     Returns a random 32-byte nonce, hex-encoded, valid for 60 seconds.
    The client signs it with its Ed25519 private key (see `scheme`) and
    submits it to `POST /auth/verify`.

    Args:
        body (CreateAuthChallengeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAuthChallengeResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthChallengeBody,
) -> Response[CreateAuthChallengeResponse200]:
    """Request an auth challenge

     Returns a random 32-byte nonce, hex-encoded, valid for 60 seconds.
    The client signs it with its Ed25519 private key (see `scheme`) and
    submits it to `POST /auth/verify`.

    Args:
        body (CreateAuthChallengeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAuthChallengeResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAuthChallengeBody,
) -> CreateAuthChallengeResponse200 | None:
    """Request an auth challenge

     Returns a random 32-byte nonce, hex-encoded, valid for 60 seconds.
    The client signs it with its Ed25519 private key (see `scheme`) and
    submits it to `POST /auth/verify`.

    Args:
        body (CreateAuthChallengeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAuthChallengeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
