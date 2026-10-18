from enum import StrEnum


class SetHubSettingsChallengeBodyChallengeMode(StrEnum):
    BOTH = "both"
    CLICK = "click"
    OFF = "off"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
