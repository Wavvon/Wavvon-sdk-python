from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_voice_pins_response_200 import ListVoicePinsResponse200
from ...types import Response


def _get_kwargs(
    channel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/channels/{channel_id}/voice-pins".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListVoicePinsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListVoicePinsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListVoicePinsResponse200]:
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
) -> Response[ListVoicePinsResponse200]:
    """Who is pinned to this voice room's stage, in pin order

     The room's stage, the same for every viewer. Pins live in memory for one voice session: whoever
    leaves loses their pin and an empty room loses its stage. Behind `voice.pins`.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVoicePinsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListVoicePinsResponse200 | None:
    """Who is pinned to this voice room's stage, in pin order

     The room's stage, the same for every viewer. Pins live in memory for one voice session: whoever
    leaves loses their pin and an empty room loses its stage. Behind `voice.pins`.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVoicePinsResponse200
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListVoicePinsResponse200]:
    """Who is pinned to this voice room's stage, in pin order

     The room's stage, the same for every viewer. Pins live in memory for one voice session: whoever
    leaves loses their pin and an empty room loses its stage. Behind `voice.pins`.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVoicePinsResponse200]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListVoicePinsResponse200 | None:
    """Who is pinned to this voice room's stage, in pin order

     The room's stage, the same for every viewer. Pins live in memory for one voice session: whoever
    leaves loses their pin and an empty room loses its stage. Behind `voice.pins`.

    Args:
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVoicePinsResponse200
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
