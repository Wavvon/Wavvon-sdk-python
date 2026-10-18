from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFederationAllianceInviteBody")


@_attrs_define
class CreateFederationAllianceInviteBody:
    """
    Attributes:
        id (str):
        alliance_id (str):
        alliance_name (str):
        from_hub_url (str):
        from_hub_name (str):
        from_hub_public_key (str):
        invite_token (str):
        message (str | Unset):
    """

    id: str
    alliance_id: str
    alliance_name: str
    from_hub_url: str
    from_hub_name: str
    from_hub_public_key: str
    invite_token: str
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        alliance_id = self.alliance_id

        alliance_name = self.alliance_name

        from_hub_url = self.from_hub_url

        from_hub_name = self.from_hub_name

        from_hub_public_key = self.from_hub_public_key

        invite_token = self.invite_token

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "alliance_id": alliance_id,
                "alliance_name": alliance_name,
                "from_hub_url": from_hub_url,
                "from_hub_name": from_hub_name,
                "from_hub_public_key": from_hub_public_key,
                "invite_token": invite_token,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        alliance_id = d.pop("alliance_id")

        alliance_name = d.pop("alliance_name")

        from_hub_url = d.pop("from_hub_url")

        from_hub_name = d.pop("from_hub_name")

        from_hub_public_key = d.pop("from_hub_public_key")

        invite_token = d.pop("invite_token")

        message = d.pop("message", UNSET)

        create_federation_alliance_invite_body = cls(
            id=id,
            alliance_id=alliance_id,
            alliance_name=alliance_name,
            from_hub_url=from_hub_url,
            from_hub_name=from_hub_name,
            from_hub_public_key=from_hub_public_key,
            invite_token=invite_token,
            message=message,
        )

        create_federation_alliance_invite_body.additional_properties = d
        return create_federation_alliance_invite_body

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
