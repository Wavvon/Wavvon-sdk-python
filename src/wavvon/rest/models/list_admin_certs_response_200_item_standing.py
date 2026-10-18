from enum import StrEnum


class ListAdminCertsResponse200ItemStanding(StrEnum):
    GOOD = "good"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
