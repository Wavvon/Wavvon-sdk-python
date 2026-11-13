from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_widget_page_theme import GetWidgetPageTheme
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    theme: GetWidgetPageTheme | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_theme: str | Unset = UNSET
    if not isinstance(theme, Unset):
        json_theme = theme.value

    params["theme"] = json_theme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/widget",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    theme: GetWidgetPageTheme | Unset = UNSET,
) -> Response[Any | str]:
    """The online widget as a page for an iframe

     Script-free HTML whose Content-Security-Policy allows any site to frame it. Capability `hub.widget`.

    Args:
        theme (GetWidgetPageTheme | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        theme=theme,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    theme: GetWidgetPageTheme | Unset = UNSET,
) -> Any | str | None:
    """The online widget as a page for an iframe

     Script-free HTML whose Content-Security-Policy allows any site to frame it. Capability `hub.widget`.

    Args:
        theme (GetWidgetPageTheme | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        theme=theme,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    theme: GetWidgetPageTheme | Unset = UNSET,
) -> Response[Any | str]:
    """The online widget as a page for an iframe

     Script-free HTML whose Content-Security-Policy allows any site to frame it. Capability `hub.widget`.

    Args:
        theme (GetWidgetPageTheme | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        theme=theme,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    theme: GetWidgetPageTheme | Unset = UNSET,
) -> Any | str | None:
    """The online widget as a page for an iframe

     Script-free HTML whose Content-Security-Policy allows any site to frame it. Capability `hub.widget`.

    Args:
        theme (GetWidgetPageTheme | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            theme=theme,
        )
    ).parsed
