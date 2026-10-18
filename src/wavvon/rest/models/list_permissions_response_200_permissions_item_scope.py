from enum import Enum


class ListPermissionsResponse200PermissionsItemScope(str, Enum):
    HUB = "hub"
    HUB_AND_CHANNEL = "hub_and_channel"

    def __str__(self) -> str:
        return str(self.value)
