from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurveyAnswerInput")


@_attrs_define
class SurveyAnswerInput:
    """One answer; the field used follows the question's `kind`.

    Attributes:
        question_id (str):
        choice_id (str | Unset): A `choice` answer.
        choice_ids (list[str] | Unset): A `multi` answer.
        text_answer (str | Unset): A `text` answer.
        checked (bool | Unset): A `consent` answer.
    """

    question_id: str
    choice_id: str | Unset = UNSET
    choice_ids: list[str] | Unset = UNSET
    text_answer: str | Unset = UNSET
    checked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question_id = self.question_id

        choice_id = self.choice_id

        choice_ids: list[str] | Unset = UNSET
        if not isinstance(self.choice_ids, Unset):
            choice_ids = self.choice_ids

        text_answer = self.text_answer

        checked = self.checked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question_id": question_id,
            }
        )
        if choice_id is not UNSET:
            field_dict["choice_id"] = choice_id
        if choice_ids is not UNSET:
            field_dict["choice_ids"] = choice_ids
        if text_answer is not UNSET:
            field_dict["text_answer"] = text_answer
        if checked is not UNSET:
            field_dict["checked"] = checked

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        question_id = d.pop("question_id")

        choice_id = d.pop("choice_id", UNSET)

        choice_ids = cast(list[str], d.pop("choice_ids", UNSET))

        text_answer = d.pop("text_answer", UNSET)

        checked = d.pop("checked", UNSET)

        survey_answer_input = cls(
            question_id=question_id,
            choice_id=choice_id,
            choice_ids=choice_ids,
            text_answer=text_answer,
            checked=checked,
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
