from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClaimIdentityPairingBody")


@_attrs_define
class ClaimIdentityPairingBody:
    """
    Attributes:
        pairing_token (str):
        subkey_pubkey (str):
        device_label (str):
        proof (str):
    """

    pairing_token: str
    subkey_pubkey: str
    device_label: str
    proof: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pairing_token = self.pairing_token

        subkey_pubkey = self.subkey_pubkey

        device_label = self.device_label

        proof = self.proof

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pairing_token": pairing_token,
                "subkey_pubkey": subkey_pubkey,
                "device_label": device_label,
                "proof": proof,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pairing_token = d.pop("pairing_token")

        subkey_pubkey = d.pop("subkey_pubkey")

        device_label = d.pop("device_label")

        proof = d.pop("proof")

        claim_identity_pairing_body = cls(
            pairing_token=pairing_token,
            subkey_pubkey=subkey_pubkey,
            device_label=device_label,
            proof=proof,
        )

        claim_identity_pairing_body.additional_properties = d
        return claim_identity_pairing_body

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
