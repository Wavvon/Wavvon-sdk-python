from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    master: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/identity/{master}/designation".format(
            master=quote(str(master), safe=""),
        ),
    }

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
    master: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Publish a master-signed home-hub list

     Unauthenticated on purpose: a client publishes the same designation to every hub in the list it just
    signed, and holds a session with at most one of them. The signature is what makes it safe — you can
    only write your own designation, one row per master, and only forward (`sequence` must exceed the
    stored one).

    **403** when this hub has never met the identity behind `master`: no member carries it, and no
    device cert for it names a subkey that is a member here. Such a row could never be read — the lookup
    starts from a member — so it was only ever a way for a stranger to leave rows behind.

    Args:
        master (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        master=master,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    master: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Publish a master-signed home-hub list

     Unauthenticated on purpose: a client publishes the same designation to every hub in the list it just
    signed, and holds a session with at most one of them. The signature is what makes it safe — you can
    only write your own designation, one row per master, and only forward (`sequence` must exceed the
    stored one).

    **403** when this hub has never met the identity behind `master`: no member carries it, and no
    device cert for it names a subkey that is a member here. Such a row could never be read — the lookup
    starts from a member — so it was only ever a way for a stranger to leave rows behind.

    Args:
        master (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        master=master,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
