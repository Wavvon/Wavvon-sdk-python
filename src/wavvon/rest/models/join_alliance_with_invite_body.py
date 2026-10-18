from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JoinAllianceWithInviteBody")


@_attrs_define
class JoinAllianceWithInviteBody:
    """
    Attributes:
        inviter_hub_url (str):
        alliance_id (str):
        invite_token (str):
        own_hub_url (str):
    """

    inviter_hub_url: str
    alliance_id: str
    invite_token: str
    own_hub_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inviter_hub_url = self.inviter_hub_url

        alliance_id = self.alliance_id

        invite_token = self.invite_token

        own_hub_url = self.own_hub_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inviter_hub_url": inviter_hub_url,
                "alliance_id": alliance_id,
                "invite_token": invite_token,
                "own_hub_url": own_hub_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        inviter_hub_url = d.pop("inviter_hub_url")

        alliance_id = d.pop("alliance_id")

        invite_token = d.pop("invite_token")

        own_hub_url = d.pop("own_hub_url")

        join_alliance_with_invite_body = cls(
            inviter_hub_url=inviter_hub_url,
            alliance_id=alliance_id,
            invite_token=invite_token,
            own_hub_url=own_hub_url,
        )

        join_alliance_with_invite_body.additional_properties = d
        return join_alliance_with_invite_body

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
