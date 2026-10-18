from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_permissions_response_200_permissions_item import (
        ListPermissionsResponse200PermissionsItem,
    )


T = TypeVar("T", bound="ListPermissionsResponse200")


@_attrs_define
class ListPermissionsResponse200:
    """
    Attributes:
        permissions (list[ListPermissionsResponse200PermissionsItem] | Unset):
    """

    permissions: list[ListPermissionsResponse200PermissionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_permissions_response_200_permissions_item import (
            ListPermissionsResponse200PermissionsItem,
        )

        d = dict(src_dict)
        _permissions = d.pop("permissions", UNSET)
        permissions: list[ListPermissionsResponse200PermissionsItem] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = ListPermissionsResponse200PermissionsItem.from_dict(
                    permissions_item_data
                )

                permissions.append(permissions_item)

        list_permissions_response_200 = cls(
            permissions=permissions,
        )

        list_permissions_response_200.additional_properties = d
        return list_permissions_response_200

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
