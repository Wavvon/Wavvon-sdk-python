from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hub_info_cert_requirement_require import HubInfoCertRequirementRequire


T = TypeVar("T", bound="HubInfoCertRequirement")


@_attrs_define
class HubInfoCertRequirement:
    """What a certificate must show to admit a member. Omitted unless set.

    Attributes:
        mode (str):
        trusted_issuers (list[str]):
        require (HubInfoCertRequirementRequire):
    """

    mode: str
    trusted_issuers: list[str]
    require: HubInfoCertRequirementRequire
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        trusted_issuers = self.trusted_issuers

        require = self.require.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "trusted_issuers": trusted_issuers,
                "require": require,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hub_info_cert_requirement_require import (
            HubInfoCertRequirementRequire,
        )

        d = dict(src_dict)
        mode = d.pop("mode")

        trusted_issuers = cast(list[str], d.pop("trusted_issuers"))

        require = HubInfoCertRequirementRequire.from_dict(d.pop("require"))

        hub_info_cert_requirement = cls(
            mode=mode,
            trusted_issuers=trusted_issuers,
            require=require,
        )

        hub_info_cert_requirement.additional_properties = d
        return hub_info_cert_requirement

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
