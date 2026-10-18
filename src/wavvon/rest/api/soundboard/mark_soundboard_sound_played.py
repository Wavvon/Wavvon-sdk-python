from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.mark_soundboard_sound_played_body import MarkSoundboardSoundPlayedBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: MarkSoundboardSoundPlayedBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/soundboard/{id}/played".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any:
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
    body: MarkSoundboardSoundPlayedBody | Unset = UNSET,
) -> Response[Any]:
    """Broadcast a "clip played" attribution event (use_soundboard)

     Attribution UX only — the hub does not verify the clip was actually mixed into the caller's outgoing
    audio; the channel-scoped use_soundboard permission check is the real enforcement.

    Args:
        id (str):
        body (MarkSoundboardSoundPlayedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkSoundboardSoundPlayedBody | Unset = UNSET,
) -> Response[Any]:
    """Broadcast a "clip played" attribution event (use_soundboard)

     Attribution UX only — the hub does not verify the clip was actually mixed into the caller's outgoing
    audio; the channel-scoped use_soundboard permission check is the real enforcement.

    Args:
        id (str):
        body (MarkSoundboardSoundPlayedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
