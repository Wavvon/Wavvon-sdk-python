from enum import StrEnum


class ListMeEventsResponse410Type(StrEnum):
    REPLAY_UNAVAILABLE = "replay_unavailable"

    def __str__(self) -> str:
        return str(self.value)
