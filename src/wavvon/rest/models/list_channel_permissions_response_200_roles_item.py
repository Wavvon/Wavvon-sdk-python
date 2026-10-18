from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_channel_permissions_response_200_roles_item_overwrites import (
        ListChannelPermissionsResponse200RolesItemOverwrites,
    )


T = TypeVar("T", bound="ListChannelPermissionsResponse200RolesItem")


@_attrs_define
class ListChannelPermissionsResponse200RolesItem:
    """
    Attributes:
        role_id (str | Unset):
        role_name (str | Unset):
        overwrites (ListChannelPermissionsResponse200RolesItemOverwrites | Unset):
        inherited (list[str] | Unset):
        effective (list[str] | Unset):
    """

    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    overwrites: ListChannelPermissionsResponse200RolesItemOverwrites | Unset = UNSET
    inherited: list[str] | Unset = UNSET
    effective: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        role_name = self.role_name

        overwrites: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overwrites, Unset):
            overwrites = self.overwrites.to_dict()

        inherited: list[str] | Unset = UNSET
        if not isinstance(self.inherited, Unset):
            inherited = self.inherited

        effective: list[str] | Unset = UNSET
        if not isinstance(self.effective, Unset):
            effective = self.effective

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if overwrites is not UNSET:
            field_dict["overwrites"] = overwrites
        if inherited is not UNSET:
            field_dict["inherited"] = inherited
        if effective is not UNSET:
            field_dict["effective"] = effective

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_channel_permissions_response_200_roles_item_overwrites import (
            ListChannelPermissionsResponse200RolesItemOverwrites,
        )

        d = dict(src_dict)
        role_id = d.pop("role_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        _overwrites = d.pop("overwrites", UNSET)
        overwrites: ListChannelPermissionsResponse200RolesItemOverwrites | Unset
        if isinstance(_overwrites, Unset):
            overwrites = UNSET
        else:
            overwrites = ListChannelPermissionsResponse200RolesItemOverwrites.from_dict(
                _overwrites
            )

        inherited = cast(list[str], d.pop("inherited", UNSET))

        effective = cast(list[str], d.pop("effective", UNSET))

        list_channel_permissions_response_200_roles_item = cls(
            role_id=role_id,
            role_name=role_name,
            overwrites=overwrites,
            inherited=inherited,
            effective=effective,
        )

        list_channel_permissions_response_200_roles_item.additional_properties = d
        return list_channel_permissions_response_200_roles_item

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
