from enum import StrEnum


class WidgetSettingsMode(StrEnum):
    COUNTS = "counts"
    NAMES = "names"
    OFF = "off"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
