from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetIdentityDhKeyBody")


@_attrs_define
class SetIdentityDhKeyBody:
    """
    Attributes:
        dh_pubkey_hex (str):
        signature_hex (str):
    """

    dh_pubkey_hex: str
    signature_hex: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dh_pubkey_hex = self.dh_pubkey_hex

        signature_hex = self.signature_hex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dh_pubkey_hex": dh_pubkey_hex,
                "signature_hex": signature_hex,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dh_pubkey_hex = d.pop("dh_pubkey_hex")

        signature_hex = d.pop("signature_hex")

        set_identity_dh_key_body = cls(
            dh_pubkey_hex=dh_pubkey_hex,
            signature_hex=signature_hex,
        )

        set_identity_dh_key_body.additional_properties = d
        return set_identity_dh_key_body

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
