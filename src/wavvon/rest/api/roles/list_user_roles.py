from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.role import Role
from ...types import Response


def _get_kwargs(
    public_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{public_key}/roles".format(
            public_key=quote(str(public_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Role] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Role.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Role]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Role]]:
    """Get roles assigned to a user

    Args:
        public_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Role]]
    """

    kwargs = _get_kwargs(
        public_key=public_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[Role] | None:
    """Get roles assigned to a user

    Args:
        public_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Role]
    """

    return sync_detailed(
        public_key=public_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    public_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Role]]:
    """Get roles assigned to a user

    Args:
        public_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Role]]
    """

    kwargs = _get_kwargs(
        public_key=public_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[Role] | None:
    """Get roles assigned to a user

    Args:
        public_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Role]
    """

    return (
        await asyncio_detailed(
            public_key=public_key,
            client=client,
        )
    ).parsed
