from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.federation_join_alliance_body import FederationJoinAllianceBody
from ...models.federation_join_alliance_response_200 import (
    FederationJoinAllianceResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alliance_id: str,
    *,
    body: FederationJoinAllianceBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alliances/{alliance_id}/join".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FederationJoinAllianceResponse200 | None:
    if response.status_code == 200:
        response_200 = FederationJoinAllianceResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FederationJoinAllianceResponse200]:
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
    body: FederationJoinAllianceBody | Unset = UNSET,
) -> Response[FederationJoinAllianceResponse200]:
    """Remote hub joins an alliance with an invite token

     Hub-to-hub, with the joining hub's peer session (`is_hub` authentication). The invite token is
    single-use and expires after seven days; hub_url must answer for the authenticated key. Answers with
    a voucher the new member presents to the other members (`POST /federation/alliance-member`).

    Args:
        alliance_id (str):
        body (FederationJoinAllianceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FederationJoinAllianceResponse200]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FederationJoinAllianceBody | Unset = UNSET,
) -> FederationJoinAllianceResponse200 | None:
    """Remote hub joins an alliance with an invite token

     Hub-to-hub, with the joining hub's peer session (`is_hub` authentication). The invite token is
    single-use and expires after seven days; hub_url must answer for the authenticated key. Answers with
    a voucher the new member presents to the other members (`POST /federation/alliance-member`).

    Args:
        alliance_id (str):
        body (FederationJoinAllianceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FederationJoinAllianceResponse200
    """

    return sync_detailed(
        alliance_id=alliance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FederationJoinAllianceBody | Unset = UNSET,
) -> Response[FederationJoinAllianceResponse200]:
    """Remote hub joins an alliance with an invite token

     Hub-to-hub, with the joining hub's peer session (`is_hub` authentication). The invite token is
    single-use and expires after seven days; hub_url must answer for the authenticated key. Answers with
    a voucher the new member presents to the other members (`POST /federation/alliance-member`).

    Args:
        alliance_id (str):
        body (FederationJoinAllianceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FederationJoinAllianceResponse200]
    """

    kwargs = _get_kwargs(
        alliance_id=alliance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alliance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FederationJoinAllianceBody | Unset = UNSET,
) -> FederationJoinAllianceResponse200 | None:
    """Remote hub joins an alliance with an invite token

     Hub-to-hub, with the joining hub's peer session (`is_hub` authentication). The invite token is
    single-use and expires after seven days; hub_url must answer for the authenticated key. Answers with
    a voucher the new member presents to the other members (`POST /federation/alliance-member`).

    Args:
        alliance_id (str):
        body (FederationJoinAllianceBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FederationJoinAllianceResponse200
    """

    return (
        await asyncio_detailed(
            alliance_id=alliance_id,
            client=client,
            body=body,
        )
    ).parsed
