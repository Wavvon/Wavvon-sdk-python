from enum import Enum


class RsvpEventBodyStatus(str, Enum):
    GOING = "going"
    MAYBE = "maybe"
    NOT_GOING = "not_going"

    def __str__(self) -> str:
        return str(self.value)
