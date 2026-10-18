from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alliance_people_response_200_item import (
    ListAlliancePeopleResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alliance_id: str,
    *,
    hub: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hub"] = hub

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alliances/{alliance_id}/people".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ListAlliancePeopleResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAlliancePeopleResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[ListAlliancePeopleResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    hub: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | list[ListAlliancePeopleResponse200Item]]:
    """Browse the opted-in members of one allied hub

     Alliance member discovery. Read-through: the owning hub answers from its
    own members and nothing is copied. `hub` names the hub to ask (absent
    or this hub's own key = answer locally).

    - **Caller is a member of this hub** and `hub` is an allied hub: this
      hub proxies the request to it. The viewer is deliberately not
      forwarded.
    - **Caller is a peer hub** (or a member asking about this hub): answers
      from `users`. A peer must belong to this alliance and may only ask
      about this hub — never a third.

    A person is listed only when the alliance's `people_visible` switch is
    on, the member set `findable_by_allies`, they are not banned, and the
    hub holds their home-hub designation (so a DM to them can be routed).
    Entries carry only the four fields below; non-opted members are not
    counted or hinted at.

    Paging is the server dialect: a bare array, `limit` (default 100, max
    500) and a keyset `cursor` (the `public_key` of the last entry) over
    `(display_name, public_key)`. `q` matches display name, capped at 64
    characters. Rate limited per caller (60 per minute).

    Advertised as the `alliance.people` capability.

    Args:
        alliance_id (str):
        hub (str | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListAlliancePeopleResponse200Item]]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        hub=hub,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    hub: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | list[ListAlliancePeopleResponse200Item] | None:
    """Browse the opted-in members of one allied hub

     Alliance member discovery. Read-through: the owning hub answers from its
    own members and nothing is copied. `hub` names the hub to ask (absent
    or this hub's own key = answer locally).

    - **Caller is a member of this hub** and `hub` is an allied hub: this
      hub proxies the request to it. The viewer is deliberately not
      forwarded.
    - **Caller is a peer hub** (or a member asking about this hub): answers
      from `users`. A peer must belong to this alliance and may only ask
      about this hub — never a third.

    A person is listed only when the alliance's `people_visible` switch is
    on, the member set `findable_by_allies`, they are not banned, and the
    hub holds their home-hub designation (so a DM to them can be routed).
    Entries carry only the four fields below; non-opted members are not
    counted or hinted at.

    Paging is the server dialect: a bare array, `limit` (default 100, max
    500) and a keyset `cursor` (the `public_key` of the last entry) over
    `(display_name, public_key)`. `q` matches display name, capped at 64
    characters. Rate limited per caller (60 per minute).

    Advertised as the `alliance.people` capability.

    Args:
        alliance_id (str):
        hub (str | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListAlliancePeopleResponse200Item]
    """

    return sync_detailed(
        alliance_id=alliance_id,
        client=client,
        hub=hub,
        q=q,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    hub: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | list[ListAlliancePeopleResponse200Item]]:
    """Browse the opted-in members of one allied hub

     Alliance member discovery. Read-through: the owning hub answers from its
    own members and nothing is copied. `hub` names the hub to ask (absent
    or this hub's own key = answer locally).

    - **Caller is a member of this hub** and `hub` is an allied hub: this
      hub proxies the request to it. The viewer is deliberately not
      forwarded.
    - **Caller is a peer hub** (or a member asking about this hub): answers
      from `users`. A peer must belong to this alliance and may only ask
      about this hub — never a third.

    A person is listed only when the alliance's `people_visible` switch is
    on, the member set `findable_by_allies`, they are not banned, and the
    hub holds their home-hub designation (so a DM to them can be routed).
    Entries carry only the four fields below; non-opted members are not
    counted or hinted at.

    Paging is the server dialect: a bare array, `limit` (default 100, max
    500) and a keyset `cursor` (the `public_key` of the last entry) over
    `(display_name, public_key)`. `q` matches display name, capped at 64
    characters. Rate limited per caller (60 per minute).

    Advertised as the `alliance.people` capability.

    Args:
        alliance_id (str):
        hub (str | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListAlliancePeopleResponse200Item]]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        hub=hub,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    hub: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | list[ListAlliancePeopleResponse200Item] | None:
    """Browse the opted-in members of one allied hub

     Alliance member discovery. Read-through: the owning hub answers from its
    own members and nothing is copied. `hub` names the hub to ask (absent
    or this hub's own key = answer locally).

    - **Caller is a member of this hub** and `hub` is an allied hub: this
      hub proxies the request to it. The viewer is deliberately not
      forwarded.
    - **Caller is a peer hub** (or a member asking about this hub): answers
      from `users`. A peer must belong to this alliance and may only ask
      about this hub — never a third.

    A person is listed only when the alliance's `people_visible` switch is
    on, the member set `findable_by_allies`, they are not banned, and the
    hub holds their home-hub designation (so a DM to them can be routed).
    Entries carry only the four fields below; non-opted members are not
    counted or hinted at.

    Paging is the server dialect: a bare array, `limit` (default 100, max
    500) and a keyset `cursor` (the `public_key` of the last entry) over
    `(display_name, public_key)`. `q` matches display name, capped at 64
    characters. Rate limited per caller (60 per minute).

    Advertised as the `alliance.people` capability.

    Args:
        alliance_id (str):
        hub (str | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListAlliancePeopleResponse200Item]
    """

    return (
        await asyncio_detailed(
            alliance_id=alliance_id,
            client=client,
            hub=hub,
            q=q,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
