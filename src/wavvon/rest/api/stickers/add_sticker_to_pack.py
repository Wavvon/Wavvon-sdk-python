from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_sticker_to_pack_files_body import AddStickerToPackFilesBody
from ...models.add_sticker_to_pack_json_body import AddStickerToPackJsonBody
from ...models.sticker import Sticker
from ...types import UNSET, Response


def _get_kwargs(
    pack_id: str,
    *,
    body: AddStickerToPackFilesBody | AddStickerToPackJsonBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/stickers/packs/{pack_id}/stickers".format(
            pack_id=quote(str(pack_id), safe=""),
        ),
    }

    if isinstance(body, AddStickerToPackFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"
    if isinstance(body, AddStickerToPackJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Sticker | None:
    if response.status_code == 201:
        response_201 = Sticker.from_dict(response.json())

        return response_201

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

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

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
    pack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddStickerToPackFilesBody | AddStickerToPackJsonBody | Unset = UNSET,
) -> Response[Any | Sticker]:
    """Add a sticker to a pack (stickers.packs.manage)

     Either a multipart upload (`file`, optional `name`) or JSON `{sha256}` for a copy this hub already
    holds, which then counts as the hub's own. The file is decoded fully whatever its declared type
    (PNG, JPEG, GIF, WebP, APNG), converted to WebP (animated stays animated) at a fixed maximum of 512
    px, and hashed by the hub. A WebP already within bounds only loses its metadata chunks.

    Args:
        pack_id (str):
        body (AddStickerToPackFilesBody):
        body (AddStickerToPackJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Sticker]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddStickerToPackFilesBody | AddStickerToPackJsonBody | Unset = UNSET,
) -> Any | Sticker | None:
    """Add a sticker to a pack (stickers.packs.manage)

     Either a multipart upload (`file`, optional `name`) or JSON `{sha256}` for a copy this hub already
    holds, which then counts as the hub's own. The file is decoded fully whatever its declared type
    (PNG, JPEG, GIF, WebP, APNG), converted to WebP (animated stays animated) at a fixed maximum of 512
    px, and hashed by the hub. A WebP already within bounds only loses its metadata chunks.

    Args:
        pack_id (str):
        body (AddStickerToPackFilesBody):
        body (AddStickerToPackJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Sticker
    """

    return sync_detailed(
        pack_id=pack_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddStickerToPackFilesBody | AddStickerToPackJsonBody | Unset = UNSET,
) -> Response[Any | Sticker]:
    """Add a sticker to a pack (stickers.packs.manage)

     Either a multipart upload (`file`, optional `name`) or JSON `{sha256}` for a copy this hub already
    holds, which then counts as the hub's own. The file is decoded fully whatever its declared type
    (PNG, JPEG, GIF, WebP, APNG), converted to WebP (animated stays animated) at a fixed maximum of 512
    px, and hashed by the hub. A WebP already within bounds only loses its metadata chunks.

    Args:
        pack_id (str):
        body (AddStickerToPackFilesBody):
        body (AddStickerToPackJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Sticker]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddStickerToPackFilesBody | AddStickerToPackJsonBody | Unset = UNSET,
) -> Any | Sticker | None:
    """Add a sticker to a pack (stickers.packs.manage)

     Either a multipart upload (`file`, optional `name`) or JSON `{sha256}` for a copy this hub already
    holds, which then counts as the hub's own. The file is decoded fully whatever its declared type
    (PNG, JPEG, GIF, WebP, APNG), converted to WebP (animated stays animated) at a fixed maximum of 512
    px, and hashed by the hub. A WebP already within bounds only loses its metadata chunks.

    Args:
        pack_id (str):
        body (AddStickerToPackFilesBody):
        body (AddStickerToPackJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Sticker
    """

    return (
        await asyncio_detailed(
            pack_id=pack_id,
            client=client,
            body=body,
        )
    ).parsed
