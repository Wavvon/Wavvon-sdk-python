from enum import StrEnum


class AdminStickerState(StrEnum):
    EVICTED = "evicted"
    OK = "ok"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
