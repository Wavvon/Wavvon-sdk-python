from enum import StrEnum


class AttachmentRefKind(StrEnum):
    FILE = "file"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
