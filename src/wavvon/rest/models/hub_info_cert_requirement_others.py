from enum import StrEnum


class HubInfoCertRequirementOthers(StrEnum):
    LOBBY = "lobby"
    REFUSE = "refuse"

    def __str__(self) -> str:
        return str(self.value)
