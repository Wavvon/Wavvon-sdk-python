from enum import StrEnum


class BadgeDefRequestRule(StrEnum):
    ACTIVE_DAYS = "active_days"
    MANUAL = "manual"
    MEMBER_AGE = "member_age"
    MESSAGES = "messages"
    ONLINE = "online"
    ROLE_HELD = "role_held"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
