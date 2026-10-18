from enum import StrEnum


class ListAdminBanlistSourcesResponse200ItemPolicy(StrEnum):
    HARD_REJECT = "hard-reject"
    SOFT_FLAG = "soft-flag"

    def __str__(self) -> str:
        return str(self.value)
