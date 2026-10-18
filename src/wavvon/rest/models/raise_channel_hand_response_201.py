from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RaiseChannelHandResponse201")


@_attrs_define
class RaiseChannelHandResponse201:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        pubkey (str | Unset):
        requested_at (str | Unset):
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    pubkey: str | Unset = UNSET
    requested_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        pubkey = self.pubkey

        requested_at = self.requested_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        requested_at = d.pop("requested_at", UNSET)

        raise_channel_hand_response_201 = cls(
            id=id,
            channel_id=channel_id,
            pubkey=pubkey,
            requested_at=requested_at,
        )

        raise_channel_hand_response_201.additional_properties = d
        return raise_channel_hand_response_201

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
