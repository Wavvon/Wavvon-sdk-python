from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_admin_webhook_body import CreateAdminWebhookBody
from ...models.create_admin_webhook_response_201 import CreateAdminWebhookResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAdminWebhookBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/webhooks",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAdminWebhookResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateAdminWebhookResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAdminWebhookResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminWebhookBody | Unset = UNSET,
) -> Response[CreateAdminWebhookResponse201]:
    """Create an incoming webhook for a channel (admin)

     The returned `webhook_url` embeds the secret token and is shown **once** — only its hash is stored.

    Args:
        body (CreateAdminWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAdminWebhookResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminWebhookBody | Unset = UNSET,
) -> CreateAdminWebhookResponse201 | None:
    """Create an incoming webhook for a channel (admin)

     The returned `webhook_url` embeds the secret token and is shown **once** — only its hash is stored.

    Args:
        body (CreateAdminWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAdminWebhookResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminWebhookBody | Unset = UNSET,
) -> Response[CreateAdminWebhookResponse201]:
    """Create an incoming webhook for a channel (admin)

     The returned `webhook_url` embeds the secret token and is shown **once** — only its hash is stored.

    Args:
        body (CreateAdminWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAdminWebhookResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAdminWebhookBody | Unset = UNSET,
) -> CreateAdminWebhookResponse201 | None:
    """Create an incoming webhook for a channel (admin)

     The returned `webhook_url` embeds the secret token and is shown **once** — only its hash is stored.

    Args:
        body (CreateAdminWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAdminWebhookResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
