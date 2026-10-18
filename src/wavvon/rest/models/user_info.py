from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserInfo")


@_attrs_define
class UserInfo:
    """A member as listed by `GET /users`.

    Attributes:
        public_key (str):
        display_name (None | str):
        avatar (None | str): Base64-encoded image
        online (bool):
        group_role (None | str):
        birthday (None | str):
        name_color (None | str):
        status (str | Unset): Presence status. Omitted unless set.
        status_custom (str | Unset): Custom status text. Omitted unless set.
    """

    public_key: str
    display_name: None | str
    avatar: None | str
    online: bool
    group_role: None | str
    birthday: None | str
    name_color: None | str
    status: str | Unset = UNSET
    status_custom: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        display_name: None | str
        display_name = self.display_name

        avatar: None | str
        avatar = self.avatar

        online = self.online

        group_role: None | str
        group_role = self.group_role

        birthday: None | str
        birthday = self.birthday

        name_color: None | str
        name_color = self.name_color

        status = self.status

        status_custom = self.status_custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "display_name": display_name,
                "avatar": avatar,
                "online": online,
                "group_role": group_role,
                "birthday": birthday,
                "name_color": name_color,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if status_custom is not UNSET:
            field_dict["status_custom"] = status_custom

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_key = d.pop("public_key")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_avatar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        online = d.pop("online")

        def _parse_group_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group_role = _parse_group_role(d.pop("group_role"))

        def _parse_birthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthday = _parse_birthday(d.pop("birthday"))

        def _parse_name_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name_color = _parse_name_color(d.pop("name_color"))

        status = d.pop("status", UNSET)

        status_custom = d.pop("status_custom", UNSET)

        user_info = cls(
            public_key=public_key,
            display_name=display_name,
            avatar=avatar,
            online=online,
            group_role=group_role,
            birthday=birthday,
            name_color=name_color,
            status=status,
            status_custom=status_custom,
        )

        user_info.additional_properties = d
        return user_info

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
