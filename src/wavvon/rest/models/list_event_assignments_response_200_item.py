from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEventAssignmentsResponse200Item")


@_attrs_define
class ListEventAssignmentsResponse200Item:
    """
    Attributes:
        user_pubkey (str | Unset):
        target_channel_id (str | Unset):
        assigned_by (str | Unset):
        created_at (int | Unset):
        voice_only (bool | Unset): Computed per row, not stored: the member lacks `read_messages` on the target, so a
            move would land them in voice-only presence. The client cannot see another member's permissions, so the hub
            resolves it.
    """

    user_pubkey: str | Unset = UNSET
    target_channel_id: str | Unset = UNSET
    assigned_by: str | Unset = UNSET
    created_at: int | Unset = UNSET
    voice_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_pubkey = self.user_pubkey

        target_channel_id = self.target_channel_id

        assigned_by = self.assigned_by

        created_at = self.created_at

        voice_only = self.voice_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_pubkey is not UNSET:
            field_dict["user_pubkey"] = user_pubkey
        if target_channel_id is not UNSET:
            field_dict["target_channel_id"] = target_channel_id
        if assigned_by is not UNSET:
            field_dict["assigned_by"] = assigned_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if voice_only is not UNSET:
            field_dict["voice_only"] = voice_only

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_pubkey = d.pop("user_pubkey", UNSET)

        target_channel_id = d.pop("target_channel_id", UNSET)

        assigned_by = d.pop("assigned_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        voice_only = d.pop("voice_only", UNSET)

        list_event_assignments_response_200_item = cls(
            user_pubkey=user_pubkey,
            target_channel_id=target_channel_id,
            assigned_by=assigned_by,
            created_at=created_at,
            voice_only=voice_only,
        )

        list_event_assignments_response_200_item.additional_properties = d
        return list_event_assignments_response_200_item

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
