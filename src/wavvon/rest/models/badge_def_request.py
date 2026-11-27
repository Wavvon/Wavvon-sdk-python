from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.badge_def_request_rule import BadgeDefRequestRule
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_level import BadgeLevel


T = TypeVar("T", bound="BadgeDefRequest")


@_attrs_define
class BadgeDefRequest:
    """
    Attributes:
        name (str):
        rule (BadgeDefRequestRule):
        levels (list[BadgeLevel]):
        icon (str | Unset):
        description (str | Unset):
        role_id (str | Unset): Required by role_held.
        keep_while (bool | Unset): Held only while the condition is true; otherwise kept for good.
    """

    name: str
    rule: BadgeDefRequestRule
    levels: list[BadgeLevel]
    icon: str | Unset = UNSET
    description: str | Unset = UNSET
    role_id: str | Unset = UNSET
    keep_while: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rule = self.rule.value

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.to_dict()
            levels.append(levels_item)

        icon = self.icon

        description = self.description

        role_id = self.role_id

        keep_while = self.keep_while

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rule": rule,
                "levels": levels,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if keep_while is not UNSET:
            field_dict["keep_while"] = keep_while

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.badge_level import BadgeLevel

        d = dict(src_dict)
        name = d.pop("name")

        rule = BadgeDefRequestRule(d.pop("rule"))

        levels = []
        _levels = d.pop("levels")
        for levels_item_data in _levels:
            levels_item = BadgeLevel.from_dict(levels_item_data)

            levels.append(levels_item)

        icon = d.pop("icon", UNSET)

        description = d.pop("description", UNSET)

        role_id = d.pop("role_id", UNSET)

        keep_while = d.pop("keep_while", UNSET)

        badge_def_request = cls(
            name=name,
            rule=rule,
            levels=levels,
            icon=icon,
            description=description,
            role_id=role_id,
            keep_while=keep_while,
        )

        badge_def_request.additional_properties = d
        return badge_def_request

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
