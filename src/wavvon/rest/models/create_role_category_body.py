from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRoleCategoryBody")


@_attrs_define
class CreateRoleCategoryBody:
    """
    Attributes:
        name (str):
        color (str | Unset): ^#[0-9a-fA-F]{6}$
        icon (str | Unset): Single emoji grapheme, max 16 bytes
        position (int | Unset):  Default: 0.
    """

    name: str
    color: str | Unset = UNSET
    icon: str | Unset = UNSET
    position: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        color = self.color

        icon = self.icon

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        position = d.pop("position", UNSET)

        create_role_category_body = cls(
            name=name,
            color=color,
            icon=icon,
            position=position,
        )

        create_role_category_body.additional_properties = d
        return create_role_category_body

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
