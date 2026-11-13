from enum import StrEnum


class ListStoredStickersState(StrEnum):
    EVICTED = "evicted"
    OK = "ok"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
