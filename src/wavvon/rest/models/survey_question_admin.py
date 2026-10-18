from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.survey_choice_admin import SurveyChoiceAdmin


T = TypeVar("T", bound="SurveyQuestionAdmin")


@_attrs_define
class SurveyQuestionAdmin:
    """
    Attributes:
        id (str):
        prompt (str):
        kind (str):
        required (bool):
        display_order (int):
        choices (list[SurveyChoiceAdmin] | Unset):
    """

    id: str
    prompt: str
    kind: str
    required: bool
    display_order: int
    choices: list[SurveyChoiceAdmin] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        prompt = self.prompt

        kind = self.kind

        required = self.required

        display_order = self.display_order

        choices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item = choices_item_data.to_dict()
                choices.append(choices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "prompt": prompt,
                "kind": kind,
                "required": required,
                "display_order": display_order,
            }
        )
        if choices is not UNSET:
            field_dict["choices"] = choices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.survey_choice_admin import SurveyChoiceAdmin

        d = dict(src_dict)
        id = d.pop("id")

        prompt = d.pop("prompt")

        kind = d.pop("kind")

        required = d.pop("required")

        display_order = d.pop("display_order")

        _choices = d.pop("choices", UNSET)
        choices: list[SurveyChoiceAdmin] | Unset = UNSET
        if _choices is not UNSET:
            choices = []
            for choices_item_data in _choices:
                choices_item = SurveyChoiceAdmin.from_dict(choices_item_data)

                choices.append(choices_item)

        survey_question_admin = cls(
            id=id,
            prompt=prompt,
            kind=kind,
            required=required,
            display_order=display_order,
            choices=choices,
        )

        survey_question_admin.additional_properties = d
        return survey_question_admin

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
