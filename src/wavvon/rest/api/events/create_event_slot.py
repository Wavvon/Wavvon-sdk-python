from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_event_slot_response_201 import CreateEventSlotResponse201
from ...models.create_slot_request import CreateSlotRequest
from ...types import Response


def _get_kwargs(
    event_id: str,
    *,
    body: CreateSlotRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/events/{event_id}/slots".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateEventSlotResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateEventSlotResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateEventSlotResponse201]:
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
    body: CreateSlotRequest,
) -> Response[CreateEventSlotResponse201]:
    """Create a sign-up slot for an event (creator or admin)

    Args:
        event_id (str):
        body (CreateSlotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEventSlotResponse201]
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
    body: CreateSlotRequest,
) -> CreateEventSlotResponse201 | None:
    """Create a sign-up slot for an event (creator or admin)

    Args:
        event_id (str):
        body (CreateSlotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEventSlotResponse201
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
    body: CreateSlotRequest,
) -> Response[CreateEventSlotResponse201]:
    """Create a sign-up slot for an event (creator or admin)

    Args:
        event_id (str):
        body (CreateSlotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEventSlotResponse201]
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
    body: CreateSlotRequest,
) -> CreateEventSlotResponse201 | None:
    """Create a sign-up slot for an event (creator or admin)

    Args:
        event_id (str):
        body (CreateSlotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEventSlotResponse201
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
        )
    ).parsed
