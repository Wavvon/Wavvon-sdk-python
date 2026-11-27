from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProgramBadgeBody")


@_attrs_define
class CreateProgramBadgeBody:
    """
    Attributes:
        name (str):
        icon (str | Unset):
        description (str | Unset):
        declared_rule (str | Unset): Up to 280 chars
        levels (list[str] | Unset): Level names in order; one level when absent.
    """

    name: str
    icon: str | Unset = UNSET
    description: str | Unset = UNSET
    declared_rule: str | Unset = UNSET
    levels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon = self.icon

        description = self.description

        declared_rule = self.declared_rule

        levels: list[str] | Unset = UNSET
        if not isinstance(self.levels, Unset):
            levels = self.levels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if declared_rule is not UNSET:
            field_dict["declared_rule"] = declared_rule
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        icon = d.pop("icon", UNSET)

        description = d.pop("description", UNSET)

        declared_rule = d.pop("declared_rule", UNSET)

        levels = cast(list[str], d.pop("levels", UNSET))

        create_program_badge_body = cls(
            name=name,
            icon=icon,
            description=description,
            declared_rule=declared_rule,
            levels=levels,
        )

        create_program_badge_body.additional_properties = d
        return create_program_badge_body

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
