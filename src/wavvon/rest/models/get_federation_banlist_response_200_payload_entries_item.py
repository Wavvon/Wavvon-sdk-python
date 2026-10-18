from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFederationBanlistResponse200PayloadEntriesItem")


@_attrs_define
class GetFederationBanlistResponse200PayloadEntriesItem:
    """
    Attributes:
        master_pubkey (str | Unset):
        reason (None | str | Unset):
        added_at (int | Unset):
    """

    master_pubkey: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    added_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if master_pubkey is not UNSET:
            field_dict["master_pubkey"] = master_pubkey
        if reason is not UNSET:
            field_dict["reason"] = reason
        if added_at is not UNSET:
            field_dict["added_at"] = added_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        added_at = d.pop("added_at", UNSET)

        get_federation_banlist_response_200_payload_entries_item = cls(
            master_pubkey=master_pubkey,
            reason=reason,
            added_at=added_at,
        )

        get_federation_banlist_response_200_payload_entries_item.additional_properties = d
        return get_federation_banlist_response_200_payload_entries_item

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
