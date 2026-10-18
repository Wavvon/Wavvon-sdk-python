from enum import Enum


class CertPayloadStanding(str, Enum):
    GOOD = "good"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
