from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFriendBody")


@_attrs_define
class CreateFriendBody:
    """
    Attributes:
        target_public_key (str):
        hub_url (str | Unset): Required for federated (cross-hub) friends
        display_name (str | Unset):
    """

    target_public_key: str
    hub_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_public_key = self.target_public_key

        hub_url = self.hub_url

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_public_key": target_public_key,
            }
        )
        if hub_url is not UNSET:
            field_dict["hub_url"] = hub_url
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_public_key = d.pop("target_public_key")

        hub_url = d.pop("hub_url", UNSET)

        display_name = d.pop("display_name", UNSET)

        create_friend_body = cls(
            target_public_key=target_public_key,
            hub_url=hub_url,
            display_name=display_name,
        )

        create_friend_body.additional_properties = d
        return create_friend_body

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
