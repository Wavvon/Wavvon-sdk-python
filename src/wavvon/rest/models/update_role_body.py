from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRoleBody")


@_attrs_define
class UpdateRoleBody:
    """
    Attributes:
        name (str | Unset):
        permissions (list[str] | Unset):
        priority (int | Unset):
        display_separately (bool | Unset):
        color (None | str | Unset):
        icon (None | str | Unset):
        category_id (None | str | Unset):
    """

    name: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    priority: int | Unset = UNSET
    display_separately: bool | Unset = UNSET
    color: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        priority = self.priority

        display_separately = self.display_separately

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if priority is not UNSET:
            field_dict["priority"] = priority
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
        name = d.pop("name", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        priority = d.pop("priority", UNSET)

        display_separately = d.pop("display_separately", UNSET)

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        update_role_body = cls(
            name=name,
            permissions=permissions,
            priority=priority,
            display_separately=display_separately,
            color=color,
            icon=icon,
            category_id=category_id,
        )

        update_role_body.additional_properties = d
        return update_role_body

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
