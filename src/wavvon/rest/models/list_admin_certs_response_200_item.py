from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_admin_certs_response_200_item_standing import (
    ListAdminCertsResponse200ItemStanding,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_payload import CertPayload


T = TypeVar("T", bound="ListAdminCertsResponse200Item")


@_attrs_define
class ListAdminCertsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        subject_pubkey (str | Unset):
        pow_level (int | None | Unset):
        member_since (int | Unset):
        issued_at (int | Unset):
        expires_at (int | Unset):
        revoked_at (int | None | Unset):
        standing (ListAdminCertsResponse200ItemStanding | Unset):
        payload (CertPayload | Unset): Canonical certification payload signed by the issuing hub.
    """

    id: str | Unset = UNSET
    subject_pubkey: str | Unset = UNSET
    pow_level: int | None | Unset = UNSET
    member_since: int | Unset = UNSET
    issued_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    revoked_at: int | None | Unset = UNSET
    standing: ListAdminCertsResponse200ItemStanding | Unset = UNSET
    payload: CertPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subject_pubkey = self.subject_pubkey

        pow_level: int | None | Unset
        if isinstance(self.pow_level, Unset):
            pow_level = UNSET
        else:
            pow_level = self.pow_level

        member_since = self.member_since

        issued_at = self.issued_at

        expires_at = self.expires_at

        revoked_at: int | None | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        else:
            revoked_at = self.revoked_at

        standing: str | Unset = UNSET
        if not isinstance(self.standing, Unset):
            standing = self.standing.value

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subject_pubkey is not UNSET:
            field_dict["subject_pubkey"] = subject_pubkey
        if pow_level is not UNSET:
            field_dict["pow_level"] = pow_level
        if member_since is not UNSET:
            field_dict["member_since"] = member_since
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if standing is not UNSET:
            field_dict["standing"] = standing
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cert_payload import CertPayload

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        subject_pubkey = d.pop("subject_pubkey", UNSET)

        def _parse_pow_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pow_level = _parse_pow_level(d.pop("pow_level", UNSET))

        member_since = d.pop("member_since", UNSET)

        issued_at = d.pop("issued_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        def _parse_revoked_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        _standing = d.pop("standing", UNSET)
        standing: ListAdminCertsResponse200ItemStanding | Unset
        if isinstance(_standing, Unset):
            standing = UNSET
        else:
            standing = ListAdminCertsResponse200ItemStanding(_standing)

        _payload = d.pop("payload", UNSET)
        payload: CertPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = CertPayload.from_dict(_payload)

        list_admin_certs_response_200_item = cls(
            id=id,
            subject_pubkey=subject_pubkey,
            pow_level=pow_level,
            member_since=member_since,
            issued_at=issued_at,
            expires_at=expires_at,
            revoked_at=revoked_at,
            standing=standing,
            payload=payload,
        )

        list_admin_certs_response_200_item.additional_properties = d
        return list_admin_certs_response_200_item

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
