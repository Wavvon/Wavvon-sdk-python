from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_payload import CertPayload


T = TypeVar("T", bound="Certification")


@_attrs_define
class Certification:
    """Certification envelope (payload + hex Ed25519 hub signature).

    Attributes:
        payload (CertPayload | Unset): Canonical certification payload signed by the issuing hub.
        signature (str | Unset):
    """

    payload: CertPayload | Unset = UNSET
    signature: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cert_payload import CertPayload

        d = dict(src_dict)
        _payload = d.pop("payload", UNSET)
        payload: CertPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = CertPayload.from_dict(_payload)

        signature = d.pop("signature", UNSET)

        certification = cls(
            payload=payload,
            signature=signature,
        )

        certification.additional_properties = d
        return certification

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
