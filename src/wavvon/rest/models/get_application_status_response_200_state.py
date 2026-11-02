from enum import StrEnum


class GetApplicationStatusResponse200State(StrEnum):
    NONE = "none"
    REJECTED = "rejected"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
