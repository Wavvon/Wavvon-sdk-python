from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BadgePayload")


@_attrs_define
class BadgePayload:
    """Canonical badge payload signed by the issuing hub.

    Attributes:
        issuer_pubkey (str | Unset):
        issuer_url (str | Unset):
        subject_pubkey (str | Unset):
        label (str | Unset):
        issued_at (str | Unset): ISO-8601 timestamp
        expires_at (None | str | Unset):
    """

    issuer_pubkey: str | Unset = UNSET
    issuer_url: str | Unset = UNSET
    subject_pubkey: str | Unset = UNSET
    label: str | Unset = UNSET
    issued_at: str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer_pubkey = self.issuer_pubkey

        issuer_url = self.issuer_url

        subject_pubkey = self.subject_pubkey

        label = self.label

        issued_at = self.issued_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer_pubkey is not UNSET:
            field_dict["issuer_pubkey"] = issuer_pubkey
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if subject_pubkey is not UNSET:
            field_dict["subject_pubkey"] = subject_pubkey
        if label is not UNSET:
            field_dict["label"] = label
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issuer_pubkey = d.pop("issuer_pubkey", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        subject_pubkey = d.pop("subject_pubkey", UNSET)

        label = d.pop("label", UNSET)

        issued_at = d.pop("issued_at", UNSET)

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        badge_payload = cls(
            issuer_pubkey=issuer_pubkey,
            issuer_url=issuer_url,
            subject_pubkey=subject_pubkey,
            label=label,
            issued_at=issued_at,
            expires_at=expires_at,
        )

        badge_payload.additional_properties = d
        return badge_payload

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
