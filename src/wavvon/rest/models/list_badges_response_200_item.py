from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_payload import BadgePayload


T = TypeVar("T", bound="ListBadgesResponse200Item")


@_attrs_define
class ListBadgesResponse200Item:
    """
    Attributes:
        id (str | Unset):
        issuer_pubkey (str | Unset):
        issuer_url (str | Unset):
        label (str | Unset):
        payload (BadgePayload | Unset): Canonical badge payload signed by the issuing hub.
        accepted_at (str | Unset):
    """

    id: str | Unset = UNSET
    issuer_pubkey: str | Unset = UNSET
    issuer_url: str | Unset = UNSET
    label: str | Unset = UNSET
    payload: BadgePayload | Unset = UNSET
    accepted_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        issuer_pubkey = self.issuer_pubkey

        issuer_url = self.issuer_url

        label = self.label

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        accepted_at = self.accepted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issuer_pubkey is not UNSET:
            field_dict["issuer_pubkey"] = issuer_pubkey
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if label is not UNSET:
            field_dict["label"] = label
        if payload is not UNSET:
            field_dict["payload"] = payload
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.badge_payload import BadgePayload

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        issuer_pubkey = d.pop("issuer_pubkey", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        label = d.pop("label", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: BadgePayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = BadgePayload.from_dict(_payload)

        accepted_at = d.pop("accepted_at", UNSET)

        list_badges_response_200_item = cls(
            id=id,
            issuer_pubkey=issuer_pubkey,
            issuer_url=issuer_url,
            label=label,
            payload=payload,
            accepted_at=accepted_at,
        )

        list_badges_response_200_item.additional_properties = d
        return list_badges_response_200_item

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
