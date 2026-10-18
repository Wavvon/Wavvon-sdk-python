from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAllianceManagersResponse200Item")


@_attrs_define
class ListAllianceManagersResponse200Item:
    """
    Attributes:
        alliance_id (str | Unset):
        role_id (str | Unset):
        role_name (str | Unset):
        granted_by (str | Unset):
        granted_at (int | Unset):
    """

    alliance_id: str | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    granted_by: str | Unset = UNSET
    granted_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alliance_id = self.alliance_id

        role_id = self.role_id

        role_name = self.role_name

        granted_by = self.granted_by

        granted_at = self.granted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alliance_id is not UNSET:
            field_dict["alliance_id"] = alliance_id
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if granted_by is not UNSET:
            field_dict["granted_by"] = granted_by
        if granted_at is not UNSET:
            field_dict["granted_at"] = granted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alliance_id = d.pop("alliance_id", UNSET)

        role_id = d.pop("role_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        granted_by = d.pop("granted_by", UNSET)

        granted_at = d.pop("granted_at", UNSET)

        list_alliance_managers_response_200_item = cls(
            alliance_id=alliance_id,
            role_id=role_id,
            role_name=role_name,
            granted_by=granted_by,
            granted_at=granted_at,
        )

        list_alliance_managers_response_200_item.additional_properties = d
        return list_alliance_managers_response_200_item

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
