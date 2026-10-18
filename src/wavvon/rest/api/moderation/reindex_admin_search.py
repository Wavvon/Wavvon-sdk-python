from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reindex_admin_search_response_202 import ReindexAdminSearchResponse202
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/search/reindex",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ReindexAdminSearchResponse202 | None:
    if response.status_code == 202:
        response_202 = ReindexAdminSearchResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ReindexAdminSearchResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ReindexAdminSearchResponse202]:
    """Rebuild the full-text search index from the messages table (admin)

     Starts an asynchronous reindex and returns immediately. A second call while a reindex is running
    returns `{"status":"already_running"}` instead of starting a duplicate job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReindexAdminSearchResponse202]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ReindexAdminSearchResponse202 | None:
    """Rebuild the full-text search index from the messages table (admin)

     Starts an asynchronous reindex and returns immediately. A second call while a reindex is running
    returns `{"status":"already_running"}` instead of starting a duplicate job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReindexAdminSearchResponse202
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ReindexAdminSearchResponse202]:
    """Rebuild the full-text search index from the messages table (admin)

     Starts an asynchronous reindex and returns immediately. A second call while a reindex is running
    returns `{"status":"already_running"}` instead of starting a duplicate job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReindexAdminSearchResponse202]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ReindexAdminSearchResponse202 | None:
    """Rebuild the full-text search index from the messages table (admin)

     Starts an asynchronous reindex and returns immediately. A second call while a reindex is running
    returns `{"status":"already_running"}` instead of starting a duplicate job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReindexAdminSearchResponse202
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
