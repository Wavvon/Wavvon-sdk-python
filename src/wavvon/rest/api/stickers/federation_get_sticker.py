from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    sha256: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/federation/stickers/{sha256}".format(
            sha256=quote(str(sha256), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 429:
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
    sha256: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Another hub fetching a sticker this hub published

     Serves only this hub's own pack stickers that are not removed, never a copy. Unauthenticated (the
    bytes are public already and any key can claim to be a hub) and rate-limited per address. 403 when
    the hub setting `stickers_export` is off, 404 for anything else.

    Args:
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    sha256: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Another hub fetching a sticker this hub published

     Serves only this hub's own pack stickers that are not removed, never a copy. Unauthenticated (the
    bytes are public already and any key can claim to be a hub) and rate-limited per address. 403 when
    the hub setting `stickers_export` is off, 404 for anything else.

    Args:
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
