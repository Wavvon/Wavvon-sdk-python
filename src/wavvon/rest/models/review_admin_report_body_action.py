from enum import StrEnum


class ReviewAdminReportBodyAction(StrEnum):
    BAN_USER = "ban_user"
    DELETE_MESSAGE = "delete_message"
    DISMISS = "dismiss"

    def __str__(self) -> str:
        return str(self.value)
