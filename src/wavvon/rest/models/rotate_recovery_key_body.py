from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attestation_input import AttestationInput


T = TypeVar("T", bound="RotateRecoveryKeyBody")


@_attrs_define
class RotateRecoveryKeyBody:
    """
    Attributes:
        old_pubkey (str):
        new_pubkey (str):
        new_key_signature (str):
        reason (str | Unset):
        attestations (list[AttestationInput] | Unset):
    """

    old_pubkey: str
    new_pubkey: str
    new_key_signature: str
    reason: str | Unset = UNSET
    attestations: list[AttestationInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_pubkey = self.old_pubkey

        new_pubkey = self.new_pubkey

        new_key_signature = self.new_key_signature

        reason = self.reason

        attestations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attestations, Unset):
            attestations = []
            for attestations_item_data in self.attestations:
                attestations_item = attestations_item_data.to_dict()
                attestations.append(attestations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_pubkey": old_pubkey,
                "new_pubkey": new_pubkey,
                "new_key_signature": new_key_signature,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if attestations is not UNSET:
            field_dict["attestations"] = attestations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attestation_input import AttestationInput

        d = dict(src_dict)
        old_pubkey = d.pop("old_pubkey")

        new_pubkey = d.pop("new_pubkey")

        new_key_signature = d.pop("new_key_signature")

        reason = d.pop("reason", UNSET)

        _attestations = d.pop("attestations", UNSET)
        attestations: list[AttestationInput] | Unset = UNSET
        if _attestations is not UNSET:
            attestations = []
            for attestations_item_data in _attestations:
                attestations_item = AttestationInput.from_dict(attestations_item_data)

                attestations.append(attestations_item)

        rotate_recovery_key_body = cls(
            old_pubkey=old_pubkey,
            new_pubkey=new_pubkey,
            new_key_signature=new_key_signature,
            reason=reason,
            attestations=attestations,
        )

        rotate_recovery_key_body.additional_properties = d
        return rotate_recovery_key_body

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
