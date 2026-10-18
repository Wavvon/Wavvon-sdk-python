from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetChannelMyPermissionsResponse200")


@_attrs_define
class GetChannelMyPermissionsResponse200:
    """
    Attributes:
        channel_id (str | Unset):
        permissions (list[str] | Unset):
        is_admin (bool | Unset):
    """

    channel_id: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    is_admin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        is_admin = self.is_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        is_admin = d.pop("is_admin", UNSET)

        get_channel_my_permissions_response_200 = cls(
            channel_id=channel_id,
            permissions=permissions,
            is_admin=is_admin,
        )

        get_channel_my_permissions_response_200.additional_properties = d
        return get_channel_my_permissions_response_200

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
