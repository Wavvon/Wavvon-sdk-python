from enum import StrEnum


class GetRecoveryRotationRequestResponse200Status(StrEnum):
    APPROVED = "approved"
    PENDING = "pending"
    READY_FOR_REVIEW = "ready_for_review"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
