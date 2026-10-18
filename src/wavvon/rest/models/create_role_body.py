from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRoleBody")


@_attrs_define
class CreateRoleBody:
    """
    Attributes:
        name (str):
        permissions (list[str]):
        priority (int):
        display_separately (bool | Unset):
        color (str | Unset):
        icon (str | Unset):
        category_id (str | Unset):
    """

    name: str
    permissions: list[str]
    priority: int
    display_separately: bool | Unset = UNSET
    color: str | Unset = UNSET
    icon: str | Unset = UNSET
    category_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions = self.permissions

        priority = self.priority

        display_separately = self.display_separately

        color = self.color

        icon = self.icon

        category_id = self.category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "permissions": permissions,
                "priority": priority,
            }
        )
        if display_separately is not UNSET:
            field_dict["display_separately"] = display_separately
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if category_id is not UNSET:
            field_dict["category_id"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        permissions = cast(list[str], d.pop("permissions"))

        priority = d.pop("priority")

        display_separately = d.pop("display_separately", UNSET)

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        category_id = d.pop("category_id", UNSET)

        create_role_body = cls(
            name=name,
            permissions=permissions,
            priority=priority,
            display_separately=display_separately,
            color=color,
            icon=icon,
            category_id=category_id,
        )

        create_role_body.additional_properties = d
        return create_role_body

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
