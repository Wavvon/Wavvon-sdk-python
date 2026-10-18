from enum import Enum


class SetHubSettingsChallengeBodyChallengeMode(str, Enum):
    BOTH = "both"
    CLICK = "click"
    OFF = "off"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
