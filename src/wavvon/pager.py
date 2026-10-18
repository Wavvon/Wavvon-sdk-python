from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Sequence
from typing import TypeVar

from .errors import WavvonError

T = TypeVar("T")

MAX_PAGE_SIZE = 500
"""The hub clamps `limit` to this; asking for more would look like a short page."""


async def paginate(
    fetch_page: Callable[[str | None, int], Awaitable[Sequence[T]]],
    key: Callable[[T], str],
    limit: int = 100,
) -> AsyncIterator[T]:
    """Walks a keyset-paged list to exhaustion. The hub's dialect is a bare
    array plus `limit` and `cursor`, where the cursor is the key of the
    previous page's last row (`code` for invites, `public_key` for users, `id`
    for most others). A page shorter than `limit` is the end; one page is not
    the list.

    `fetch_page(cursor, limit)` makes the request (so it can name the cursor
    parameter the endpoint uses) and must raise on failure: an error must
    never read as an empty page. Check the endpoint's capability
    (`list.cursor` or `list.cursor.lists`) first; a hub without it ignores the
    cursor, which this detects and reports rather than looping."""
    size = min(max(1, int(limit)), MAX_PAGE_SIZE)
    cursor: str | None = None
    previous_first: str | None = None
    while True:
        page = await fetch_page(cursor, size)
        if page and cursor is not None and key(page[0]) == previous_first:
            raise WavvonError("the hub returned the same page twice: it does not honour the cursor on this endpoint")
        for item in page:
            yield item
        if len(page) < size or not page:
            return
        previous_first = key(page[0])
        cursor = key(page[-1])
