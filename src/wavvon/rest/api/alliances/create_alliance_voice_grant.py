from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_alliance_voice_grant_body import CreateAllianceVoiceGrantBody
from ...models.create_alliance_voice_grant_response_200 import (
    CreateAllianceVoiceGrantResponse200,
)
from ...types import Response


def _get_kwargs(
    alliance_id: str,
    *,
    body: CreateAllianceVoiceGrantBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alliances/{alliance_id}/voice-grant".format(
            alliance_id=quote(str(alliance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateAllianceVoiceGrantResponse200 | None:
    if response.status_code == 200:
        response_200 = CreateAllianceVoiceGrantResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateAllianceVoiceGrantResponse200]:
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
    body: CreateAllianceVoiceGrantBody,
) -> Response[Any | CreateAllianceVoiceGrantResponse200]:
    """Mint a voice grant for an allied hub's shared channel

     Called by one of **this** hub's members, for a voice channel owned by
    another member of the alliance. Returns a short-lived (5 minute) grant to
    present at the owning hub's `POST /auth/verify`, plus where to present it.

    This hub gates on the only local permission that means anything about a
    remote channel — the caller is a member here, approved and not muted — and
    resolves the owning hub by asking each alliance member which shared
    channels it owns. Every channel fact is re-checked by the owning hub
    against its own shared set on redemption.

    Args:
        alliance_id (str):
        body (CreateAllianceVoiceGrantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAllianceVoiceGrantResponse200]
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
    body: CreateAllianceVoiceGrantBody,
) -> Any | CreateAllianceVoiceGrantResponse200 | None:
    """Mint a voice grant for an allied hub's shared channel

     Called by one of **this** hub's members, for a voice channel owned by
    another member of the alliance. Returns a short-lived (5 minute) grant to
    present at the owning hub's `POST /auth/verify`, plus where to present it.

    This hub gates on the only local permission that means anything about a
    remote channel — the caller is a member here, approved and not muted — and
    resolves the owning hub by asking each alliance member which shared
    channels it owns. Every channel fact is re-checked by the owning hub
    against its own shared set on redemption.

    Args:
        alliance_id (str):
        body (CreateAllianceVoiceGrantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAllianceVoiceGrantResponse200
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
    body: CreateAllianceVoiceGrantBody,
) -> Response[Any | CreateAllianceVoiceGrantResponse200]:
    """Mint a voice grant for an allied hub's shared channel

     Called by one of **this** hub's members, for a voice channel owned by
    another member of the alliance. Returns a short-lived (5 minute) grant to
    present at the owning hub's `POST /auth/verify`, plus where to present it.

    This hub gates on the only local permission that means anything about a
    remote channel — the caller is a member here, approved and not muted — and
    resolves the owning hub by asking each alliance member which shared
    channels it owns. Every channel fact is re-checked by the owning hub
    against its own shared set on redemption.

    Args:
        alliance_id (str):
        body (CreateAllianceVoiceGrantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateAllianceVoiceGrantResponse200]
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
    body: CreateAllianceVoiceGrantBody,
) -> Any | CreateAllianceVoiceGrantResponse200 | None:
    """Mint a voice grant for an allied hub's shared channel

     Called by one of **this** hub's members, for a voice channel owned by
    another member of the alliance. Returns a short-lived (5 minute) grant to
    present at the owning hub's `POST /auth/verify`, plus where to present it.

    This hub gates on the only local permission that means anything about a
    remote channel — the caller is a member here, approved and not muted — and
    resolves the owning hub by asking each alliance member which shared
    channels it owns. Every channel fact is re-checked by the owning hub
    against its own shared set on redemption.

    Args:
        alliance_id (str):
        body (CreateAllianceVoiceGrantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateAllianceVoiceGrantResponse200
    """

    return (
        await asyncio_detailed(
            alliance_id=alliance_id,
            client=client,
            body=body,
        )
    ).parsed
