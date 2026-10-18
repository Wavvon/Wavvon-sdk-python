from enum import StrEnum


class RotateRecoveryKeyResponse201Status(StrEnum):
    PENDING = "pending"
    READY_FOR_REVIEW = "ready_for_review"

    def __str__(self) -> str:
        return str(self.value)
