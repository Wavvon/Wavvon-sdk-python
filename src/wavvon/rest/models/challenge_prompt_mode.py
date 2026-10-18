from enum import Enum


class ChallengePromptMode(str, Enum):
    BOTH = "both"
    CLICK = "click"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
