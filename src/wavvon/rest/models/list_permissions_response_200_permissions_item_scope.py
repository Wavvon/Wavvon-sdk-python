from enum import StrEnum


class ListPermissionsResponse200PermissionsItemScope(StrEnum):
    HUB = "hub"
    HUB_AND_CHANNEL = "hub_and_channel"

    def __str__(self) -> str:
        return str(self.value)
