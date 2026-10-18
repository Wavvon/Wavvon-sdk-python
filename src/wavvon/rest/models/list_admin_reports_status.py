from enum import StrEnum


class ListAdminReportsStatus(StrEnum):
    PENDING = "pending"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
