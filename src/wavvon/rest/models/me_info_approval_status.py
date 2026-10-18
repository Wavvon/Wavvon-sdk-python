from enum import Enum


class MeInfoApprovalStatus(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
