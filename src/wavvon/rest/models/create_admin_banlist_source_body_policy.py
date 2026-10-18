from enum import Enum


class CreateAdminBanlistSourceBodyPolicy(str, Enum):
    HARD_REJECT = "hard-reject"
    SOFT_FLAG = "soft-flag"

    def __str__(self) -> str:
        return str(self.value)
