from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_admin_banlist_override_body_override_type import (
    CreateAdminBanlistOverrideBodyOverrideType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminBanlistOverrideBody")


@_attrs_define
class CreateAdminBanlistOverrideBody:
    """
    Attributes:
        target_pubkey (str):
        override_type (CreateAdminBanlistOverrideBodyOverrideType):
        reason (str | Unset):
    """

    target_pubkey: str
    override_type: CreateAdminBanlistOverrideBodyOverrideType
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_pubkey = self.target_pubkey

        override_type = self.override_type.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_pubkey": target_pubkey,
                "override_type": override_type,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_pubkey = d.pop("target_pubkey")

        override_type = CreateAdminBanlistOverrideBodyOverrideType(
            d.pop("override_type")
        )

        reason = d.pop("reason", UNSET)

        create_admin_banlist_override_body = cls(
            target_pubkey=target_pubkey,
            override_type=override_type,
            reason=reason,
        )

        create_admin_banlist_override_body.additional_properties = d
        return create_admin_banlist_override_body

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
