from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_federation_dm_member_change_body import (
    CreateFederationDmMemberChangeBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFederationDmMemberChangeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/federation/dm-member-change",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
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
    body: CreateFederationDmMemberChangeBody,
) -> Response[Any]:
    """Receive a signed group membership change from a peer hub

     The actor's signature over `wavvon/dm-member-change/v1` (see wire-format.md). Applied only for a
    group this hub holds, from an actor already on its roster, removing nobody but the actor, and only
    when newer than the last change applied for that member; an older one answers 200 and changes
    nothing. A conversation this hub has never seen also answers 200: its first DM brings the current
    roster.

    Args:
        body (CreateFederationDmMemberChangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFederationDmMemberChangeBody,
) -> Response[Any]:
    """Receive a signed group membership change from a peer hub

     The actor's signature over `wavvon/dm-member-change/v1` (see wire-format.md). Applied only for a
    group this hub holds, from an actor already on its roster, removing nobody but the actor, and only
    when newer than the last change applied for that member; an older one answers 200 and changes
    nothing. A conversation this hub has never seen also answers 200: its first DM brings the current
    roster.

    Args:
        body (CreateFederationDmMemberChangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
