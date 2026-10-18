from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_preview_response_200 import GetPreviewResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    url_query: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/preview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPreviewResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPreviewResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetPreviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
) -> Response[Any | GetPreviewResponse200]:
    """Fetch a link preview (title/description/image) for a URL

     Server-side fetch with SSRF protection (private/loopback/link-local targets rejected, DNS result
    pinned for the fetch). Responses are cached per URL. Rate-limited to 10 requests per 60 seconds per
    user; excess returns 429.

    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPreviewResponse200]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
) -> Any | GetPreviewResponse200 | None:
    """Fetch a link preview (title/description/image) for a URL

     Server-side fetch with SSRF protection (private/loopback/link-local targets rejected, DNS result
    pinned for the fetch). Responses are cached per URL. Rate-limited to 10 requests per 60 seconds per
    user; excess returns 429.

    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPreviewResponse200
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
) -> Response[Any | GetPreviewResponse200]:
    """Fetch a link preview (title/description/image) for a URL

     Server-side fetch with SSRF protection (private/loopback/link-local targets rejected, DNS result
    pinned for the fetch). Responses are cached per URL. Rate-limited to 10 requests per 60 seconds per
    user; excess returns 429.

    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPreviewResponse200]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
) -> Any | GetPreviewResponse200 | None:
    """Fetch a link preview (title/description/image) for a URL

     Server-side fetch with SSRF protection (private/loopback/link-local targets rejected, DNS result
    pinned for the fetch). Responses are cached per URL. Rate-limited to 10 requests per 60 seconds per
    user; excess returns 429.

    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPreviewResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
        )
    ).parsed
