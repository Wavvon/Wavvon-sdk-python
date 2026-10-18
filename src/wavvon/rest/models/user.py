from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        public_key (str | Unset):
        display_name (None | str | Unset):
        avatar (None | str | Unset): Base64-encoded image
        online (bool | Unset):
        group_role (None | str | Unset):
    """

    public_key: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    online: bool | Unset = UNSET
    group_role: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

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

        online = self.online

        group_role: None | str | Unset
        if isinstance(self.group_role, Unset):
            group_role = UNSET
        else:
            group_role = self.group_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if online is not UNSET:
            field_dict["online"] = online
        if group_role is not UNSET:
            field_dict["group_role"] = group_role

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_key = d.pop("public_key", UNSET)

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

        online = d.pop("online", UNSET)

        def _parse_group_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_role = _parse_group_role(d.pop("group_role", UNSET))

        user = cls(
            public_key=public_key,
            display_name=display_name,
            avatar=avatar,
            online=online,
            group_role=group_role,
        )

        user.additional_properties = d
        return user

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
