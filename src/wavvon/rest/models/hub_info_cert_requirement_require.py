from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HubInfoCertRequirementRequire")


@_attrs_define
class HubInfoCertRequirementRequire:
    """
    Attributes:
        min_pow_level (int | None):
        min_member_since_days (int | None):
    """

    min_pow_level: int | None
    min_member_since_days: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_pow_level: int | None
        min_pow_level = self.min_pow_level

        min_member_since_days: int | None
        min_member_since_days = self.min_member_since_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min_pow_level": min_pow_level,
                "min_member_since_days": min_member_since_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_min_pow_level(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_pow_level = _parse_min_pow_level(d.pop("min_pow_level"))

        def _parse_min_member_since_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_member_since_days = _parse_min_member_since_days(
            d.pop("min_member_since_days")
        )

        hub_info_cert_requirement_require = cls(
            min_pow_level=min_pow_level,
            min_member_since_days=min_member_since_days,
        )

        hub_info_cert_requirement_require.additional_properties = d
        return hub_info_cert_requirement_require

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
