from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminSettingsCertsBodyCertRequire")


@_attrs_define
class UpdateAdminSettingsCertsBodyCertRequire:
    """
    Attributes:
        min_pow_level (int | Unset):
        min_member_since_days (int | Unset):
    """

    min_pow_level: int | Unset = UNSET
    min_member_since_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_pow_level = self.min_pow_level

        min_member_since_days = self.min_member_since_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_pow_level is not UNSET:
            field_dict["min_pow_level"] = min_pow_level
        if min_member_since_days is not UNSET:
            field_dict["min_member_since_days"] = min_member_since_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        min_pow_level = d.pop("min_pow_level", UNSET)

        min_member_since_days = d.pop("min_member_since_days", UNSET)

        update_admin_settings_certs_body_cert_require = cls(
            min_pow_level=min_pow_level,
            min_member_since_days=min_member_since_days,
        )

        update_admin_settings_certs_body_cert_require.additional_properties = d
        return update_admin_settings_certs_body_cert_require

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
