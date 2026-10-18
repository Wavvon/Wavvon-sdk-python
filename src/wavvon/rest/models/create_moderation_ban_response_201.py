from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateModerationBanResponse201")


@_attrs_define
class CreateModerationBanResponse201:
    """
    Attributes:
        target_public_key (str | Unset):
        banned_by (str | Unset):
        reason (None | str | Unset):
        expires_at (int | None | Unset): Unix seconds; null for a permanent ban.
        created_at (int | Unset):
    """

    target_public_key: str | Unset = UNSET
    banned_by: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    expires_at: int | None | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_public_key = self.target_public_key

        banned_by = self.banned_by

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_public_key is not UNSET:
            field_dict["target_public_key"] = target_public_key
        if banned_by is not UNSET:
            field_dict["banned_by"] = banned_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_public_key = d.pop("target_public_key", UNSET)

        banned_by = d.pop("banned_by", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        created_at = d.pop("created_at", UNSET)

        create_moderation_ban_response_201 = cls(
            target_public_key=target_public_key,
            banned_by=banned_by,
            reason=reason,
            expires_at=expires_at,
            created_at=created_at,
        )

        create_moderation_ban_response_201.additional_properties = d
        return create_moderation_ban_response_201

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
