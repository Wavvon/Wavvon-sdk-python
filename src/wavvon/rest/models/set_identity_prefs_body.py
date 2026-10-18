from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetIdentityPrefsBody")


@_attrs_define
class SetIdentityPrefsBody:
    """
    Attributes:
        master_pubkey (str):
        blob_version (int):
        ciphertext_hex (str):
        signature (str):
    """

    master_pubkey: str
    blob_version: int
    ciphertext_hex: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        blob_version = self.blob_version

        ciphertext_hex = self.ciphertext_hex

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_pubkey": master_pubkey,
                "blob_version": blob_version,
                "ciphertext_hex": ciphertext_hex,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey")

        blob_version = d.pop("blob_version")

        ciphertext_hex = d.pop("ciphertext_hex")

        signature = d.pop("signature")

        set_identity_prefs_body = cls(
            master_pubkey=master_pubkey,
            blob_version=blob_version,
            ciphertext_hex=ciphertext_hex,
            signature=signature,
        )

        set_identity_prefs_body.additional_properties = d
        return set_identity_prefs_body

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
