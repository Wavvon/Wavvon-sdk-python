from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_push_subscription_body import PutPushSubscriptionBody
from ...types import Response


def _get_kwargs(
    *,
    body: PutPushSubscriptionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/push/subscriptions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 409:
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
    *,
    client: AuthenticatedClient | Client,
    body: PutPushSubscriptionBody,
) -> Response[Any]:
    """Add or update this browser's Web Push subscription

     Keyed by `endpoint` per identity: a second call updates the keys and
    the notify modes. The hub pushes a mention, a reply to the caller's
    message or a DM while the caller has no socket open, is not in
    `dnd`, and the channel (or the hub) is not `silent` in `notify`.
    The encrypted payload (RFC 8291) is only
    `{hub, kind: mention|reply|dm, channel_id | conversation_id}`, never
    message text. The endpoint must be https and resolve to a public
    address unless the operator set `WAVVON_ALLOW_PRIVATE_WEBHOOKS`; a
    404 or 410 from the push service drops the subscription. At most 20
    per identity.

    Args:
        body (PutPushSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PutPushSubscriptionBody,
) -> Response[Any]:
    """Add or update this browser's Web Push subscription

     Keyed by `endpoint` per identity: a second call updates the keys and
    the notify modes. The hub pushes a mention, a reply to the caller's
    message or a DM while the caller has no socket open, is not in
    `dnd`, and the channel (or the hub) is not `silent` in `notify`.
    The encrypted payload (RFC 8291) is only
    `{hub, kind: mention|reply|dm, channel_id | conversation_id}`, never
    message text. The endpoint must be https and resolve to a public
    address unless the operator set `WAVVON_ALLOW_PRIVATE_WEBHOOKS`; a
    404 or 410 from the push service drops the subscription. At most 20
    per identity.

    Args:
        body (PutPushSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
