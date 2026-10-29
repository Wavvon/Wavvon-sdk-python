from enum import StrEnum


class ListAdminSurveyResponsesStatus(StrEnum):
    ALL = "all"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
