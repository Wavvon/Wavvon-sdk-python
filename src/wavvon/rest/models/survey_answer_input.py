from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurveyAnswerInput")


@_attrs_define
class SurveyAnswerInput:
    """
    Attributes:
        question_id (str):
        choice_id (str | Unset):
        text_answer (str | Unset):
    """

    question_id: str
    choice_id: str | Unset = UNSET
    text_answer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question_id = self.question_id

        choice_id = self.choice_id

        text_answer = self.text_answer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question_id": question_id,
            }
        )
        if choice_id is not UNSET:
            field_dict["choice_id"] = choice_id
        if text_answer is not UNSET:
            field_dict["text_answer"] = text_answer

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        question_id = d.pop("question_id")

        choice_id = d.pop("choice_id", UNSET)

        text_answer = d.pop("text_answer", UNSET)

        survey_answer_input = cls(
            question_id=question_id,
            choice_id=choice_id,
            text_answer=text_answer,
        )

        survey_answer_input.additional_properties = d
        return survey_answer_input

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
