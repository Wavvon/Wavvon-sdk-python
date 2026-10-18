from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SurveyChoiceAdmin")


@_attrs_define
class SurveyChoiceAdmin:
    """
    Attributes:
        id (str):
        label (str):
        display_order (int):
        role_ids (list[str]):
    """

    id: str
    label: str
    display_order: int
    role_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        display_order = self.display_order

        role_ids = self.role_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "display_order": display_order,
                "role_ids": role_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        display_order = d.pop("display_order")

        role_ids = cast(list[str], d.pop("role_ids"))

        survey_choice_admin = cls(
            id=id,
            label=label,
            display_order=display_order,
            role_ids=role_ids,
        )

        survey_choice_admin.additional_properties = d
        return survey_choice_admin

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
