from enum import StrEnum


class PutPushSubscriptionBodyNotifyHub(StrEnum):
    ALL = "all"
    MENTIONS = "mentions"
    SILENT = "silent"

    def __str__(self) -> str:
        return str(self.value)
