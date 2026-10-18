from enum import StrEnum


class CreateAllianceChannelBodyVoiceRemoteJoin(StrEnum):
    ALLOWED = "allowed"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
