from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateFederationAllianceMemberBody")


@_attrs_define
class CreateFederationAllianceMemberBody:
    """
    Attributes:
        alliance_id (str):
        hub_url (str):
        inviter_public_key (str):
        voucher (str):
    """

    alliance_id: str
    hub_url: str
    inviter_public_key: str
    voucher: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alliance_id = self.alliance_id

        hub_url = self.hub_url

        inviter_public_key = self.inviter_public_key

        voucher = self.voucher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alliance_id": alliance_id,
                "hub_url": hub_url,
                "inviter_public_key": inviter_public_key,
                "voucher": voucher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alliance_id = d.pop("alliance_id")

        hub_url = d.pop("hub_url")

        inviter_public_key = d.pop("inviter_public_key")

        voucher = d.pop("voucher")

        create_federation_alliance_member_body = cls(
            alliance_id=alliance_id,
            hub_url=hub_url,
            inviter_public_key=inviter_public_key,
            voucher=voucher,
        )

        create_federation_alliance_member_body.additional_properties = d
        return create_federation_alliance_member_body

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
