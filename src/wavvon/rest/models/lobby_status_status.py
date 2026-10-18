from enum import Enum


class LobbyStatusStatus(str, Enum):
    LOBBY = "lobby"
    MEMBER = "member"
    PROMOTED = "promoted"

    def __str__(self) -> str:
        return str(self.value)
