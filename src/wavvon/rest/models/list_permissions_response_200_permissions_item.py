from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_permissions_response_200_permissions_item_scope import (
    ListPermissionsResponse200PermissionsItemScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListPermissionsResponse200PermissionsItem")


@_attrs_define
class ListPermissionsResponse200PermissionsItem:
    """
    Attributes:
        id (str | Unset):  Example: moderation.ban.permanent.
        scope (ListPermissionsResponse200PermissionsItemScope | Unset): `hub_and_channel` may also be set as a channel
            overwrite. Offering a `hub` entry there is a 400.
        group (str | Unset): Dotted prefix, for grouping without re-splitting the id. Example: moderation.
    """

    id: str | Unset = UNSET
    scope: ListPermissionsResponse200PermissionsItemScope | Unset = UNSET
    group: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ListPermissionsResponse200PermissionsItemScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ListPermissionsResponse200PermissionsItemScope(_scope)

        group = d.pop("group", UNSET)

        list_permissions_response_200_permissions_item = cls(
            id=id,
            scope=scope,
            group=group,
        )

        list_permissions_response_200_permissions_item.additional_properties = d
        return list_permissions_response_200_permissions_item

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
