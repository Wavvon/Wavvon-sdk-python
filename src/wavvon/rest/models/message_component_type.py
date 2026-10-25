from enum import StrEnum


class MessageComponentType(StrEnum):
    BUTTON = "button"
    SELECT = "select"

    def __str__(self) -> str:
        return str(self.value)
