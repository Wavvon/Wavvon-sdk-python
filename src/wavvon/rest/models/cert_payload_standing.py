from enum import StrEnum


class CertPayloadStanding(StrEnum):
    GOOD = "good"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
