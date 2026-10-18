from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invite_body import CreateInviteBody
from ...models.invite import Invite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateInviteBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/invites",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Invite | None:
    if response.status_code == 201:
        response_201 = Invite.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Invite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInviteBody | Unset = UNSET,
) -> Response[Invite]:
    """Create an invite (manage_invites)

     With `bound_pubkey` set the invite admits that identity and nobody else, and `max_uses` is forced to
    1 — a code that names its recipient and admits several people is a contradiction. On hubs
    advertising `invites.bound`; an older hub ignores the field and mints an ordinary bearer code, which
    is why a client must test for the string before offering it.

    Redeeming a bound invite also **satisfies the admission challenge**: an admin naming one key is the
    human act the challenge asks about, so a client with nobody watching its screen can join a hub that
    has `challenge_mode` on. A bearer invite buys no such exemption.

    Args:
        body (CreateInviteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invite]
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
    body: CreateInviteBody | Unset = UNSET,
) -> Invite | None:
    """Create an invite (manage_invites)

     With `bound_pubkey` set the invite admits that identity and nobody else, and `max_uses` is forced to
    1 — a code that names its recipient and admits several people is a contradiction. On hubs
    advertising `invites.bound`; an older hub ignores the field and mints an ordinary bearer code, which
    is why a client must test for the string before offering it.

    Redeeming a bound invite also **satisfies the admission challenge**: an admin naming one key is the
    human act the challenge asks about, so a client with nobody watching its screen can join a hub that
    has `challenge_mode` on. A bearer invite buys no such exemption.

    Args:
        body (CreateInviteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInviteBody | Unset = UNSET,
) -> Response[Invite]:
    """Create an invite (manage_invites)

     With `bound_pubkey` set the invite admits that identity and nobody else, and `max_uses` is forced to
    1 — a code that names its recipient and admits several people is a contradiction. On hubs
    advertising `invites.bound`; an older hub ignores the field and mints an ordinary bearer code, which
    is why a client must test for the string before offering it.

    Redeeming a bound invite also **satisfies the admission challenge**: an admin naming one key is the
    human act the challenge asks about, so a client with nobody watching its screen can join a hub that
    has `challenge_mode` on. A bearer invite buys no such exemption.

    Args:
        body (CreateInviteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInviteBody | Unset = UNSET,
) -> Invite | None:
    """Create an invite (manage_invites)

     With `bound_pubkey` set the invite admits that identity and nobody else, and `max_uses` is forced to
    1 — a code that names its recipient and admits several people is a contradiction. On hubs
    advertising `invites.bound`; an older hub ignores the field and mints an ordinary bearer code, which
    is why a client must test for the string before offering it.

    Redeeming a bound invite also **satisfies the admission challenge**: an admin naming one key is the
    human act the challenge asks about, so a client with nobody watching its screen can join a hub that
    has `challenge_mode` on. A bearer invite buys no such exemption.

    Args:
        body (CreateInviteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
