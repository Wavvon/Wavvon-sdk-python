from enum import Enum


class SetMeAppCommandsBodyCommandsItemScope(str, Enum):
    CHANNEL = "channel"
    HUB = "hub"

    def __str__(self) -> str:
        return str(self.value)
