from enum import StrEnum


class UpdateAdminSettingsCertsBodyCertMode(StrEnum):
    ANY = "any"
    NONE = "none"
    TRUSTED = "trusted"

    def __str__(self) -> str:
        return str(self.value)
