from enum import Enum


class CreateAllianceChannelBodyVoiceRemoteJoin(str, Enum):
    ALLOWED = "allowed"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
