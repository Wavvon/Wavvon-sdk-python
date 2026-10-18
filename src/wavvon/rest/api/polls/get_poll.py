from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_poll_response_200 import GetPollResponse200
from ...types import Response


def _get_kwargs(
    poll_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/polls/{poll_id}".format(
            poll_id=quote(str(poll_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPollResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPollResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPollResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    poll_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPollResponse200]:
    """Get a poll with vote totals and the caller's vote

    Args:
        poll_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPollResponse200]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    poll_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPollResponse200 | None:
    """Get a poll with vote totals and the caller's vote

    Args:
        poll_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPollResponse200
    """

    return sync_detailed(
        poll_id=poll_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    poll_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPollResponse200]:
    """Get a poll with vote totals and the caller's vote

    Args:
        poll_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPollResponse200]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    poll_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPollResponse200 | None:
    """Get a poll with vote totals and the caller's vote

    Args:
        poll_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPollResponse200
    """

    return (
        await asyncio_detailed(
            poll_id=poll_id,
            client=client,
        )
    ).parsed
