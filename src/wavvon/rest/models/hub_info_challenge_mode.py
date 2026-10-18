from enum import Enum


class HubInfoChallengeMode(str, Enum):
    BOTH = "both"
    CLICK = "click"
    OFF = "off"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
