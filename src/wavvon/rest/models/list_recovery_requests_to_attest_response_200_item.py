from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListRecoveryRequestsToAttestResponse200Item")


@_attrs_define
class ListRecoveryRequestsToAttestResponse200Item:
    """
    Attributes:
        id (str | Unset):
        old_pubkey (str | Unset):
        new_pubkey (str | Unset):
        reason (None | str | Unset):
        created_at (int | Unset):
        attestation_count (int | Unset):
        threshold (int | Unset):
    """

    id: str | Unset = UNSET
    old_pubkey: str | Unset = UNSET
    new_pubkey: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    attestation_count: int | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        old_pubkey = self.old_pubkey

        new_pubkey = self.new_pubkey

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        created_at = self.created_at

        attestation_count = self.attestation_count

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if old_pubkey is not UNSET:
            field_dict["old_pubkey"] = old_pubkey
        if new_pubkey is not UNSET:
            field_dict["new_pubkey"] = new_pubkey
        if reason is not UNSET:
            field_dict["reason"] = reason
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

        old_pubkey = d.pop("old_pubkey", UNSET)

        new_pubkey = d.pop("new_pubkey", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        created_at = d.pop("created_at", UNSET)

        attestation_count = d.pop("attestation_count", UNSET)

        threshold = d.pop("threshold", UNSET)

        list_recovery_requests_to_attest_response_200_item = cls(
            id=id,
            old_pubkey=old_pubkey,
            new_pubkey=new_pubkey,
            reason=reason,
            created_at=created_at,
            attestation_count=attestation_count,
            threshold=threshold,
        )

        list_recovery_requests_to_attest_response_200_item.additional_properties = d
        return list_recovery_requests_to_attest_response_200_item

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
