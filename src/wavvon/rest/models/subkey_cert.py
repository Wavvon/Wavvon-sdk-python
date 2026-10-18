from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubkeyCert")


@_attrs_define
class SubkeyCert:
    """
    Attributes:
        master_pubkey (str):
        subkey_pubkey (str):
        device_label (str):
        issued_at (int):
        signature (str):
        not_after (int | Unset):
        fallback_hubs (list[str] | Unset):
    """

    master_pubkey: str
    subkey_pubkey: str
    device_label: str
    issued_at: int
    signature: str
    not_after: int | Unset = UNSET
    fallback_hubs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        subkey_pubkey = self.subkey_pubkey

        device_label = self.device_label

        issued_at = self.issued_at

        signature = self.signature

        not_after = self.not_after

        fallback_hubs: list[str] | Unset = UNSET
        if not isinstance(self.fallback_hubs, Unset):
            fallback_hubs = self.fallback_hubs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_pubkey": master_pubkey,
                "subkey_pubkey": subkey_pubkey,
                "device_label": device_label,
                "issued_at": issued_at,
                "signature": signature,
            }
        )
        if not_after is not UNSET:
            field_dict["not_after"] = not_after
        if fallback_hubs is not UNSET:
            field_dict["fallback_hubs"] = fallback_hubs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey")

        subkey_pubkey = d.pop("subkey_pubkey")

        device_label = d.pop("device_label")

        issued_at = d.pop("issued_at")

        signature = d.pop("signature")

        not_after = d.pop("not_after", UNSET)

        fallback_hubs = cast(list[str], d.pop("fallback_hubs", UNSET))

        subkey_cert = cls(
            master_pubkey=master_pubkey,
            subkey_pubkey=subkey_pubkey,
            device_label=device_label,
            issued_at=issued_at,
            signature=signature,
            not_after=not_after,
            fallback_hubs=fallback_hubs,
        )

        subkey_cert.additional_properties = d
        return subkey_cert

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
