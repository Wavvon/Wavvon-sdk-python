from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_alliance_people_visibility_body import (
    SetAlliancePeopleVisibilityBody,
)
from ...types import Response


def _get_kwargs(
    alliance_id: str,
    *,
    body: SetAlliancePeopleVisibilityBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/alliances/{alliance_id}/people-visibility".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
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
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAlliancePeopleVisibilityBody,
) -> Response[Any]:
    """Allow or withhold this hub's people for one alliance (alliance manager)

     The alliance-level consent switch, off by default. Mirrored as `people_visible` on `GET
    /alliances/{alliance_id}`. Hubs advertising `alliance.people`.

    Args:
        alliance_id (str):
        body (SetAlliancePeopleVisibilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAlliancePeopleVisibilityBody,
) -> Response[Any]:
    """Allow or withhold this hub's people for one alliance (alliance manager)

     The alliance-level consent switch, off by default. Mirrored as `people_visible` on `GET
    /alliances/{alliance_id}`. Hubs advertising `alliance.people`.

    Args:
        alliance_id (str):
        body (SetAlliancePeopleVisibilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
