from enum import StrEnum


class MeInfoApprovalStatus(StrEnum):
    APPROVED = "approved"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
