from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BeginWebauthnRegistrationBody")


@_attrs_define
class BeginWebauthnRegistrationBody:
    """
    Attributes:
        user_pubkey (str): Hex-encoded Ed25519 public key
        display_name (str | Unset):
    """

    user_pubkey: str
    display_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_pubkey = self.user_pubkey

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_pubkey": user_pubkey,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_pubkey = d.pop("user_pubkey")

        display_name = d.pop("display_name", UNSET)

        begin_webauthn_registration_body = cls(
            user_pubkey=user_pubkey,
            display_name=display_name,
        )

        begin_webauthn_registration_body.additional_properties = d
        return begin_webauthn_registration_body

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
