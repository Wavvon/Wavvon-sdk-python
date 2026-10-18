from enum import Enum


class ListAdminReportsStatus(str, Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
