from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    thread_root: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["thread_root"] = thread_root

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/channels/{channel_id}/messages".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Message] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Message.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Message]]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    thread_root: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[list[Message]]:
    """Fetch message history

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        thread_root (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Message]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        cursor=cursor,
        limit=limit,
        thread_root=thread_root,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    thread_root: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> list[Message] | None:
    """Fetch message history

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        thread_root (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Message]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        cursor=cursor,
        limit=limit,
        thread_root=thread_root,
        q=q,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    thread_root: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[list[Message]]:
    """Fetch message history

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        thread_root (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Message]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        cursor=cursor,
        limit=limit,
        thread_root=thread_root,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    thread_root: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> list[Message] | None:
    """Fetch message history

    Args:
        channel_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        thread_root (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Message]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            cursor=cursor,
            limit=limit,
            thread_root=thread_root,
            q=q,
        )
    ).parsed
