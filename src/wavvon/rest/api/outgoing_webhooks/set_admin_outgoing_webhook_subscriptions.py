from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_admin_outgoing_webhook_subscriptions_body import (
    SetAdminOutgoingWebhookSubscriptionsBody,
)
from ...models.set_admin_outgoing_webhook_subscriptions_response_200 import (
    SetAdminOutgoingWebhookSubscriptionsResponse200,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SetAdminOutgoingWebhookSubscriptionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/admin/outgoing-webhooks/{id}/subscriptions".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetAdminOutgoingWebhookSubscriptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SetAdminOutgoingWebhookSubscriptionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetAdminOutgoingWebhookSubscriptionsResponse200]:
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
    body: SetAdminOutgoingWebhookSubscriptionsBody,
) -> Response[SetAdminOutgoingWebhookSubscriptionsResponse200]:
    """Replace an outgoing webhook's event subscriptions (admin)

     `message.*` events (other than `message.mention_bot`) require an explicit `channels` list.

    Args:
        id (str):
        body (SetAdminOutgoingWebhookSubscriptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetAdminOutgoingWebhookSubscriptionsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAdminOutgoingWebhookSubscriptionsBody,
) -> SetAdminOutgoingWebhookSubscriptionsResponse200 | None:
    """Replace an outgoing webhook's event subscriptions (admin)

     `message.*` events (other than `message.mention_bot`) require an explicit `channels` list.

    Args:
        id (str):
        body (SetAdminOutgoingWebhookSubscriptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetAdminOutgoingWebhookSubscriptionsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAdminOutgoingWebhookSubscriptionsBody,
) -> Response[SetAdminOutgoingWebhookSubscriptionsResponse200]:
    """Replace an outgoing webhook's event subscriptions (admin)

     `message.*` events (other than `message.mention_bot`) require an explicit `channels` list.

    Args:
        id (str):
        body (SetAdminOutgoingWebhookSubscriptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetAdminOutgoingWebhookSubscriptionsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAdminOutgoingWebhookSubscriptionsBody,
) -> SetAdminOutgoingWebhookSubscriptionsResponse200 | None:
    """Replace an outgoing webhook's event subscriptions (admin)

     `message.*` events (other than `message.mention_bot`) require an explicit `channels` list.

    Args:
        id (str):
        body (SetAdminOutgoingWebhookSubscriptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetAdminOutgoingWebhookSubscriptionsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
