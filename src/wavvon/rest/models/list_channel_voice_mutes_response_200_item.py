from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListChannelVoiceMutesResponse200Item")


@_attrs_define
class ListChannelVoiceMutesResponse200Item:
    """
    Attributes:
        channel_id (str | Unset):
        pubkey (str | Unset):
        muted_by (str | Unset):
        muted_at (str | Unset):
    """

    channel_id: str | Unset = UNSET
    pubkey: str | Unset = UNSET
    muted_by: str | Unset = UNSET
    muted_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        pubkey = self.pubkey

        muted_by = self.muted_by

        muted_at = self.muted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if muted_by is not UNSET:
            field_dict["muted_by"] = muted_by
        if muted_at is not UNSET:
            field_dict["muted_at"] = muted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        muted_by = d.pop("muted_by", UNSET)

        muted_at = d.pop("muted_at", UNSET)

        list_channel_voice_mutes_response_200_item = cls(
            channel_id=channel_id,
            pubkey=pubkey,
            muted_by=muted_by,
            muted_at=muted_at,
        )

        list_channel_voice_mutes_response_200_item.additional_properties = d
        return list_channel_voice_mutes_response_200_item

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
