from enum import StrEnum


class CreateAuthChallengeResponse200Scheme(StrEnum):
    TAGGED_V1 = "tagged-v1"
    TAGGED_V2 = "tagged-v2"

    def __str__(self) -> str:
        return str(self.value)
