from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_payload import BadgePayload


T = TypeVar("T", bound="IssueAdminBadgeResponse201")


@_attrs_define
class IssueAdminBadgeResponse201:
    """
    Attributes:
        id (str | Unset):
        recipient_hub_url (str | Unset):
        recipient_hub_pubkey (str | Unset):
        label (str | Unset):
        payload (BadgePayload | Unset): Canonical badge payload signed by the issuing hub.
        issued_at (str | Unset):
        expires_at (None | str | Unset):
    """

    id: str | Unset = UNSET
    recipient_hub_url: str | Unset = UNSET
    recipient_hub_pubkey: str | Unset = UNSET
    label: str | Unset = UNSET
    payload: BadgePayload | Unset = UNSET
    issued_at: str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipient_hub_url = self.recipient_hub_url

        recipient_hub_pubkey = self.recipient_hub_pubkey

        label = self.label

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        issued_at = self.issued_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if recipient_hub_url is not UNSET:
            field_dict["recipient_hub_url"] = recipient_hub_url
        if recipient_hub_pubkey is not UNSET:
            field_dict["recipient_hub_pubkey"] = recipient_hub_pubkey
        if label is not UNSET:
            field_dict["label"] = label
        if payload is not UNSET:
            field_dict["payload"] = payload
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.badge_payload import BadgePayload

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        recipient_hub_url = d.pop("recipient_hub_url", UNSET)

        recipient_hub_pubkey = d.pop("recipient_hub_pubkey", UNSET)

        label = d.pop("label", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: BadgePayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = BadgePayload.from_dict(_payload)

        issued_at = d.pop("issued_at", UNSET)

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        issue_admin_badge_response_201 = cls(
            id=id,
            recipient_hub_url=recipient_hub_url,
            recipient_hub_pubkey=recipient_hub_pubkey,
            label=label,
            payload=payload,
            issued_at=issued_at,
            expires_at=expires_at,
        )

        issue_admin_badge_response_201.additional_properties = d
        return issue_admin_badge_response_201

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
