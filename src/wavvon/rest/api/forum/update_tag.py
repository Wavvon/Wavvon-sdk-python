from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forum_tag import ForumTag
from ...models.update_tag_body import UpdateTagBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tag_id: str,
    *,
    body: UpdateTagBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/tags/{tag_id}".format(
            tag_id=quote(str(tag_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ForumTag | None:
    if response.status_code == 200:
        response_200 = ForumTag.from_dict(response.json())

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
) -> Response[Any | ForumTag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagBody | Unset = UNSET,
) -> Response[Any | ForumTag]:
    """Edit a tag definition (manage_posts)

     No channel in the path — it is resolved from the tag row. `label` and `position` follow the usual
    "absent means unchanged" rule; `color` is tri-state, so omitting it leaves the colour alone while
    sending `null` clears it.

    Args:
        tag_id (str):
        body (UpdateTagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ForumTag]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagBody | Unset = UNSET,
) -> Any | ForumTag | None:
    """Edit a tag definition (manage_posts)

     No channel in the path — it is resolved from the tag row. `label` and `position` follow the usual
    "absent means unchanged" rule; `color` is tri-state, so omitting it leaves the colour alone while
    sending `null` clears it.

    Args:
        tag_id (str):
        body (UpdateTagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ForumTag
    """

    return sync_detailed(
        tag_id=tag_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagBody | Unset = UNSET,
) -> Response[Any | ForumTag]:
    """Edit a tag definition (manage_posts)

     No channel in the path — it is resolved from the tag row. `label` and `position` follow the usual
    "absent means unchanged" rule; `color` is tri-state, so omitting it leaves the colour alone while
    sending `null` clears it.

    Args:
        tag_id (str):
        body (UpdateTagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ForumTag]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagBody | Unset = UNSET,
) -> Any | ForumTag | None:
    """Edit a tag definition (manage_posts)

     No channel in the path — it is resolved from the tag row. `label` and `position` follow the usual
    "absent means unchanged" rule; `color` is tri-state, so omitting it leaves the colour alone while
    sending `null` clears it.

    Args:
        tag_id (str):
        body (UpdateTagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ForumTag
    """

    return (
        await asyncio_detailed(
            tag_id=tag_id,
            client=client,
            body=body,
        )
    ).parsed
