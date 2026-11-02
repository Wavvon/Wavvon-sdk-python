from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ensure_channel_sticker_body import EnsureChannelStickerBody
from ...models.sticker import Sticker
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    body: EnsureChannelStickerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/channels/{channel_id}/stickers".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Sticker | None:
    if response.status_code == 200:
        response_200 = Sticker.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Sticker.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

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
) -> Response[Any | Sticker]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnsureChannelStickerBody,
) -> Response[Any | Sticker]:
    """Make this hub hold a sticker so a message can reference it

     Returns the existing row when the hash is already here (200); this hub's own pack stickers need no
    `stickers.external`. Otherwise needs `messages.send` and `stickers.external`: the hub fetches
    `{origin_hub_url}/federation/stickers/{sha256}` through its SSRF-checked fetcher, capped at
    `stickers_max_file_bytes` and sharing the link-preview rate limit, checks that the bytes hash to
    `sha256` and come out of normalization unchanged, ingests them (201), and records the origin and its
    `/info` name. An evicted copy is re-fetched the same way. Then send the message with `sticker_id`.

    Args:
        channel_id (str):
        body (EnsureChannelStickerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Sticker]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnsureChannelStickerBody,
) -> Any | Sticker | None:
    """Make this hub hold a sticker so a message can reference it

     Returns the existing row when the hash is already here (200); this hub's own pack stickers need no
    `stickers.external`. Otherwise needs `messages.send` and `stickers.external`: the hub fetches
    `{origin_hub_url}/federation/stickers/{sha256}` through its SSRF-checked fetcher, capped at
    `stickers_max_file_bytes` and sharing the link-preview rate limit, checks that the bytes hash to
    `sha256` and come out of normalization unchanged, ingests them (201), and records the origin and its
    `/info` name. An evicted copy is re-fetched the same way. Then send the message with `sticker_id`.

    Args:
        channel_id (str):
        body (EnsureChannelStickerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Sticker
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnsureChannelStickerBody,
) -> Response[Any | Sticker]:
    """Make this hub hold a sticker so a message can reference it

     Returns the existing row when the hash is already here (200); this hub's own pack stickers need no
    `stickers.external`. Otherwise needs `messages.send` and `stickers.external`: the hub fetches
    `{origin_hub_url}/federation/stickers/{sha256}` through its SSRF-checked fetcher, capped at
    `stickers_max_file_bytes` and sharing the link-preview rate limit, checks that the bytes hash to
    `sha256` and come out of normalization unchanged, ingests them (201), and records the origin and its
    `/info` name. An evicted copy is re-fetched the same way. Then send the message with `sticker_id`.

    Args:
        channel_id (str):
        body (EnsureChannelStickerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Sticker]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnsureChannelStickerBody,
) -> Any | Sticker | None:
    """Make this hub hold a sticker so a message can reference it

     Returns the existing row when the hash is already here (200); this hub's own pack stickers need no
    `stickers.external`. Otherwise needs `messages.send` and `stickers.external`: the hub fetches
    `{origin_hub_url}/federation/stickers/{sha256}` through its SSRF-checked fetcher, capped at
    `stickers_max_file_bytes` and sharing the link-preview rate limit, checks that the bytes hash to
    `sha256` and come out of normalization unchanged, ingests them (201), and records the origin and its
    `/info` name. An evicted copy is re-fetched the same way. Then send the message with `sticker_id`.

    Args:
        channel_id (str):
        body (EnsureChannelStickerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Sticker
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
