from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInviteBody")


@_attrs_define
class CreateInviteBody:
    """
    Attributes:
        max_uses (int | None | Unset):
        expires_in_seconds (int | None | Unset): Lifetime in seconds from now. Omitted means no expiry, except as noted
            under `grant_role_id`.
        grant_role_id (None | str | Unset): Role granted to the joining member besides the everyone role. Must exist,
            and the creator must be able to grant every permission it carries. A role that amounts to a takeover caps the
            invite to one use and a short expiry.
        bound_pubkey (None | str | Unset): 64 hex characters. The only identity this invite admits.
    """

    max_uses: int | None | Unset = UNSET
    expires_in_seconds: int | None | Unset = UNSET
    grant_role_id: None | str | Unset = UNSET
    bound_pubkey: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_uses: int | None | Unset
        if isinstance(self.max_uses, Unset):
            max_uses = UNSET
        else:
            max_uses = self.max_uses

        expires_in_seconds: int | None | Unset
        if isinstance(self.expires_in_seconds, Unset):
            expires_in_seconds = UNSET
        else:
            expires_in_seconds = self.expires_in_seconds

        grant_role_id: None | str | Unset
        if isinstance(self.grant_role_id, Unset):
            grant_role_id = UNSET
        else:
            grant_role_id = self.grant_role_id

        bound_pubkey: None | str | Unset
        if isinstance(self.bound_pubkey, Unset):
            bound_pubkey = UNSET
        else:
            bound_pubkey = self.bound_pubkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses
        if expires_in_seconds is not UNSET:
            field_dict["expires_in_seconds"] = expires_in_seconds
        if grant_role_id is not UNSET:
            field_dict["grant_role_id"] = grant_role_id
        if bound_pubkey is not UNSET:
            field_dict["bound_pubkey"] = bound_pubkey

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_max_uses(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_uses = _parse_max_uses(d.pop("max_uses", UNSET))

        def _parse_expires_in_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_seconds = _parse_expires_in_seconds(
            d.pop("expires_in_seconds", UNSET)
        )

        def _parse_grant_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_role_id = _parse_grant_role_id(d.pop("grant_role_id", UNSET))

        def _parse_bound_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bound_pubkey = _parse_bound_pubkey(d.pop("bound_pubkey", UNSET))

        create_invite_body = cls(
            max_uses=max_uses,
            expires_in_seconds=expires_in_seconds,
            grant_role_id=grant_role_id,
            bound_pubkey=bound_pubkey,
        )

        create_invite_body.additional_properties = d
        return create_invite_body

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
