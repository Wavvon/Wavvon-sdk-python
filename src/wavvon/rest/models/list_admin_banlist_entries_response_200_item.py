from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminBanlistEntriesResponse200Item")


@_attrs_define
class ListAdminBanlistEntriesResponse200Item:
    """
    Attributes:
        source_hub_pubkey (str | Unset):
        target_master_pubkey (str | Unset):
        reason (None | str | Unset):
        added_at (int | Unset):
        synced_at (int | Unset):
    """

    source_hub_pubkey: str | Unset = UNSET
    target_master_pubkey: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    added_at: int | Unset = UNSET
    synced_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_hub_pubkey = self.source_hub_pubkey

        target_master_pubkey = self.target_master_pubkey

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        added_at = self.added_at

        synced_at = self.synced_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_hub_pubkey is not UNSET:
            field_dict["source_hub_pubkey"] = source_hub_pubkey
        if target_master_pubkey is not UNSET:
            field_dict["target_master_pubkey"] = target_master_pubkey
        if reason is not UNSET:
            field_dict["reason"] = reason
        if added_at is not UNSET:
            field_dict["added_at"] = added_at
        if synced_at is not UNSET:
            field_dict["synced_at"] = synced_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_hub_pubkey = d.pop("source_hub_pubkey", UNSET)

        target_master_pubkey = d.pop("target_master_pubkey", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        added_at = d.pop("added_at", UNSET)

        synced_at = d.pop("synced_at", UNSET)

        list_admin_banlist_entries_response_200_item = cls(
            source_hub_pubkey=source_hub_pubkey,
            target_master_pubkey=target_master_pubkey,
            reason=reason,
            added_at=added_at,
            synced_at=synced_at,
        )

        list_admin_banlist_entries_response_200_item.additional_properties = d
        return list_admin_banlist_entries_response_200_item

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
