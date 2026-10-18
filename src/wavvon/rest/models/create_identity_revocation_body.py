from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateIdentityRevocationBody")


@_attrs_define
class CreateIdentityRevocationBody:
    """
    Attributes:
        master_pubkey (str):
        subkey_pubkey (str):
        revoked_at (int):
        signature (str):
    """

    master_pubkey: str
    subkey_pubkey: str
    revoked_at: int
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        subkey_pubkey = self.subkey_pubkey

        revoked_at = self.revoked_at

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_pubkey": master_pubkey,
                "subkey_pubkey": subkey_pubkey,
                "revoked_at": revoked_at,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey")

        subkey_pubkey = d.pop("subkey_pubkey")

        revoked_at = d.pop("revoked_at")

        signature = d.pop("signature")

        create_identity_revocation_body = cls(
            master_pubkey=master_pubkey,
            subkey_pubkey=subkey_pubkey,
            revoked_at=revoked_at,
            signature=signature,
        )

        create_identity_revocation_body.additional_properties = d
        return create_identity_revocation_body

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
