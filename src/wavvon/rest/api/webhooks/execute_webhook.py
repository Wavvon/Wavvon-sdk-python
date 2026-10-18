from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_webhook_body import ExecuteWebhookBody
from ...models.execute_webhook_response_200 import ExecuteWebhookResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    token: str,
    *,
    body: ExecuteWebhookBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{id}/{token}".format(
            id=quote(str(id), safe=""),
            token=quote(str(token), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ExecuteWebhookResponse200 | None:
    if response.status_code == 200:
        response_200 = ExecuteWebhookResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ExecuteWebhookResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteWebhookBody,
) -> Response[Any | ExecuteWebhookResponse200]:
    """Post a message via an incoming webhook

     No Authorization header — the token in the URL is the credential (compared in constant time against
    the stored hash).

    Args:
        id (str):
        token (str):
        body (ExecuteWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExecuteWebhookResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteWebhookBody,
) -> Any | ExecuteWebhookResponse200 | None:
    """Post a message via an incoming webhook

     No Authorization header — the token in the URL is the credential (compared in constant time against
    the stored hash).

    Args:
        id (str):
        token (str):
        body (ExecuteWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExecuteWebhookResponse200
    """

    return sync_detailed(
        id=id,
        token=token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteWebhookBody,
) -> Response[Any | ExecuteWebhookResponse200]:
    """Post a message via an incoming webhook

     No Authorization header — the token in the URL is the credential (compared in constant time against
    the stored hash).

    Args:
        id (str):
        token (str):
        body (ExecuteWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExecuteWebhookResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteWebhookBody,
) -> Any | ExecuteWebhookResponse200 | None:
    """Post a message via an incoming webhook

     No Authorization header — the token in the URL is the credential (compared in constant time against
    the stored hash).

    Args:
        id (str):
        token (str):
        body (ExecuteWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExecuteWebhookResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            token=token,
            client=client,
            body=body,
        )
    ).parsed
