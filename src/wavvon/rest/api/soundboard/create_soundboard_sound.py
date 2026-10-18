from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_soundboard_sound_body import CreateSoundboardSoundBody
from ...models.create_soundboard_sound_response_201 import (
    CreateSoundboardSoundResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSoundboardSoundBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/soundboard",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateSoundboardSoundResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateSoundboardSoundResponse201.from_dict(response.json())

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
) -> Response[Any | CreateSoundboardSoundResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSoundboardSoundBody | Unset = UNSET,
) -> Response[Any | CreateSoundboardSoundResponse201]:
    """Upload a soundboard clip (manage_soundboard)

     Multipart upload: `name` (text), optional `emoji` (text), `audio` (Opus-in-Ogg file, ≤512 KB, ≤10s).
    Hubs cap at 50 clips.

    Args:
        body (CreateSoundboardSoundBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSoundboardSoundResponse201]
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
    body: CreateSoundboardSoundBody | Unset = UNSET,
) -> Any | CreateSoundboardSoundResponse201 | None:
    """Upload a soundboard clip (manage_soundboard)

     Multipart upload: `name` (text), optional `emoji` (text), `audio` (Opus-in-Ogg file, ≤512 KB, ≤10s).
    Hubs cap at 50 clips.

    Args:
        body (CreateSoundboardSoundBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSoundboardSoundResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSoundboardSoundBody | Unset = UNSET,
) -> Response[Any | CreateSoundboardSoundResponse201]:
    """Upload a soundboard clip (manage_soundboard)

     Multipart upload: `name` (text), optional `emoji` (text), `audio` (Opus-in-Ogg file, ≤512 KB, ≤10s).
    Hubs cap at 50 clips.

    Args:
        body (CreateSoundboardSoundBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateSoundboardSoundResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSoundboardSoundBody | Unset = UNSET,
) -> Any | CreateSoundboardSoundResponse201 | None:
    """Upload a soundboard clip (manage_soundboard)

     Multipart upload: `name` (text), optional `emoji` (text), `audio` (Opus-in-Ogg file, ≤512 KB, ≤10s).
    Hubs cap at 50 clips.

    Args:
        body (CreateSoundboardSoundBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateSoundboardSoundResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
