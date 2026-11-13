from enum import StrEnum


class GetWidgetPageTheme(StrEnum):
    DARK = "dark"
    LIGHT = "light"

    def __str__(self) -> str:
        return str(self.value)
