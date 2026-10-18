from enum import Enum


class ListAdminCertsResponse200ItemStanding(str, Enum):
    GOOD = "good"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
