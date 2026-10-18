from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.role_category import RoleCategory
from ...models.update_role_category_body import UpdateRoleCategoryBody
from ...types import Response


def _get_kwargs(
    category_id: str,
    *,
    body: UpdateRoleCategoryBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/role-categories/{category_id}".format(
            category_id=quote(str(category_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RoleCategory | None:
    if response.status_code == 200:
        response_200 = RoleCategory.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RoleCategory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRoleCategoryBody,
) -> Response[RoleCategory]:
    """Update a role category (manage_roles)

    Args:
        category_id (str):
        body (UpdateRoleCategoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoleCategory]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRoleCategoryBody,
) -> RoleCategory | None:
    """Update a role category (manage_roles)

    Args:
        category_id (str):
        body (UpdateRoleCategoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoleCategory
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRoleCategoryBody,
) -> Response[RoleCategory]:
    """Update a role category (manage_roles)

    Args:
        category_id (str):
        body (UpdateRoleCategoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoleCategory]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRoleCategoryBody,
) -> RoleCategory | None:
    """Update a role category (manage_roles)

    Args:
        category_id (str):
        body (UpdateRoleCategoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoleCategory
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
            body=body,
        )
    ).parsed
