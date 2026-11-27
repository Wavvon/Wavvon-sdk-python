from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.badge_def import BadgeDef
from ...models.badge_def_request import BadgeDefRequest
from ...types import Response


def _get_kwargs(
    *,
    body: BadgeDefRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/badge-defs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadgeDef | None:
    if response.status_code == 201:
        response_201 = BadgeDef.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BadgeDef]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BadgeDefRequest,
) -> Response[Any | BadgeDef]:
    """Define a hub badge, by hand or by rule (badges.manage)

     A rule badge is retroactive; whoever already qualifies receives it at once.

    Args:
        body (BadgeDefRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadgeDef]
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
    body: BadgeDefRequest,
) -> Any | BadgeDef | None:
    """Define a hub badge, by hand or by rule (badges.manage)

     A rule badge is retroactive; whoever already qualifies receives it at once.

    Args:
        body (BadgeDefRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadgeDef
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BadgeDefRequest,
) -> Response[Any | BadgeDef]:
    """Define a hub badge, by hand or by rule (badges.manage)

     A rule badge is retroactive; whoever already qualifies receives it at once.

    Args:
        body (BadgeDefRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadgeDef]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BadgeDefRequest,
) -> Any | BadgeDef | None:
    """Define a hub badge, by hand or by rule (badges.manage)

     A rule badge is retroactive; whoever already qualifies receives it at once.

    Args:
        body (BadgeDefRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadgeDef
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
