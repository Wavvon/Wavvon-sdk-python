from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cert_payload_standing import CertPayloadStanding
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertPayload")


@_attrs_define
class CertPayload:
    """Canonical certification payload signed by the issuing hub.

    Attributes:
        subject_kind (str | Unset): Always 'user'
        issuer_pubkey (str | Unset):
        issuer_url (str | Unset):
        subject_pubkey (str | Unset):
        member_since (int | Unset):
        standing (CertPayloadStanding | Unset):
        pow_level (int | None | Unset):
        issued_at (int | Unset):
        expires_at (int | Unset):
        capabilities (list[str] | Unset):
        label (str | Unset): Badge display name; present means this cert is an achievement badge. Omitted unless set.
        description (str | Unset): Omitted unless set.
        icon (str | Unset): Emoji or short icon for the badge. Omitted unless set.
    """

    subject_kind: str | Unset = UNSET
    issuer_pubkey: str | Unset = UNSET
    issuer_url: str | Unset = UNSET
    subject_pubkey: str | Unset = UNSET
    member_since: int | Unset = UNSET
    standing: CertPayloadStanding | Unset = UNSET
    pow_level: int | None | Unset = UNSET
    issued_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    label: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_kind = self.subject_kind

        issuer_pubkey = self.issuer_pubkey

        issuer_url = self.issuer_url

        subject_pubkey = self.subject_pubkey

        member_since = self.member_since

        standing: str | Unset = UNSET
        if not isinstance(self.standing, Unset):
            standing = self.standing.value

        pow_level: int | None | Unset
        if isinstance(self.pow_level, Unset):
            pow_level = UNSET
        else:
            pow_level = self.pow_level

        issued_at = self.issued_at

        expires_at = self.expires_at

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        label = self.label

        description = self.description

        icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject_kind is not UNSET:
            field_dict["subject_kind"] = subject_kind
        if issuer_pubkey is not UNSET:
            field_dict["issuer_pubkey"] = issuer_pubkey
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if subject_pubkey is not UNSET:
            field_dict["subject_pubkey"] = subject_pubkey
        if member_since is not UNSET:
            field_dict["member_since"] = member_since
        if standing is not UNSET:
            field_dict["standing"] = standing
        if pow_level is not UNSET:
            field_dict["pow_level"] = pow_level
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        subject_kind = d.pop("subject_kind", UNSET)

        issuer_pubkey = d.pop("issuer_pubkey", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        subject_pubkey = d.pop("subject_pubkey", UNSET)

        member_since = d.pop("member_since", UNSET)

        _standing = d.pop("standing", UNSET)
        standing: CertPayloadStanding | Unset
        if isinstance(_standing, Unset):
            standing = UNSET
        else:
            standing = CertPayloadStanding(_standing)

        def _parse_pow_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pow_level = _parse_pow_level(d.pop("pow_level", UNSET))

        issued_at = d.pop("issued_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        cert_payload = cls(
            subject_kind=subject_kind,
            issuer_pubkey=issuer_pubkey,
            issuer_url=issuer_url,
            subject_pubkey=subject_pubkey,
            member_since=member_since,
            standing=standing,
            pow_level=pow_level,
            issued_at=issued_at,
            expires_at=expires_at,
            capabilities=capabilities,
            label=label,
            description=description,
            icon=icon,
        )

        cert_payload.additional_properties = d
        return cert_payload

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
