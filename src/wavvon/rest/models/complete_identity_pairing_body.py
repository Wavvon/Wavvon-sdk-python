from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="CompleteIdentityPairingBody")


@_attrs_define
class CompleteIdentityPairingBody:
    """
    Attributes:
        pairing_token (str):
        cert (SubkeyCert):
        wrapped_blob_key_hex (str):
        wrapped_dh_seed_hex (str | Unset):
    """

    pairing_token: str
    cert: SubkeyCert
    wrapped_blob_key_hex: str
    wrapped_dh_seed_hex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pairing_token = self.pairing_token

        cert = self.cert.to_dict()

        wrapped_blob_key_hex = self.wrapped_blob_key_hex

        wrapped_dh_seed_hex = self.wrapped_dh_seed_hex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pairing_token": pairing_token,
                "cert": cert,
                "wrapped_blob_key_hex": wrapped_blob_key_hex,
            }
        )
        if wrapped_dh_seed_hex is not UNSET:
            field_dict["wrapped_dh_seed_hex"] = wrapped_dh_seed_hex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        pairing_token = d.pop("pairing_token")

        cert = SubkeyCert.from_dict(d.pop("cert"))

        wrapped_blob_key_hex = d.pop("wrapped_blob_key_hex")

        wrapped_dh_seed_hex = d.pop("wrapped_dh_seed_hex", UNSET)

        complete_identity_pairing_body = cls(
            pairing_token=pairing_token,
            cert=cert,
            wrapped_blob_key_hex=wrapped_blob_key_hex,
            wrapped_dh_seed_hex=wrapped_dh_seed_hex,
        )

        complete_identity_pairing_body.additional_properties = d
        return complete_identity_pairing_body

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
