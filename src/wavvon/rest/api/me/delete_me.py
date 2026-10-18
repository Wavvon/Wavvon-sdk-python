from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/me",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Leave this hub

     Removes the caller from the hub: profile fields cleared, every role
    deleted, sessions ended. The `users` row itself is **kept** as a bare
    pubkey — moderation records and message authorship reference it, so a
    departure must not take a ban or a report with it. Messages,
    reactions and RSVPs are untouched; the author becomes a pubkey with
    no name.

    Self only. Removing someone else is `/moderation`.

    Note that membership *is* the roles, and the invite gate is "has no
    roles", so on an `invite_only` hub this makes the return that is
    otherwise free require a fresh invite. Clients say so before asking.

    Advertised as the `hub.leave` capability; a hub without it answers 404
    and the client must not offer the action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Leave this hub

     Removes the caller from the hub: profile fields cleared, every role
    deleted, sessions ended. The `users` row itself is **kept** as a bare
    pubkey — moderation records and message authorship reference it, so a
    departure must not take a ban or a report with it. Messages,
    reactions and RSVPs are untouched; the author becomes a pubkey with
    no name.

    Self only. Removing someone else is `/moderation`.

    Note that membership *is* the roles, and the invite gate is "has no
    roles", so on an `invite_only` hub this makes the return that is
    otherwise free require a fresh invite. Clients say so before asking.

    Advertised as the `hub.leave` capability; a hub without it answers 404
    and the client must not offer the action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
