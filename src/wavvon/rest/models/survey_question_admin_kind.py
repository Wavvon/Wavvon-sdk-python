from enum import StrEnum


class SurveyQuestionAdminKind(StrEnum):
    CHOICE = "choice"
    CONSENT = "consent"
    MULTI = "multi"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
