from enum import StrEnum


class GetModerationHistoryResponse200EntriesItemPolicy(StrEnum):
    HARD_REJECT = "hard-reject"
    SOFT_FLAG = "soft-flag"

    def __str__(self) -> str:
        return str(self.value)
