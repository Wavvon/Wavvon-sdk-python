from enum import Enum


class InviteStatus(str, Enum):
    EXPIRED = "expired"
    LIVE = "live"
    USED_UP = "used_up"

    def __str__(self) -> str:
        return str(self.value)
