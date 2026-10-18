from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_event_assignments_response_200_item import (
    ListEventAssignmentsResponse200Item,
)
from ...types import Response


def _get_kwargs(
    event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/{event_id}/assignments".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ListEventAssignmentsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListEventAssignmentsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[ListEventAssignmentsResponse200Item]]:
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
) -> Response[Any | list[ListEventAssignmentsResponse200Item]]:
    """Every move assignment for an event

     Requires `read_messages` on the event's anchor channel plus organizer or `move_members`. 404 (not
    403) when the event does not exist or the caller cannot read its anchor — an id alone must not
    confirm a hidden channel exists. See events.md §7.4.

    Args:
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListEventAssignmentsResponse200Item]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | list[ListEventAssignmentsResponse200Item] | None:
    """Every move assignment for an event

     Requires `read_messages` on the event's anchor channel plus organizer or `move_members`. 404 (not
    403) when the event does not exist or the caller cannot read its anchor — an id alone must not
    confirm a hidden channel exists. See events.md §7.4.

    Args:
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListEventAssignmentsResponse200Item]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | list[ListEventAssignmentsResponse200Item]]:
    """Every move assignment for an event

     Requires `read_messages` on the event's anchor channel plus organizer or `move_members`. 404 (not
    403) when the event does not exist or the caller cannot read its anchor — an id alone must not
    confirm a hidden channel exists. See events.md §7.4.

    Args:
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListEventAssignmentsResponse200Item]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | list[ListEventAssignmentsResponse200Item] | None:
    """Every move assignment for an event

     Requires `read_messages` on the event's anchor channel plus organizer or `move_members`. 404 (not
    403) when the event does not exist or the caller cannot read its anchor — an id alone must not
    confirm a hidden channel exists. See events.md §7.4.

    Args:
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListEventAssignmentsResponse200Item]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed
