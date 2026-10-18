from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRoleBody")


@_attrs_define
class CreateRoleBody:
    """
    Attributes:
        name (str):
        permissions (list[str] | Unset):
        priority (int | Unset):
        display_separately (bool | Unset):
    """

    name: str
    permissions: list[str] | Unset = UNSET
    priority: int | Unset = UNSET
    display_separately: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        priority = self.priority

        display_separately = self.display_separately

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
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
        name = d.pop("name")

        permissions = cast(list[str], d.pop("permissions", UNSET))

        priority = d.pop("priority", UNSET)

        display_separately = d.pop("display_separately", UNSET)

        create_role_body = cls(
            name=name,
            permissions=permissions,
            priority=priority,
            display_separately=display_separately,
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
