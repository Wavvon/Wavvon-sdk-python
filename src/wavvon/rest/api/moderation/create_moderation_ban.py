from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_moderation_ban_body import CreateModerationBanBody
from ...models.create_moderation_ban_response_201 import CreateModerationBanResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateModerationBanBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/moderation/bans",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateModerationBanResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateModerationBanResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateModerationBanResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateModerationBanBody | Unset = UNSET,
) -> Response[Any | CreateModerationBanResponse201]:
    """Ban a user (moderation.ban.temporary or .permanent)

     Which permission this needs is decided by the request, not the route. `duration_seconds` present
    needs `moderation.ban.temporary`; absent needs `moderation.ban.permanent`. They are split by
    irreversibility — an hour is a cooling-off period, forever ends a membership — so a moderator
    trusted with the first is not thereby trusted with the second.

    Both still require out-ranking the target.

    Args:
        body (CreateModerationBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateModerationBanResponse201]
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
    body: CreateModerationBanBody | Unset = UNSET,
) -> Any | CreateModerationBanResponse201 | None:
    """Ban a user (moderation.ban.temporary or .permanent)

     Which permission this needs is decided by the request, not the route. `duration_seconds` present
    needs `moderation.ban.temporary`; absent needs `moderation.ban.permanent`. They are split by
    irreversibility — an hour is a cooling-off period, forever ends a membership — so a moderator
    trusted with the first is not thereby trusted with the second.

    Both still require out-ranking the target.

    Args:
        body (CreateModerationBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateModerationBanResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateModerationBanBody | Unset = UNSET,
) -> Response[Any | CreateModerationBanResponse201]:
    """Ban a user (moderation.ban.temporary or .permanent)

     Which permission this needs is decided by the request, not the route. `duration_seconds` present
    needs `moderation.ban.temporary`; absent needs `moderation.ban.permanent`. They are split by
    irreversibility — an hour is a cooling-off period, forever ends a membership — so a moderator
    trusted with the first is not thereby trusted with the second.

    Both still require out-ranking the target.

    Args:
        body (CreateModerationBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateModerationBanResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateModerationBanBody | Unset = UNSET,
) -> Any | CreateModerationBanResponse201 | None:
    """Ban a user (moderation.ban.temporary or .permanent)

     Which permission this needs is decided by the request, not the route. `duration_seconds` present
    needs `moderation.ban.temporary`; absent needs `moderation.ban.permanent`. They are split by
    irreversibility — an hour is a cooling-off period, forever ends a membership — so a moderator
    trusted with the first is not thereby trusted with the second.

    Both still require out-ranking the target.

    Args:
        body (CreateModerationBanBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateModerationBanResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
