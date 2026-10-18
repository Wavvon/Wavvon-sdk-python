from enum import StrEnum


class ListEventsResponse200ItemMyRsvp(StrEnum):
    GOING = "going"
    MAYBE = "maybe"
    NOT_GOING = "not_going"

    def __str__(self) -> str:
        return str(self.value)
