from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.issue_admin_badge_body import IssueAdminBadgeBody
from ...models.issue_admin_badge_response_201 import IssueAdminBadgeResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: IssueAdminBadgeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/badges/issued",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | IssueAdminBadgeResponse201 | None:
    if response.status_code == 201:
        response_201 = IssueAdminBadgeResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | IssueAdminBadgeResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IssueAdminBadgeBody,
) -> Response[Any | IssueAdminBadgeResponse201]:
    """Issue a badge to another hub (admin)

     Fetches the recipient hub's /info, signs the badge payload with this hub's keypair, delivers it to
    the recipient's /federation/badge-offer, and records it locally.

    Args:
        body (IssueAdminBadgeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueAdminBadgeResponse201]
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
    body: IssueAdminBadgeBody,
) -> Any | IssueAdminBadgeResponse201 | None:
    """Issue a badge to another hub (admin)

     Fetches the recipient hub's /info, signs the badge payload with this hub's keypair, delivers it to
    the recipient's /federation/badge-offer, and records it locally.

    Args:
        body (IssueAdminBadgeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueAdminBadgeResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IssueAdminBadgeBody,
) -> Response[Any | IssueAdminBadgeResponse201]:
    """Issue a badge to another hub (admin)

     Fetches the recipient hub's /info, signs the badge payload with this hub's keypair, delivers it to
    the recipient's /federation/badge-offer, and records it locally.

    Args:
        body (IssueAdminBadgeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueAdminBadgeResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IssueAdminBadgeBody,
) -> Any | IssueAdminBadgeResponse201 | None:
    """Issue a badge to another hub (admin)

     Fetches the recipient hub's /info, signs the badge payload with this hub's keypair, delivers it to
    the recipient's /federation/badge-offer, and records it locally.

    Args:
        body (IssueAdminBadgeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueAdminBadgeResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
