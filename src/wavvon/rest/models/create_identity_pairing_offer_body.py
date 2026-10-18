from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateIdentityPairingOfferBody")


@_attrs_define
class CreateIdentityPairingOfferBody:
    """
    Attributes:
        master_pubkey (str):
        home_hubs (list[str]):
        pairing_token (str):
        issued_at (int):
        expires_at (int):
        signature (str):
    """

    master_pubkey: str
    home_hubs: list[str]
    pairing_token: str
    issued_at: int
    expires_at: int
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        home_hubs = self.home_hubs

        pairing_token = self.pairing_token

        issued_at = self.issued_at

        expires_at = self.expires_at

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_pubkey": master_pubkey,
                "home_hubs": home_hubs,
                "pairing_token": pairing_token,
                "issued_at": issued_at,
                "expires_at": expires_at,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey")

        home_hubs = cast(list[str], d.pop("home_hubs"))

        pairing_token = d.pop("pairing_token")

        issued_at = d.pop("issued_at")

        expires_at = d.pop("expires_at")

        signature = d.pop("signature")

        create_identity_pairing_offer_body = cls(
            master_pubkey=master_pubkey,
            home_hubs=home_hubs,
            pairing_token=pairing_token,
            issued_at=issued_at,
            expires_at=expires_at,
            signature=signature,
        )

        create_identity_pairing_offer_body.additional_properties = d
        return create_identity_pairing_offer_body

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
