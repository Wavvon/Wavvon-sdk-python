"""Where the SDK keeps state it must not lose: DH pins, DM ratchet sessions and
group sender chains."""

from __future__ import annotations

from typing import Protocol


class StateStore(Protocol):
    """A byte-valued key/value store. Keys are opaque strings the SDK chooses
    (`dh-pin/<pubkey>`, `dr/<conv>`, `group-own/<conv>`,
    `group-peer/<conv>/<sender>/<version>`); values are JSON.

    Losing DM ratchet state leaves the conversations it belongs to unreadable,
    so a persistent implementation should make `put` durable before it
    returns. The methods are synchronous and called from the event loop."""

    def get(self, key: str) -> bytes | None: ...
    def put(self, key: str, value: bytes) -> None: ...
    def delete(self, key: str) -> None: ...


class MemoryStore:
    """The default: lost when the process ends."""

    def __init__(self) -> None:
        self._m: dict[str, bytes] = {}

    def get(self, key: str) -> bytes | None:
        return self._m.get(key)

    def put(self, key: str, value: bytes) -> None:
        self._m[key] = bytes(value)

    def delete(self, key: str) -> None:
        self._m.pop(key, None)
