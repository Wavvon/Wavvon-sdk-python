from enum import Enum


class CreateAuthChallengeResponse200Scheme(str, Enum):
    TAGGED_V1 = "tagged-v1"

    def __str__(self) -> str:
        return str(self.value)
