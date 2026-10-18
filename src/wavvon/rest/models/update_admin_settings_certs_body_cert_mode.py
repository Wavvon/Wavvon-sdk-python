from enum import Enum


class UpdateAdminSettingsCertsBodyCertMode(str, Enum):
    ANY = "any"
    NONE = "none"
    TRUSTED = "trusted"

    def __str__(self) -> str:
        return str(self.value)
