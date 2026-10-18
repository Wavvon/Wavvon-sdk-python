from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListRecoveryContactsResponse200ContactsItem")


@_attrs_define
class ListRecoveryContactsResponse200ContactsItem:
    """
    Attributes:
        pubkey (str | Unset):
        added_at (int | Unset):
    """

    pubkey: str | Unset = UNSET
    added_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pubkey = self.pubkey

        added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if added_at is not UNSET:
            field_dict["added_at"] = added_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pubkey = d.pop("pubkey", UNSET)

        added_at = d.pop("added_at", UNSET)

        list_recovery_contacts_response_200_contacts_item = cls(
            pubkey=pubkey,
            added_at=added_at,
        )

        list_recovery_contacts_response_200_contacts_item.additional_properties = d
        return list_recovery_contacts_response_200_contacts_item

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
