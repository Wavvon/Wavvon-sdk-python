from enum import Enum


class GetRecoveryRotationRequestResponse200Status(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"
    READY_FOR_REVIEW = "ready_for_review"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
