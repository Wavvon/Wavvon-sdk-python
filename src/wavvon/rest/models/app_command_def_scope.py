from enum import StrEnum


class AppCommandDefScope(StrEnum):
    CHANNEL = "channel"
    HUB = "hub"

    def __str__(self) -> str:
        return str(self.value)
