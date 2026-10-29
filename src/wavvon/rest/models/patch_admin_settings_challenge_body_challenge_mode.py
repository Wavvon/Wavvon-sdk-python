from enum import StrEnum


class PatchAdminSettingsChallengeBodyChallengeMode(StrEnum):
    BOTH = "both"
    CLICK = "click"
    OFF = "off"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
