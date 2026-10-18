from __future__ import annotations

from collections.abc import AsyncIterator, Sequence
from typing import TypeVar

import pytest

from wavvon import WavvonError, paginate

T = TypeVar("T")
ROWS = [{"code": f"c{i}"} for i in range(7)]


def code(r: dict[str, str]) -> str:
    return r["code"]


async def endpoint(cursor: str | None, limit: int) -> Sequence[dict[str, str]]:
    start = 0 if cursor is None else next(i for i, r in enumerate(ROWS) if r["code"] == cursor) + 1
    return ROWS[start : start + limit]


async def collect(it: AsyncIterator[T]) -> list[T]:
    return [x async for x in it]


async def test_walks_every_page() -> None:
    assert await collect(paginate(endpoint, code, 3)) == ROWS


async def test_stops_on_an_exactly_full_last_page_after_one_empty_fetch() -> None:
    cursors: list[str | None] = []

    async def page(c: str | None, n: int) -> Sequence[dict[str, str]]:
        cursors.append(c)
        return await endpoint(c, n)

    assert await collect(paginate(page, code, 7)) == ROWS
    assert cursors == [None, "c6"]


async def test_clamps_the_page_size() -> None:
    limits: list[int] = []

    async def page(c: str | None, n: int) -> Sequence[dict[str, str]]:
        limits.append(n)
        return await endpoint(c, n)

    await collect(paginate(page, code, 10_000))
    assert limits[0] == 500


async def test_refuses_to_loop_on_a_hub_that_ignores_the_cursor() -> None:
    async def full(_c: str | None, n: int) -> Sequence[dict[str, str]]:
        return ROWS[:n]

    with pytest.raises(WavvonError):
        await collect(paginate(full, code, 3))


async def test_propagates_a_failed_page_instead_of_ending_the_list() -> None:
    async def failing(c: str | None, n: int) -> Sequence[dict[str, str]]:
        if c:
            raise RuntimeError("503")
        return await endpoint(c, n)

    with pytest.raises(RuntimeError, match="503"):
        await collect(paginate(failing, code, 3))
