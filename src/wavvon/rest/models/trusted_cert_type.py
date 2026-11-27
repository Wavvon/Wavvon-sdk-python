from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrustedCertType")


@_attrs_define
class TrustedCertType:
    """
    Attributes:
        issuer (str): Issuer hub pubkey.
        cert_type (str): Type id in that hub's catalogue.
    """

    issuer: str
    cert_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        cert_type = self.cert_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer": issuer,
                "cert_type": cert_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issuer = d.pop("issuer")

        cert_type = d.pop("cert_type")

        trusted_cert_type = cls(
            issuer=issuer,
            cert_type=cert_type,
        )

        trusted_cert_type.additional_properties = d
        return trusted_cert_type

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
