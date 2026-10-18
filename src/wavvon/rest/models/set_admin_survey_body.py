from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.survey_question_admin import SurveyQuestionAdmin


T = TypeVar("T", bound="SetAdminSurveyBody")


@_attrs_define
class SetAdminSurveyBody:
    """
    Attributes:
        id (str):
        enabled (bool):
        questions (list[SurveyQuestionAdmin]):
    """

    id: str
    enabled: bool
    questions: list[SurveyQuestionAdmin]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        questions = []
        for questions_item_data in self.questions:
            questions_item = questions_item_data.to_dict()
            questions.append(questions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
                "questions": questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.survey_question_admin import SurveyQuestionAdmin

        d = dict(src_dict)
        id = d.pop("id")

        enabled = d.pop("enabled")

        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = SurveyQuestionAdmin.from_dict(questions_item_data)

            questions.append(questions_item)

        set_admin_survey_body = cls(
            id=id,
            enabled=enabled,
            questions=questions,
        )

        set_admin_survey_body.additional_properties = d
        return set_admin_survey_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
