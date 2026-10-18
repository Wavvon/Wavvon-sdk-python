from enum import StrEnum


class ChallengePromptMode(StrEnum):
    BOTH = "both"
    CLICK = "click"
    PUZZLE = "puzzle"

    def __str__(self) -> str:
        return str(self.value)
