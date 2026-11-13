from enum import StrEnum


class AttachmentRefState(StrEnum):
    EXPIRED = "expired"
    OK = "ok"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
