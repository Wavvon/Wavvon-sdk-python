from enum import StrEnum


class ListStoredStickersSort(StrEnum):
    CREATED = "created"
    SIZE = "size"
    USED = "used"

    def __str__(self) -> str:
        return str(self.value)
