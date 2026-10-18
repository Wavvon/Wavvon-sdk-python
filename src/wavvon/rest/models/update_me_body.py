from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMeBody")


@_attrs_define
class UpdateMeBody:
    """
    Attributes:
        display_name (str | Unset):
        avatar (None | str | Unset):
        findable_by_allies (bool | Unset): List me to members of allied hubs (see `GET
            /alliances/{alliance_id}/people`). Per hub, off by default; only takes effect while the alliance's own
            `people_visible` switch is on. Hubs advertising `alliance.people`.
    """

    display_name: str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    findable_by_allies: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        findable_by_allies = self.findable_by_allies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if findable_by_allies is not UNSET:
            field_dict["findable_by_allies"] = findable_by_allies

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        findable_by_allies = d.pop("findable_by_allies", UNSET)

        update_me_body = cls(
            display_name=display_name,
            avatar=avatar,
            findable_by_allies=findable_by_allies,
        )

        update_me_body.additional_properties = d
        return update_me_body

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
