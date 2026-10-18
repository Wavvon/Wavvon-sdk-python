from enum import StrEnum


class LobbyStatusStatus(StrEnum):
    LOBBY = "lobby"
    MEMBER = "member"
    PROMOTED = "promoted"

    def __str__(self) -> str:
        return str(self.value)
