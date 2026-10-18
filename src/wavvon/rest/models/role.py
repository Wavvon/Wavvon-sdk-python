from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        permissions (list[str] | Unset):
        priority (int | Unset):
        display_separately (bool | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    priority: int | Unset = UNSET
    display_separately: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        priority = self.priority

        display_separately = self.display_separately

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if priority is not UNSET:
            field_dict["priority"] = priority
        if display_separately is not UNSET:
            field_dict["display_separately"] = display_separately

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        priority = d.pop("priority", UNSET)

        display_separately = d.pop("display_separately", UNSET)

        role = cls(
            id=id,
            name=name,
            permissions=permissions,
            priority=priority,
            display_separately=display_separately,
        )

        role.additional_properties = d
        return role

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
