from enum import StrEnum


class RsvpEventBodyStatus(StrEnum):
    GOING = "going"
    MAYBE = "maybe"
    NOT_GOING = "not_going"

    def __str__(self) -> str:
        return str(self.value)
