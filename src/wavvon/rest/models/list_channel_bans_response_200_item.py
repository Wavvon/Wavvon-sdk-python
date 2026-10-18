from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListChannelBansResponse200Item")


@_attrs_define
class ListChannelBansResponse200Item:
    """
    Attributes:
        channel_id (str | Unset):
        pubkey (str | Unset):
        banned_by (str | Unset):
        reason (None | str | Unset):
        banned_at (int | Unset):
    """

    channel_id: str | Unset = UNSET
    pubkey: str | Unset = UNSET
    banned_by: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    banned_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        pubkey = self.pubkey

        banned_by = self.banned_by

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        banned_at = self.banned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if banned_by is not UNSET:
            field_dict["banned_by"] = banned_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if banned_at is not UNSET:
            field_dict["banned_at"] = banned_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        banned_by = d.pop("banned_by", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        banned_at = d.pop("banned_at", UNSET)

        list_channel_bans_response_200_item = cls(
            channel_id=channel_id,
            pubkey=pubkey,
            banned_by=banned_by,
            reason=reason,
            banned_at=banned_at,
        )

        list_channel_bans_response_200_item.additional_properties = d
        return list_channel_bans_response_200_item

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
