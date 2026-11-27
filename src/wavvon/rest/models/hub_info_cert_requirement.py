from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hub_info_cert_requirement_others import HubInfoCertRequirementOthers

if TYPE_CHECKING:
    from ..models.trusted_cert_type import TrustedCertType


T = TypeVar("T", bound="HubInfoCertRequirement")


@_attrs_define
class HubInfoCertRequirement:
    """Which certificates take a newcomer through the fast lane (no lobby, approval or challenge). Omitted while both trust
    lists are empty.

        Attributes:
            trusted_issuers (list[str]): Hubs whose every certificate counts.
            trusted_types (list[TrustedCertType]):
            others (HubInfoCertRequirementOthers): What happens without a trusted certificate.
            replaces_invite (bool): A trusted certificate stands in for an invite.
    """

    trusted_issuers: list[str]
    trusted_types: list[TrustedCertType]
    others: HubInfoCertRequirementOthers
    replaces_invite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trusted_issuers = self.trusted_issuers

        trusted_types = []
        for trusted_types_item_data in self.trusted_types:
            trusted_types_item = trusted_types_item_data.to_dict()
            trusted_types.append(trusted_types_item)

        others = self.others.value

        replaces_invite = self.replaces_invite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trusted_issuers": trusted_issuers,
                "trusted_types": trusted_types,
                "others": others,
                "replaces_invite": replaces_invite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trusted_cert_type import TrustedCertType

        d = dict(src_dict)
        trusted_issuers = cast(list[str], d.pop("trusted_issuers"))

        trusted_types = []
        _trusted_types = d.pop("trusted_types")
        for trusted_types_item_data in _trusted_types:
            trusted_types_item = TrustedCertType.from_dict(trusted_types_item_data)

            trusted_types.append(trusted_types_item)

        others = HubInfoCertRequirementOthers(d.pop("others"))

        replaces_invite = d.pop("replaces_invite")

        hub_info_cert_requirement = cls(
            trusted_issuers=trusted_issuers,
            trusted_types=trusted_types,
            others=others,
            replaces_invite=replaces_invite,
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
