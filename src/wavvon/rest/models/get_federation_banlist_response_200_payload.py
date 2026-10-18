from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_federation_banlist_response_200_payload_entries_item import (
        GetFederationBanlistResponse200PayloadEntriesItem,
    )


T = TypeVar("T", bound="GetFederationBanlistResponse200Payload")


@_attrs_define
class GetFederationBanlistResponse200Payload:
    """
    Attributes:
        issuer_pubkey (str | Unset):
        issued_at (int | Unset):
        entries (list[GetFederationBanlistResponse200PayloadEntriesItem] | Unset):
    """

    issuer_pubkey: str | Unset = UNSET
    issued_at: int | Unset = UNSET
    entries: list[GetFederationBanlistResponse200PayloadEntriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer_pubkey = self.issuer_pubkey

        issued_at = self.issued_at

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer_pubkey is not UNSET:
            field_dict["issuer_pubkey"] = issuer_pubkey
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_federation_banlist_response_200_payload_entries_item import (
            GetFederationBanlistResponse200PayloadEntriesItem,
        )

        d = dict(src_dict)
        issuer_pubkey = d.pop("issuer_pubkey", UNSET)

        issued_at = d.pop("issued_at", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[GetFederationBanlistResponse200PayloadEntriesItem] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = (
                    GetFederationBanlistResponse200PayloadEntriesItem.from_dict(
                        entries_item_data
                    )
                )

                entries.append(entries_item)

        get_federation_banlist_response_200_payload = cls(
            issuer_pubkey=issuer_pubkey,
            issued_at=issued_at,
            entries=entries,
        )

        get_federation_banlist_response_200_payload.additional_properties = d
        return get_federation_banlist_response_200_payload

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
