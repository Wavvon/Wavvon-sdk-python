from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_moderation_history_response_200 import (
    GetModerationHistoryResponse200,
)
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/moderation/history/{pubkey}".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetModerationHistoryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetModerationHistoryResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetModerationHistoryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetModerationHistoryResponse200]:
    """What other hubs have said about this member

     Entries from subscribed federated ban lists that name this member, soft-flag ones included — those
    do not block admission and exist to be read. Resolved against the member master pubkey where they
    have one, matching admission, so a paired device does not show a clean record. Requires ban_members.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetModerationHistoryResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetModerationHistoryResponse200 | None:
    """What other hubs have said about this member

     Entries from subscribed federated ban lists that name this member, soft-flag ones included — those
    do not block admission and exist to be read. Resolved against the member master pubkey where they
    have one, matching admission, so a paired device does not show a clean record. Requires ban_members.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetModerationHistoryResponse200
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetModerationHistoryResponse200]:
    """What other hubs have said about this member

     Entries from subscribed federated ban lists that name this member, soft-flag ones included — those
    do not block admission and exist to be read. Resolved against the member master pubkey where they
    have one, matching admission, so a paired device does not show a clean record. Requires ban_members.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetModerationHistoryResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetModerationHistoryResponse200 | None:
    """What other hubs have said about this member

     Entries from subscribed federated ban lists that name this member, soft-flag ones included — those
    do not block admission and exist to be read. Resolved against the member master pubkey where they
    have one, matching admission, so a paired device does not show a clean record. Requires ban_members.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetModerationHistoryResponse200
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
