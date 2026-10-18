from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel import Channel
from ...models.create_event_squad_room_body import CreateEventSquadRoomBody
from ...types import Response


def _get_kwargs(
    event_id: str,
    *,
    body: CreateEventSquadRoomBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/events/{event_id}/squad-rooms".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Channel] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = Channel.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Channel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventSquadRoomBody,
) -> Response[list[Channel]]:
    """Auto-spawn temp squad voice channels

     Creates `count` temp voice-capable channels named "<prefix> 1"…"<prefix> N", parented under the
    event's anchor and tagged with the event id so clients can identify them and the reminder worker can
    sweep them at event end. Needs organizer/`create_events` **and** `move_members` on the anchor. See
    events.md §7.5.

    Args:
        event_id (str):
        body (CreateEventSquadRoomBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Channel]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventSquadRoomBody,
) -> list[Channel] | None:
    """Auto-spawn temp squad voice channels

     Creates `count` temp voice-capable channels named "<prefix> 1"…"<prefix> N", parented under the
    event's anchor and tagged with the event id so clients can identify them and the reminder worker can
    sweep them at event end. Needs organizer/`create_events` **and** `move_members` on the anchor. See
    events.md §7.5.

    Args:
        event_id (str):
        body (CreateEventSquadRoomBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Channel]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventSquadRoomBody,
) -> Response[list[Channel]]:
    """Auto-spawn temp squad voice channels

     Creates `count` temp voice-capable channels named "<prefix> 1"…"<prefix> N", parented under the
    event's anchor and tagged with the event id so clients can identify them and the reminder worker can
    sweep them at event end. Needs organizer/`create_events` **and** `move_members` on the anchor. See
    events.md §7.5.

    Args:
        event_id (str):
        body (CreateEventSquadRoomBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Channel]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventSquadRoomBody,
) -> list[Channel] | None:
    """Auto-spawn temp squad voice channels

     Creates `count` temp voice-capable channels named "<prefix> 1"…"<prefix> N", parented under the
    event's anchor and tagged with the event id so clients can identify them and the reminder worker can
    sweep them at event end. Needs organizer/`create_events` **and** `move_members` on the anchor. See
    events.md §7.5.

    Args:
        event_id (str):
        body (CreateEventSquadRoomBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Channel]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
        )
    ).parsed
