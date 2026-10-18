from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dm_message import DmMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: str,
    *,
    limit: int | Unset = 50,
    before: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations/{conversation_id}/messages".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[DmMessage] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DmMessage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DmMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    before: str | Unset = UNSET,
) -> Response[list[DmMessage]]:
    """List messages in a DM conversation (paginated)

     Newest `limit` messages, returned oldest-first. Page backwards with `before` = the `id` of the
    oldest row you already have. Before 2026-08-08 this took no query params and returned the entire
    history on every call, though both clients were already sending these two.

    Args:
        conversation_id (str):
        limit (int | Unset):  Default: 50.
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DmMessage]]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        limit=limit,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    before: str | Unset = UNSET,
) -> list[DmMessage] | None:
    """List messages in a DM conversation (paginated)

     Newest `limit` messages, returned oldest-first. Page backwards with `before` = the `id` of the
    oldest row you already have. Before 2026-08-08 this took no query params and returned the entire
    history on every call, though both clients were already sending these two.

    Args:
        conversation_id (str):
        limit (int | Unset):  Default: 50.
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DmMessage]
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        limit=limit,
        before=before,
    ).parsed


async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    before: str | Unset = UNSET,
) -> Response[list[DmMessage]]:
    """List messages in a DM conversation (paginated)

     Newest `limit` messages, returned oldest-first. Page backwards with `before` = the `id` of the
    oldest row you already have. Before 2026-08-08 this took no query params and returned the entire
    history on every call, though both clients were already sending these two.

    Args:
        conversation_id (str):
        limit (int | Unset):  Default: 50.
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DmMessage]]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        limit=limit,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    before: str | Unset = UNSET,
) -> list[DmMessage] | None:
    """List messages in a DM conversation (paginated)

     Newest `limit` messages, returned oldest-first. Page backwards with `before` = the `id` of the
    oldest row you already have. Before 2026-08-08 this took no query params and returned the entire
    history on every call, though both clients were already sending these two.

    Args:
        conversation_id (str):
        limit (int | Unset):  Default: 50.
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DmMessage]
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            limit=limit,
            before=before,
        )
    ).parsed
