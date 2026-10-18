from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verify_auth_body import VerifyAuthBody
from ...models.verify_auth_response_200 import VerifyAuthResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: VerifyAuthBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/verify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | VerifyAuthResponse200 | None:
    if response.status_code == 200:
        response_200 = VerifyAuthResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | VerifyAuthResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyAuthBody,
) -> Response[Any | VerifyAuthResponse200]:
    """Verify signature and obtain session token

     Submit the signed challenge to receive a Bearer token.

    **Signing:** hex-decode `challenge` to its 32 bytes. If
    `POST /auth/challenge` returned `scheme: "tagged-v1"`, sign
    `b"wavvon/auth-challenge/v1\\0" || challenge_bytes`; with no `scheme`,
    sign the raw 32 bytes (wire-format.md). Encode the 64-byte signature
    as lowercase hex. Send `challenge` back as the hex string you received.

    **PoW:** if the hub requires a security level > 0, compute:
    `SHA256(utf8(public_key_hex) || little_endian_u64(nonce))` and find a
    `nonce` (u64, starting from 1) whose hash has ≥ N leading zero bits.
    Submit that nonce as `security_nonce` and N as `security_level`.

    Args:
        body (VerifyAuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VerifyAuthResponse200]
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
    body: VerifyAuthBody,
) -> Any | VerifyAuthResponse200 | None:
    """Verify signature and obtain session token

     Submit the signed challenge to receive a Bearer token.

    **Signing:** hex-decode `challenge` to its 32 bytes. If
    `POST /auth/challenge` returned `scheme: "tagged-v1"`, sign
    `b"wavvon/auth-challenge/v1\\0" || challenge_bytes`; with no `scheme`,
    sign the raw 32 bytes (wire-format.md). Encode the 64-byte signature
    as lowercase hex. Send `challenge` back as the hex string you received.

    **PoW:** if the hub requires a security level > 0, compute:
    `SHA256(utf8(public_key_hex) || little_endian_u64(nonce))` and find a
    `nonce` (u64, starting from 1) whose hash has ≥ N leading zero bits.
    Submit that nonce as `security_nonce` and N as `security_level`.

    Args:
        body (VerifyAuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VerifyAuthResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyAuthBody,
) -> Response[Any | VerifyAuthResponse200]:
    """Verify signature and obtain session token

     Submit the signed challenge to receive a Bearer token.

    **Signing:** hex-decode `challenge` to its 32 bytes. If
    `POST /auth/challenge` returned `scheme: "tagged-v1"`, sign
    `b"wavvon/auth-challenge/v1\\0" || challenge_bytes`; with no `scheme`,
    sign the raw 32 bytes (wire-format.md). Encode the 64-byte signature
    as lowercase hex. Send `challenge` back as the hex string you received.

    **PoW:** if the hub requires a security level > 0, compute:
    `SHA256(utf8(public_key_hex) || little_endian_u64(nonce))` and find a
    `nonce` (u64, starting from 1) whose hash has ≥ N leading zero bits.
    Submit that nonce as `security_nonce` and N as `security_level`.

    Args:
        body (VerifyAuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VerifyAuthResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyAuthBody,
) -> Any | VerifyAuthResponse200 | None:
    """Verify signature and obtain session token

     Submit the signed challenge to receive a Bearer token.

    **Signing:** hex-decode `challenge` to its 32 bytes. If
    `POST /auth/challenge` returned `scheme: "tagged-v1"`, sign
    `b"wavvon/auth-challenge/v1\\0" || challenge_bytes`; with no `scheme`,
    sign the raw 32 bytes (wire-format.md). Encode the 64-byte signature
    as lowercase hex. Send `challenge` back as the hex string you received.

    **PoW:** if the hub requires a security level > 0, compute:
    `SHA256(utf8(public_key_hex) || little_endian_u64(nonce))` and find a
    `nonce` (u64, starting from 1) whose hash has ≥ N leading zero bits.
    Submit that nonce as `security_nonce` and N as `security_level`.

    Args:
        body (VerifyAuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VerifyAuthResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
