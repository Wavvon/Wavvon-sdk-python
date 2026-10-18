from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListRecoveryRequestsResponse200Item")


@_attrs_define
class ListRecoveryRequestsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        new_pubkey (str | Unset):
        status (str | Unset):
        created_at (int | Unset):
        attestation_count (int | Unset):
        threshold (int | Unset):
    """

    id: str | Unset = UNSET
    new_pubkey: str | Unset = UNSET
    status: str | Unset = UNSET
    created_at: int | Unset = UNSET
    attestation_count: int | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        new_pubkey = self.new_pubkey

        status = self.status

        created_at = self.created_at

        attestation_count = self.attestation_count

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if new_pubkey is not UNSET:
            field_dict["new_pubkey"] = new_pubkey
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if attestation_count is not UNSET:
            field_dict["attestation_count"] = attestation_count
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        new_pubkey = d.pop("new_pubkey", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("created_at", UNSET)

        attestation_count = d.pop("attestation_count", UNSET)

        threshold = d.pop("threshold", UNSET)

        list_recovery_requests_response_200_item = cls(
            id=id,
            new_pubkey=new_pubkey,
            status=status,
            created_at=created_at,
            attestation_count=attestation_count,
            threshold=threshold,
        )

        list_recovery_requests_response_200_item.additional_properties = d
        return list_recovery_requests_response_200_item

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
