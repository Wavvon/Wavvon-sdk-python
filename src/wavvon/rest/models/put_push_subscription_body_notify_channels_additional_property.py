from enum import StrEnum


class PutPushSubscriptionBodyNotifyChannelsAdditionalProperty(StrEnum):
    ALL = "all"
    MENTIONS = "mentions"
    SILENT = "silent"

    def __str__(self) -> str:
        return str(self.value)
