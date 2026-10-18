from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_status import InviteStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invite")


@_attrs_define
class Invite:
    """
    Attributes:
        code (str | Unset):
        created_by (str | Unset):
        max_uses (int | None | Unset):
        uses (int | Unset):
        expires_at (int | None | Unset):
        created_at (int | Unset):
        grant_role_id (None | str | Unset): Role granted on redemption besides everyone
        bound_pubkey (None | str | Unset): The one identity this invite admits, or null for a bearer code. Advertised as
            the `invites.bound` capability.
        status (InviteStatus | Unset): Whether this invite can still admit anyone, and if not, which of the two ways it
            retired. Advertised as the `invites.status` capability; absent on hubs that do not advertise it.
    """

    code: str | Unset = UNSET
    created_by: str | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    uses: int | Unset = UNSET
    expires_at: int | None | Unset = UNSET
    created_at: int | Unset = UNSET
    grant_role_id: None | str | Unset = UNSET
    bound_pubkey: None | str | Unset = UNSET
    status: InviteStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        created_by = self.created_by

        max_uses: int | None | Unset
        if isinstance(self.max_uses, Unset):
            max_uses = UNSET
        else:
            max_uses = self.max_uses

        uses = self.uses

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        created_at = self.created_at

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses
        if uses is not UNSET:
            field_dict["uses"] = uses
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if grant_role_id is not UNSET:
            field_dict["grant_role_id"] = grant_role_id
        if bound_pubkey is not UNSET:
            field_dict["bound_pubkey"] = bound_pubkey
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        created_by = d.pop("created_by", UNSET)

        def _parse_max_uses(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_uses = _parse_max_uses(d.pop("max_uses", UNSET))

        uses = d.pop("uses", UNSET)

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        created_at = d.pop("created_at", UNSET)

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

        _status = d.pop("status", UNSET)
        status: InviteStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InviteStatus(_status)

        invite = cls(
            code=code,
            created_by=created_by,
            max_uses=max_uses,
            uses=uses,
            expires_at=expires_at,
            created_at=created_at,
            grant_role_id=grant_role_id,
            bound_pubkey=bound_pubkey,
            status=status,
        )

        invite.additional_properties = d
        return invite

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
