from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    block: bool | Unset = False,
    reason: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["block"] = block

    params["reason"] = reason

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/admin/stickers/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    block: bool | Unset = False,
    reason: str | Unset = UNSET,
) -> Response[Any]:
    """Delete a stored sticker, optionally blocking its hash (stickers.moderate)

     The bytes go and the row stays as the "sticker removed" tombstone that messages render. With
    `block=true` the hash is also refused at every later ingest; without it a removed row still refuses
    the same image until the orphan sweep deletes it.

    Args:
        id (str):
        block (bool | Unset):  Default: False.
        reason (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        block=block,
        reason=reason,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    block: bool | Unset = False,
    reason: str | Unset = UNSET,
) -> Response[Any]:
    """Delete a stored sticker, optionally blocking its hash (stickers.moderate)

     The bytes go and the row stays as the "sticker removed" tombstone that messages render. With
    `block=true` the hash is also refused at every later ingest; without it a removed row still refuses
    the same image until the orphan sweep deletes it.

    Args:
        id (str):
        block (bool | Unset):  Default: False.
        reason (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        block=block,
        reason=reason,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
