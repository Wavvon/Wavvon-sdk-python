from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rotate_recovery_key_response_201_status import (
    RotateRecoveryKeyResponse201Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RotateRecoveryKeyResponse201")


@_attrs_define
class RotateRecoveryKeyResponse201:
    """
    Attributes:
        id (str | Unset):
        old_pubkey (str | Unset):
        new_pubkey (str | Unset):
        status (RotateRecoveryKeyResponse201Status | Unset):
        created_at (int | Unset):
        attestation_count (int | Unset):
    """

    id: str | Unset = UNSET
    old_pubkey: str | Unset = UNSET
    new_pubkey: str | Unset = UNSET
    status: RotateRecoveryKeyResponse201Status | Unset = UNSET
    created_at: int | Unset = UNSET
    attestation_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        old_pubkey = self.old_pubkey

        new_pubkey = self.new_pubkey

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_at = self.created_at

        attestation_count = self.attestation_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if old_pubkey is not UNSET:
            field_dict["old_pubkey"] = old_pubkey
        if new_pubkey is not UNSET:
            field_dict["new_pubkey"] = new_pubkey
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if attestation_count is not UNSET:
            field_dict["attestation_count"] = attestation_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        old_pubkey = d.pop("old_pubkey", UNSET)

        new_pubkey = d.pop("new_pubkey", UNSET)

        _status = d.pop("status", UNSET)
        status: RotateRecoveryKeyResponse201Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RotateRecoveryKeyResponse201Status(_status)

        created_at = d.pop("created_at", UNSET)

        attestation_count = d.pop("attestation_count", UNSET)

        rotate_recovery_key_response_201 = cls(
            id=id,
            old_pubkey=old_pubkey,
            new_pubkey=new_pubkey,
            status=status,
            created_at=created_at,
            attestation_count=attestation_count,
        )

        rotate_recovery_key_response_201.additional_properties = d
        return rotate_recovery_key_response_201

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
