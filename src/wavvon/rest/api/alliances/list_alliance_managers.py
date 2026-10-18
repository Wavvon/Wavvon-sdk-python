from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alliance_managers_response_200_item import (
    ListAllianceManagersResponse200Item,
)
from ...types import Response


def _get_kwargs(
    alliance_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alliances/{alliance_id}/managers".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListAllianceManagersResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAllianceManagersResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListAllianceManagersResponse200Item]]:
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
) -> Response[list[ListAllianceManagersResponse200Item]]:
    """Roles that may act on this alliance

     The per-alliance grant list (decisions.md, "Alliance permissions"): the local roles that may invite
    another hub into this alliance, share and unshare a channel in it, and set the per-share policies.
    `alliances.manage` answers for every alliance and is not listed here. Readable by anyone who may act
    on this alliance. Present only on hubs advertising `alliance.permissions`.

    Args:
        alliance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAllianceManagersResponse200Item]]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[ListAllianceManagersResponse200Item] | None:
    """Roles that may act on this alliance

     The per-alliance grant list (decisions.md, "Alliance permissions"): the local roles that may invite
    another hub into this alliance, share and unshare a channel in it, and set the per-share policies.
    `alliances.manage` answers for every alliance and is not listed here. Readable by anyone who may act
    on this alliance. Present only on hubs advertising `alliance.permissions`.

    Args:
        alliance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAllianceManagersResponse200Item]
    """

    return sync_detailed(
        alliance_id=alliance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[ListAllianceManagersResponse200Item]]:
    """Roles that may act on this alliance

     The per-alliance grant list (decisions.md, "Alliance permissions"): the local roles that may invite
    another hub into this alliance, share and unshare a channel in it, and set the per-share policies.
    `alliances.manage` answers for every alliance and is not listed here. Readable by anyone who may act
    on this alliance. Present only on hubs advertising `alliance.permissions`.

    Args:
        alliance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListAllianceManagersResponse200Item]]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[ListAllianceManagersResponse200Item] | None:
    """Roles that may act on this alliance

     The per-alliance grant list (decisions.md, "Alliance permissions"): the local roles that may invite
    another hub into this alliance, share and unshare a channel in it, and set the per-share policies.
    `alliances.manage` answers for every alliance and is not listed here. Readable by anyone who may act
    on this alliance. Present only on hubs advertising `alliance.permissions`.

    Args:
        alliance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListAllianceManagersResponse200Item]
    """

    return (
        await asyncio_detailed(
            alliance_id=alliance_id,
            client=client,
        )
    ).parsed
