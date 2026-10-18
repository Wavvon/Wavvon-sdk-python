from enum import StrEnum


class ListAdminBanlistOverridesResponse200ItemOverrideType(StrEnum):
    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"

    def __str__(self) -> str:
        return str(self.value)
