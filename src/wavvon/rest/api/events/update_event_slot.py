from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_event_slot_body import UpdateEventSlotBody
from ...models.update_event_slot_response_200 import UpdateEventSlotResponse200
from ...types import Response


def _get_kwargs(
    event_id: str,
    slot_id: str,
    *,
    body: UpdateEventSlotBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/events/{event_id}/slots/{slot_id}".format(
            event_id=quote(str(event_id), safe=""),
            slot_id=quote(str(slot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateEventSlotResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateEventSlotResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UpdateEventSlotResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    slot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEventSlotBody,
) -> Response[Any | UpdateEventSlotResponse200]:
    """Rename or resize a slot (creator or admin)

     Rejects shrinking capacity below the current claim count; demote claimants off the slot first.

    Args:
        event_id (str):
        slot_id (str):
        body (UpdateEventSlotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateEventSlotResponse200]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        slot_id=slot_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    slot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEventSlotBody,
) -> Any | UpdateEventSlotResponse200 | None:
    """Rename or resize a slot (creator or admin)

     Rejects shrinking capacity below the current claim count; demote claimants off the slot first.

    Args:
        event_id (str):
        slot_id (str):
        body (UpdateEventSlotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateEventSlotResponse200
    """

    return sync_detailed(
        event_id=event_id,
        slot_id=slot_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    slot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEventSlotBody,
) -> Response[Any | UpdateEventSlotResponse200]:
    """Rename or resize a slot (creator or admin)

     Rejects shrinking capacity below the current claim count; demote claimants off the slot first.

    Args:
        event_id (str):
        slot_id (str):
        body (UpdateEventSlotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateEventSlotResponse200]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        slot_id=slot_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    slot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEventSlotBody,
) -> Any | UpdateEventSlotResponse200 | None:
    """Rename or resize a slot (creator or admin)

     Rejects shrinking capacity below the current claim count; demote claimants off the slot first.

    Args:
        event_id (str):
        slot_id (str):
        body (UpdateEventSlotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateEventSlotResponse200
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            slot_id=slot_id,
            client=client,
            body=body,
        )
    ).parsed
