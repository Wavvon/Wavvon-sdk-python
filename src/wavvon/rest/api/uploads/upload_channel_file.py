from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment_ref import AttachmentRef
from ...models.upload_channel_file_body import UploadChannelFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    body: UploadChannelFileBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/channels/{channel_id}/upload".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AttachmentRef | None:
    if response.status_code == 201:
        response_201 = AttachmentRef.from_dict(response.json())

        return response_201

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415

    if response.status_code == 507:
        response_507 = cast(Any, None)
        return response_507

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AttachmentRef]:
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
    body: UploadChannelFileBody | Unset = UNSET,
) -> Response[Any | AttachmentRef]:
    """Upload a file to a channel (messages.send there)

     The one way bytes enter, for messages, forum posts and banners alike. Multipart with the file in
    `file`, and optionally `as_file=true`. The type comes from the magic bytes, never from the declared
    one; the response describes what was stored. PNG, APNG, JPEG, GIF and WebP are re-encoded (4096 px
    long edge, metadata dropped; JPEG stays JPEG, the rest becomes WebP) unless `as_file`, which keeps
    the original as a download. Everything else, executables and SVG included, is stored as is and only
    ever downloaded. The hub hashes what it stores and keeps one copy of equal bytes; the response never
    says whether it already held them. Send the returned `id` in `attachment_ids`; an upload nothing
    claims within 24 hours is deleted. Max is the hub's `max_upload_bytes` (512 KB for banner channels,
    which take a raster image only and always re-encode). A full disk expires the oldest attachments
    rather than refusing; only a disk full of something else answers 507. Advertised by
    `attachments.stored`.

    Args:
        channel_id (str):
        body (UploadChannelFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentRef]
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
    body: UploadChannelFileBody | Unset = UNSET,
) -> Any | AttachmentRef | None:
    """Upload a file to a channel (messages.send there)

     The one way bytes enter, for messages, forum posts and banners alike. Multipart with the file in
    `file`, and optionally `as_file=true`. The type comes from the magic bytes, never from the declared
    one; the response describes what was stored. PNG, APNG, JPEG, GIF and WebP are re-encoded (4096 px
    long edge, metadata dropped; JPEG stays JPEG, the rest becomes WebP) unless `as_file`, which keeps
    the original as a download. Everything else, executables and SVG included, is stored as is and only
    ever downloaded. The hub hashes what it stores and keeps one copy of equal bytes; the response never
    says whether it already held them. Send the returned `id` in `attachment_ids`; an upload nothing
    claims within 24 hours is deleted. Max is the hub's `max_upload_bytes` (512 KB for banner channels,
    which take a raster image only and always re-encode). A full disk expires the oldest attachments
    rather than refusing; only a disk full of something else answers 507. Advertised by
    `attachments.stored`.

    Args:
        channel_id (str):
        body (UploadChannelFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentRef
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
    body: UploadChannelFileBody | Unset = UNSET,
) -> Response[Any | AttachmentRef]:
    """Upload a file to a channel (messages.send there)

     The one way bytes enter, for messages, forum posts and banners alike. Multipart with the file in
    `file`, and optionally `as_file=true`. The type comes from the magic bytes, never from the declared
    one; the response describes what was stored. PNG, APNG, JPEG, GIF and WebP are re-encoded (4096 px
    long edge, metadata dropped; JPEG stays JPEG, the rest becomes WebP) unless `as_file`, which keeps
    the original as a download. Everything else, executables and SVG included, is stored as is and only
    ever downloaded. The hub hashes what it stores and keeps one copy of equal bytes; the response never
    says whether it already held them. Send the returned `id` in `attachment_ids`; an upload nothing
    claims within 24 hours is deleted. Max is the hub's `max_upload_bytes` (512 KB for banner channels,
    which take a raster image only and always re-encode). A full disk expires the oldest attachments
    rather than refusing; only a disk full of something else answers 507. Advertised by
    `attachments.stored`.

    Args:
        channel_id (str):
        body (UploadChannelFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentRef]
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
    body: UploadChannelFileBody | Unset = UNSET,
) -> Any | AttachmentRef | None:
    """Upload a file to a channel (messages.send there)

     The one way bytes enter, for messages, forum posts and banners alike. Multipart with the file in
    `file`, and optionally `as_file=true`. The type comes from the magic bytes, never from the declared
    one; the response describes what was stored. PNG, APNG, JPEG, GIF and WebP are re-encoded (4096 px
    long edge, metadata dropped; JPEG stays JPEG, the rest becomes WebP) unless `as_file`, which keeps
    the original as a download. Everything else, executables and SVG included, is stored as is and only
    ever downloaded. The hub hashes what it stores and keeps one copy of equal bytes; the response never
    says whether it already held them. Send the returned `id` in `attachment_ids`; an upload nothing
    claims within 24 hours is deleted. Max is the hub's `max_upload_bytes` (512 KB for banner channels,
    which take a raster image only and always re-encode). A full disk expires the oldest attachments
    rather than refusing; only a disk full of something else answers 507. Advertised by
    `attachments.stored`.

    Args:
        channel_id (str):
        body (UploadChannelFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentRef
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
