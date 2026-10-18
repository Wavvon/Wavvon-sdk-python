from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_federation_alliance_member_body import (
    DeleteFederationAllianceMemberBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteFederationAllianceMemberBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/federation/alliance-member",
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
    body: DeleteFederationAllianceMemberBody,
) -> Response[Any]:
    """A hub tells the other members that it is leaving the alliance

     Removes the **calling** hub's own membership row and nothing else, so the authenticated peer is the
    whole authorisation. Without it a departure was local: the partners kept the row, kept calling the
    hub, and kept letting it read what the alliance shares.

    Args:
        body (DeleteFederationAllianceMemberBody):

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
    body: DeleteFederationAllianceMemberBody,
) -> Response[Any]:
    """A hub tells the other members that it is leaving the alliance

     Removes the **calling** hub's own membership row and nothing else, so the authenticated peer is the
    whole authorisation. Without it a departure was local: the partners kept the row, kept calling the
    hub, and kept letting it read what the alliance shares.

    Args:
        body (DeleteFederationAllianceMemberBody):

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
