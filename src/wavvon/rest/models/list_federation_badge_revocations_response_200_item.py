from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListFederationBadgeRevocationsResponse200Item")


@_attrs_define
class ListFederationBadgeRevocationsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        recipient_hub_pubkey (str | Unset):
        label (str | Unset):
        revoked_at (str | Unset):
    """

    id: str | Unset = UNSET
    recipient_hub_pubkey: str | Unset = UNSET
    label: str | Unset = UNSET
    revoked_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipient_hub_pubkey = self.recipient_hub_pubkey

        label = self.label

        revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if recipient_hub_pubkey is not UNSET:
            field_dict["recipient_hub_pubkey"] = recipient_hub_pubkey
        if label is not UNSET:
            field_dict["label"] = label
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        recipient_hub_pubkey = d.pop("recipient_hub_pubkey", UNSET)

        label = d.pop("label", UNSET)

        revoked_at = d.pop("revoked_at", UNSET)

        list_federation_badge_revocations_response_200_item = cls(
            id=id,
            recipient_hub_pubkey=recipient_hub_pubkey,
            label=label,
            revoked_at=revoked_at,
        )

        list_federation_badge_revocations_response_200_item.additional_properties = d
        return list_federation_badge_revocations_response_200_item

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
