from enum import StrEnum


class CreateAuthChallengeResponse200Scheme(StrEnum):
    TAGGED_V1 = "tagged-v1"

    def __str__(self) -> str:
        return str(self.value)
