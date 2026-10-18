from enum import Enum


class ReviewAdminReportBodyAction(str, Enum):
    BAN_USER = "ban_user"
    DELETE_MESSAGE = "delete_message"
    DISMISS = "dismiss"

    def __str__(self) -> str:
        return str(self.value)
