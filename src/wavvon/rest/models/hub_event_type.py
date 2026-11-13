from enum import StrEnum


class HubEventType(StrEnum):
    HUB_EVENT = "hub_event"

    def __str__(self) -> str:
        return str(self.value)
