from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_admin_banlist_overrides_response_200_item_override_type import (
    ListAdminBanlistOverridesResponse200ItemOverrideType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminBanlistOverridesResponse200Item")


@_attrs_define
class ListAdminBanlistOverridesResponse200Item:
    """
    Attributes:
        target_pubkey (str | Unset):
        override_type (ListAdminBanlistOverridesResponse200ItemOverrideType | Unset):
        reason (None | str | Unset):
        created_at (int | Unset):
    """

    target_pubkey: str | Unset = UNSET
    override_type: ListAdminBanlistOverridesResponse200ItemOverrideType | Unset = UNSET
    reason: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_pubkey = self.target_pubkey

        override_type: str | Unset = UNSET
        if not isinstance(self.override_type, Unset):
            override_type = self.override_type.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_pubkey is not UNSET:
            field_dict["target_pubkey"] = target_pubkey
        if override_type is not UNSET:
            field_dict["override_type"] = override_type
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_pubkey = d.pop("target_pubkey", UNSET)

        _override_type = d.pop("override_type", UNSET)
        override_type: ListAdminBanlistOverridesResponse200ItemOverrideType | Unset
        if isinstance(_override_type, Unset):
            override_type = UNSET
        else:
            override_type = ListAdminBanlistOverridesResponse200ItemOverrideType(
                _override_type
            )

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        created_at = d.pop("created_at", UNSET)

        list_admin_banlist_overrides_response_200_item = cls(
            target_pubkey=target_pubkey,
            override_type=override_type,
            reason=reason,
            created_at=created_at,
        )

        list_admin_banlist_overrides_response_200_item.additional_properties = d
        return list_admin_banlist_overrides_response_200_item

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
