from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FederationJoinAllianceBody")


@_attrs_define
class FederationJoinAllianceBody:
    """
    Attributes:
        invite_token (str):
        hub_url (str):
    """

    invite_token: str
    hub_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invite_token = self.invite_token

        hub_url = self.hub_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invite_token": invite_token,
                "hub_url": hub_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        invite_token = d.pop("invite_token")

        hub_url = d.pop("hub_url")

        federation_join_alliance_body = cls(
            invite_token=invite_token,
            hub_url=hub_url,
        )

        federation_join_alliance_body.additional_properties = d
        return federation_join_alliance_body

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
