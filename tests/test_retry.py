from __future__ import annotations

import httpx
import pytest

from wavvon import HubUnavailableError, RetryInfo, RetryOptions, backoff_delay, fetch_with_retry, is_transient_status


async def no_sleep(_: float) -> None:
    pass


def one() -> float:
    return 1.0


def test_transient_statuses() -> None:
    assert all(is_transient_status(s) for s in (429, 500, 502, 503))
    assert not any(is_transient_status(s) for s in (200, 400, 401, 403, 404))


def test_backoff_is_exponential_up_to_the_cap() -> None:
    opts = RetryOptions(base_delay=0.1, max_delay=1.0)
    assert [round(backoff_delay(n, opts, one), 6) for n in (1, 2, 3, 4, 5, 9)] == [0.1, 0.2, 0.4, 0.8, 1.0, 1.0]
    assert backoff_delay(3, None, lambda: 0.0) == 0
    assert backoff_delay(10_000, None, one) == 30.0


async def test_retries_429_until_an_answer() -> None:
    statuses = [429, 503, 200]
    seen: list[int | None] = []

    def record(i: RetryInfo) -> None:
        seen.append(i.status)

    async def attempt() -> httpx.Response:
        return httpx.Response(statuses.pop(0))

    res = await fetch_with_retry(attempt, RetryOptions(on_retry=record), sleep=no_sleep, random=one)
    assert res.status_code == 200
    assert seen == [429, 503]


async def test_retries_network_errors() -> None:
    n = 0

    async def attempt() -> httpx.Response:
        nonlocal n
        n += 1
        if n <= 2:
            raise httpx.ConnectError("refused")
        return httpx.Response(200, text="ok")

    assert (await fetch_with_retry(attempt, sleep=no_sleep)).text == "ok"


async def test_never_returns_a_transient_failure_as_the_answer() -> None:
    async def attempt() -> httpx.Response:
        return httpx.Response(429)

    with pytest.raises(HubUnavailableError) as e:
        await fetch_with_retry(attempt, RetryOptions(max_attempts=3), sleep=no_sleep)
    assert e.value.last_status == 429


async def test_returns_a_definitive_refusal_without_retrying() -> None:
    calls = 0

    async def attempt() -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(403)

    assert (await fetch_with_retry(attempt, sleep=no_sleep)).status_code == 403
    assert calls == 1


async def test_does_not_retry_programming_errors() -> None:
    async def attempt() -> httpx.Response:
        raise KeyError("challenge")

    with pytest.raises(KeyError):
        await fetch_with_retry(attempt, sleep=no_sleep)
