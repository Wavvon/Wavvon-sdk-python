from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (str | Unset):
        conv_type (str | Unset):
        members (list[str] | Unset):
        created_at (int | Unset):
        last_activity_at (int | Unset):
    """

    id: str | Unset = UNSET
    conv_type: str | Unset = UNSET
    members: list[str] | Unset = UNSET
    created_at: int | Unset = UNSET
    last_activity_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conv_type = self.conv_type

        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        created_at = self.created_at

        last_activity_at = self.last_activity_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if conv_type is not UNSET:
            field_dict["conv_type"] = conv_type
        if members is not UNSET:
            field_dict["members"] = members
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conv_type = d.pop("conv_type", UNSET)

        members = cast(list[str], d.pop("members", UNSET))

        created_at = d.pop("created_at", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        conversation = cls(
            id=id,
            conv_type=conv_type,
            members=members,
            created_at=created_at,
            last_activity_at=last_activity_at,
        )

        conversation.additional_properties = d
        return conversation

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
