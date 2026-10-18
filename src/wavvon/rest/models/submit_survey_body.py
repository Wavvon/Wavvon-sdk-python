from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.survey_answer_input import SurveyAnswerInput


T = TypeVar("T", bound="SubmitSurveyBody")


@_attrs_define
class SubmitSurveyBody:
    """
    Attributes:
        survey_id (str):
        answers (list[SurveyAnswerInput]):
    """

    survey_id: str
    answers: list[SurveyAnswerInput]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        survey_id = self.survey_id

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "survey_id": survey_id,
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.survey_answer_input import SurveyAnswerInput

        d = dict(src_dict)
        survey_id = d.pop("survey_id")

        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = SurveyAnswerInput.from_dict(answers_item_data)

            answers.append(answers_item)

        submit_survey_body = cls(
            survey_id=survey_id,
            answers=answers,
        )

        submit_survey_body.additional_properties = d
        return submit_survey_body

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
