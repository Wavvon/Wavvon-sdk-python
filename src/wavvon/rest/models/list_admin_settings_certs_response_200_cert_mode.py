from enum import StrEnum


class ListAdminSettingsCertsResponse200CertMode(StrEnum):
    ANY = "any"
    NONE = "none"
    TRUSTED = "trusted"

    def __str__(self) -> str:
        return str(self.value)
