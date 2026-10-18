from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.signed_member_change import SignedMemberChange
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: str,
    pubkey: str,
    *,
    body: SignedMemberChange | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/conversations/{conversation_id}/members/{pubkey}".format(
            conversation_id=quote(str(conversation_id), safe=""),
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
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
    conversation_id: str,
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignedMemberChange | Unset = UNSET,
) -> Response[Any]:
    """Leave a group conversation (callers may only remove themselves)

    Args:
        conversation_id (str):
        pubkey (str):
        body (SignedMemberChange | Unset): The actor's signature over a group add or leave (wire-
            format.md, "Group DM member change"). Without it the change holds on this hub only; with
            it the hub carries the change to the other members' hubs. Only on a hub advertising
            `dms.group.signedmembers`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        pubkey=pubkey,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    conversation_id: str,
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignedMemberChange | Unset = UNSET,
) -> Response[Any]:
    """Leave a group conversation (callers may only remove themselves)

    Args:
        conversation_id (str):
        pubkey (str):
        body (SignedMemberChange | Unset): The actor's signature over a group add or leave (wire-
            format.md, "Group DM member change"). Without it the change holds on this hub only; with
            it the hub carries the change to the other members' hubs. Only on a hub advertising
            `dms.group.signedmembers`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        pubkey=pubkey,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
