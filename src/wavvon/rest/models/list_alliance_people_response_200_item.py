from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAlliancePeopleResponse200Item")


@_attrs_define
class ListAlliancePeopleResponse200Item:
    """
    Attributes:
        public_key (str): Roster pubkey on the owning hub
        master_pubkey (str): Master key, for DM routing
        display_name (None | str | Unset):
        avatar (None | str | Unset):
    """

    public_key: str
    master_pubkey: str
    display_name: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        master_pubkey = self.master_pubkey

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "master_pubkey": master_pubkey,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_key = d.pop("public_key")

        master_pubkey = d.pop("master_pubkey")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        list_alliance_people_response_200_item = cls(
            public_key=public_key,
            master_pubkey=master_pubkey,
            display_name=display_name,
            avatar=avatar,
        )

        list_alliance_people_response_200_item.additional_properties = d
        return list_alliance_people_response_200_item

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
