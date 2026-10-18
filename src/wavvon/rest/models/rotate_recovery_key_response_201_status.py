from enum import Enum


class RotateRecoveryKeyResponse201Status(str, Enum):
    PENDING = "pending"
    READY_FOR_REVIEW = "ready_for_review"

    def __str__(self) -> str:
        return str(self.value)
