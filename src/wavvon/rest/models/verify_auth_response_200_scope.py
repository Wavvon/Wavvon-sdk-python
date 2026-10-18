from enum import StrEnum


class VerifyAuthResponse200Scope(StrEnum):
    ALLIANCE_VOICE = "alliance_voice"
    LOBBY = "lobby"
    MEMBER = "member"
    PEER = "peer"

    def __str__(self) -> str:
        return str(self.value)
