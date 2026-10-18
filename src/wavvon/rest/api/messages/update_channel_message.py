from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.update_channel_message_body import UpdateChannelMessageBody
from ...types import Response


def _get_kwargs(
    channel_id: str,
    message_id: str,
    *,
    body: UpdateChannelMessageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/channels/{channel_id}/messages/{message_id}".format(
            channel_id=quote(str(channel_id), safe=""),
            message_id=quote(str(message_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | None:
    if response.status_code == 200:
        response_200 = Message.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    message_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelMessageBody,
) -> Response[Message]:
    """Edit own message

    Args:
        channel_id (str):
        message_id (str):
        body (UpdateChannelMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        message_id=message_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    message_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelMessageBody,
) -> Message | None:
    """Edit own message

    Args:
        channel_id (str):
        message_id (str):
        body (UpdateChannelMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message
    """

    return sync_detailed(
        channel_id=channel_id,
        message_id=message_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    message_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelMessageBody,
) -> Response[Message]:
    """Edit own message

    Args:
        channel_id (str):
        message_id (str):
        body (UpdateChannelMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        message_id=message_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    message_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChannelMessageBody,
) -> Message | None:
    """Edit own message

    Args:
        channel_id (str):
        message_id (str):
        body (UpdateChannelMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            message_id=message_id,
            client=client,
            body=body,
        )
    ).parsed
