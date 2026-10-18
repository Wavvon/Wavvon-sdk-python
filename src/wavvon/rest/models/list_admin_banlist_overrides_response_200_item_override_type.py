from enum import Enum


class ListAdminBanlistOverridesResponse200ItemOverrideType(str, Enum):
    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"

    def __str__(self) -> str:
        return str(self.value)
