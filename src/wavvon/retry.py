from __future__ import annotations

import asyncio
import math
import random as _random
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

import httpx

from .errors import HubUnavailableError


@dataclass(frozen=True)
class RetryInfo:
    attempt: int
    delay: float
    """Seconds until the next attempt."""
    status: int | None = None
    """HTTP status, or None for a network error or timeout."""
    error: BaseException | None = None


@dataclass(frozen=True)
class RetryOptions:
    max_attempts: float = 8
    """Attempts before giving up with HubUnavailableError. math.inf keeps trying."""
    base_delay: float = 0.5
    """First backoff ceiling, seconds."""
    max_delay: float = 30.0
    """The backoff ceiling never grows past this, seconds."""
    timeout: float = 15.0
    """Per-attempt timeout, seconds; a timeout counts as transient."""
    on_retry: Callable[[RetryInfo], None] | None = None
    """Called before each wait, so a program can show that it is retrying."""


def is_transient_status(status: int) -> bool:
    """429 is "not now"; 5xx is the hub or a proxy in front of it failing."""
    return status == 429 or status >= 500


def backoff_delay(
    attempt: int, opts: RetryOptions | None = None, random: Callable[[], float] = _random.random
) -> float:
    """Full jitter: uniform in [0, min(max_delay, base_delay * 2^(attempt-1))]."""
    o = opts or RetryOptions()
    return random() * min(o.max_delay, math.ldexp(o.base_delay, min(attempt - 1, 64)))


async def fetch_with_retry(
    attempt: Callable[[], Awaitable[httpx.Response]],
    opts: RetryOptions | None = None,
    *,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    random: Callable[[], float] = _random.random,
) -> httpx.Response:
    """Runs `attempt` until it yields a non-transient response. The hub sends no
    Retry-After, so the wait is capped exponential backoff with jitter. When the
    budget runs out this raises HubUnavailableError rather than handing back the
    last 429/5xx: a transient failure must never be mistaken for an answer.

    `attempt` may make several requests (login does) and return whichever
    response decides the outcome. Only transport errors and timeouts are
    retried; any other exception propagates."""
    o = opts or RetryOptions()
    n = 0
    last_status: int | None = None
    last_error: BaseException | None = None
    while True:
        n += 1
        status: int | None = None
        error: BaseException | None = None
        try:
            res = await asyncio.wait_for(attempt(), o.timeout)
            if not is_transient_status(res.status_code):
                return res
            status = res.status_code
            await res.aclose()
        except (TimeoutError, httpx.TransportError) as e:
            error = e
        last_status, last_error = status, error
        if n >= o.max_attempts:
            break
        delay = backoff_delay(n, o, random)
        if o.on_retry:
            o.on_retry(RetryInfo(n, delay, status, error))
        await sleep(delay)
    msg = (
        f"hub kept answering {last_status} after {n} attempts"
        if last_status is not None
        else f"hub unreachable after {n} attempts"
    )
    raise HubUnavailableError(msg, last_status) from last_error
