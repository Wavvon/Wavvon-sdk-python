from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_recovery_rotation_request_response_200_status import (
    GetRecoveryRotationRequestResponse200Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRecoveryRotationRequestResponse200")


@_attrs_define
class GetRecoveryRotationRequestResponse200:
    """
    Attributes:
        id (str | Unset):
        hub_pubkey (str | Unset):
        old_pubkey (str | Unset):
        new_pubkey (str | Unset):
        nonce (str | Unset):
        status (GetRecoveryRotationRequestResponse200Status | Unset):
        attestation_count (int | Unset):
        threshold (int | Unset):
    """

    id: str | Unset = UNSET
    hub_pubkey: str | Unset = UNSET
    old_pubkey: str | Unset = UNSET
    new_pubkey: str | Unset = UNSET
    nonce: str | Unset = UNSET
    status: GetRecoveryRotationRequestResponse200Status | Unset = UNSET
    attestation_count: int | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        hub_pubkey = self.hub_pubkey

        old_pubkey = self.old_pubkey

        new_pubkey = self.new_pubkey

        nonce = self.nonce

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        attestation_count = self.attestation_count

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if hub_pubkey is not UNSET:
            field_dict["hub_pubkey"] = hub_pubkey
        if old_pubkey is not UNSET:
            field_dict["old_pubkey"] = old_pubkey
        if new_pubkey is not UNSET:
            field_dict["new_pubkey"] = new_pubkey
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if status is not UNSET:
            field_dict["status"] = status
        if attestation_count is not UNSET:
            field_dict["attestation_count"] = attestation_count
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        hub_pubkey = d.pop("hub_pubkey", UNSET)

        old_pubkey = d.pop("old_pubkey", UNSET)

        new_pubkey = d.pop("new_pubkey", UNSET)

        nonce = d.pop("nonce", UNSET)

        _status = d.pop("status", UNSET)
        status: GetRecoveryRotationRequestResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetRecoveryRotationRequestResponse200Status(_status)

        attestation_count = d.pop("attestation_count", UNSET)

        threshold = d.pop("threshold", UNSET)

        get_recovery_rotation_request_response_200 = cls(
            id=id,
            hub_pubkey=hub_pubkey,
            old_pubkey=old_pubkey,
            new_pubkey=new_pubkey,
            nonce=nonce,
            status=status,
            attestation_count=attestation_count,
            threshold=threshold,
        )

        get_recovery_rotation_request_response_200.additional_properties = d
        return get_recovery_rotation_request_response_200

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
