from enum import StrEnum


class ListAdminSettingsCertsResponse200CertOthers(StrEnum):
    LOBBY = "lobby"
    REFUSE = "refuse"

    def __str__(self) -> str:
        return str(self.value)
