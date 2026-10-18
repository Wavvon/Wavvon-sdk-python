from enum import StrEnum


class SetMeAppCommandsBodyCommandsItemScope(StrEnum):
    CHANNEL = "channel"
    HUB = "hub"

    def __str__(self) -> str:
        return str(self.value)
