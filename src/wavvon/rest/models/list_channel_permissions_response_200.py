from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_channel_permissions_response_200_roles_item import (
        ListChannelPermissionsResponse200RolesItem,
    )


T = TypeVar("T", bound="ListChannelPermissionsResponse200")


@_attrs_define
class ListChannelPermissionsResponse200:
    """
    Attributes:
        channel_id (str | Unset):
        roles (list[ListChannelPermissionsResponse200RolesItem] | Unset):
    """

    channel_id: str | Unset = UNSET
    roles: list[ListChannelPermissionsResponse200RolesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_channel_permissions_response_200_roles_item import (
            ListChannelPermissionsResponse200RolesItem,
        )

        d = dict(src_dict)
        channel_id = d.pop("channel_id", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[ListChannelPermissionsResponse200RolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = ListChannelPermissionsResponse200RolesItem.from_dict(
                    roles_item_data
                )

                roles.append(roles_item)

        list_channel_permissions_response_200 = cls(
            channel_id=channel_id,
            roles=roles,
        )

        list_channel_permissions_response_200.additional_properties = d
        return list_channel_permissions_response_200

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
