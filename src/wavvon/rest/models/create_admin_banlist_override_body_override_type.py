from enum import StrEnum


class CreateAdminBanlistOverrideBodyOverrideType(StrEnum):
    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"

    def __str__(self) -> str:
        return str(self.value)
