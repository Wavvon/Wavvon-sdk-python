from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.explain_user_permissions_response_200 import (
    ExplainUserPermissionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pubkey: str,
    *,
    permission: str,
    channel_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["permission"] = permission

    params["channel_id"] = channel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{pubkey}/permissions/why".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ExplainUserPermissionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ExplainUserPermissionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ExplainUserPermissionsResponse200]:
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
    permission: str,
    channel_id: str | Unset = UNSET,
) -> Response[Any | ExplainUserPermissionsResponse200]:
    """Why this member can (or cannot) do X here

     Answers *role Moderators, allowed on #general*. Two axes are debuggable by reading and not by
    guessing, and every operator question about permissions is this one. Reading your own answer is
    always allowed; reading someone else's needs `members.read`.

    `sources` is every row bearing on the answer, in the order the resolver folds them: the hub-wide
    baseline first, then the channel's ancestor chain root to target. An owner's answer carries
    `is_owner` and no sources, because no role explains it.

    Args:
        pubkey (str):
        permission (str):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExplainUserPermissionsResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        permission=permission,
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    permission: str,
    channel_id: str | Unset = UNSET,
) -> Any | ExplainUserPermissionsResponse200 | None:
    """Why this member can (or cannot) do X here

     Answers *role Moderators, allowed on #general*. Two axes are debuggable by reading and not by
    guessing, and every operator question about permissions is this one. Reading your own answer is
    always allowed; reading someone else's needs `members.read`.

    `sources` is every row bearing on the answer, in the order the resolver folds them: the hub-wide
    baseline first, then the channel's ancestor chain root to target. An owner's answer carries
    `is_owner` and no sources, because no role explains it.

    Args:
        pubkey (str):
        permission (str):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExplainUserPermissionsResponse200
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
        permission=permission,
        channel_id=channel_id,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    permission: str,
    channel_id: str | Unset = UNSET,
) -> Response[Any | ExplainUserPermissionsResponse200]:
    """Why this member can (or cannot) do X here

     Answers *role Moderators, allowed on #general*. Two axes are debuggable by reading and not by
    guessing, and every operator question about permissions is this one. Reading your own answer is
    always allowed; reading someone else's needs `members.read`.

    `sources` is every row bearing on the answer, in the order the resolver folds them: the hub-wide
    baseline first, then the channel's ancestor chain root to target. An owner's answer carries
    `is_owner` and no sources, because no role explains it.

    Args:
        pubkey (str):
        permission (str):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExplainUserPermissionsResponse200]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        permission=permission,
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    permission: str,
    channel_id: str | Unset = UNSET,
) -> Any | ExplainUserPermissionsResponse200 | None:
    """Why this member can (or cannot) do X here

     Answers *role Moderators, allowed on #general*. Two axes are debuggable by reading and not by
    guessing, and every operator question about permissions is this one. Reading your own answer is
    always allowed; reading someone else's needs `members.read`.

    `sources` is every row bearing on the answer, in the order the resolver folds them: the hub-wide
    baseline first, then the channel's ancestor chain root to target. An owner's answer carries
    `is_owner` and no sources, because no role explains it.

    Args:
        pubkey (str):
        permission (str):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExplainUserPermissionsResponse200
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
            permission=permission,
            channel_id=channel_id,
        )
    ).parsed
