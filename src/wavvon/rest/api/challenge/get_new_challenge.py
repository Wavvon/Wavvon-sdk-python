from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_prompt import ChallengePrompt
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/challenge/new",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChallengePrompt | None:
    if response.status_code == 200:
        response_200 = ChallengePrompt.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChallengePrompt]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengePrompt]:
    """Fetch a bot-challenge prompt

     Returns a challenge the user must solve before auth. Mode is set by the hub admin.
    - `click`: no SVG, user just confirms they are human.
    - `puzzle`: SVG math puzzle, user types the answer.
    - `both`: SVG puzzle shown, click confirmation also required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengePrompt]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ChallengePrompt | None:
    """Fetch a bot-challenge prompt

     Returns a challenge the user must solve before auth. Mode is set by the hub admin.
    - `click`: no SVG, user just confirms they are human.
    - `puzzle`: SVG math puzzle, user types the answer.
    - `both`: SVG puzzle shown, click confirmation also required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengePrompt
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengePrompt]:
    """Fetch a bot-challenge prompt

     Returns a challenge the user must solve before auth. Mode is set by the hub admin.
    - `click`: no SVG, user just confirms they are human.
    - `puzzle`: SVG math puzzle, user types the answer.
    - `both`: SVG puzzle shown, click confirmation also required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengePrompt]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ChallengePrompt | None:
    """Fetch a bot-challenge prompt

     Returns a challenge the user must solve before auth. Mode is set by the hub admin.
    - `click`: no SVG, user just confirms they are human.
    - `puzzle`: SVG math puzzle, user types the answer.
    - `both`: SVG puzzle shown, click confirmation also required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengePrompt
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
