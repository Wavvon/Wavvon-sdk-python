from enum import Enum


class VerifyAuthResponse200Scope(str, Enum):
    ALLIANCE_VOICE = "alliance_voice"
    LOBBY = "lobby"
    MEMBER = "member"
    PEER = "peer"

    def __str__(self) -> str:
        return str(self.value)
