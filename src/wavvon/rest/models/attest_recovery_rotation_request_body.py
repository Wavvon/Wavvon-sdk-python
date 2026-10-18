from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttestRecoveryRotationRequestBody")


@_attrs_define
class AttestRecoveryRotationRequestBody:
    """
    Attributes:
        attester (str): Contact's public key
        signature (str): Ed25519 signature over the bundle
    """

    attester: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attester = self.attester

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attester": attester,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attester = d.pop("attester")

        signature = d.pop("signature")

        attest_recovery_rotation_request_body = cls(
            attester=attester,
            signature=signature,
        )

        attest_recovery_rotation_request_body.additional_properties = d
        return attest_recovery_rotation_request_body

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
