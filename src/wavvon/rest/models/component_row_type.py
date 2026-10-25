from enum import StrEnum


class ComponentRowType(StrEnum):
    ROW = "row"

    def __str__(self) -> str:
        return str(self.value)
