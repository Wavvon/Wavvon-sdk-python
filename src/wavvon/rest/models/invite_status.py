from enum import StrEnum


class InviteStatus(StrEnum):
    EXPIRED = "expired"
    LIVE = "live"
    USED_UP = "used_up"

    def __str__(self) -> str:
        return str(self.value)
