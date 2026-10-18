from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateIdentityDesignationBody")


@_attrs_define
class CreateIdentityDesignationBody:
    """
    Attributes:
        master_pubkey (str):
        hubs (list[str]):
        issued_at (int):
        sequence (int):
        signature (str):
    """

    master_pubkey: str
    hubs: list[str]
    issued_at: int
    sequence: int
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_pubkey = self.master_pubkey

        hubs = self.hubs

        issued_at = self.issued_at

        sequence = self.sequence

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_pubkey": master_pubkey,
                "hubs": hubs,
                "issued_at": issued_at,
                "sequence": sequence,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        master_pubkey = d.pop("master_pubkey")

        hubs = cast(list[str], d.pop("hubs"))

        issued_at = d.pop("issued_at")

        sequence = d.pop("sequence")

        signature = d.pop("signature")

        create_identity_designation_body = cls(
            master_pubkey=master_pubkey,
            hubs=hubs,
            issued_at=issued_at,
            sequence=sequence,
            signature=signature,
        )

        create_identity_designation_body.additional_properties = d
        return create_identity_designation_body

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
