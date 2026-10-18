from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_profile_response_200_badges_item import (
        GetUserProfileResponse200BadgesItem,
    )
    from ..models.get_user_profile_response_200_roles_item import (
        GetUserProfileResponse200RolesItem,
    )


T = TypeVar("T", bound="GetUserProfileResponse200")


@_attrs_define
class GetUserProfileResponse200:
    """
    Attributes:
        public_key (str | Unset):
        display_name (None | str | Unset):
        avatar (None | str | Unset):
        joined_at (int | Unset):
        roles (list[GetUserProfileResponse200RolesItem] | Unset):
        badges (list[GetUserProfileResponse200BadgesItem] | Unset):
    """

    public_key: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    joined_at: int | Unset = UNSET
    roles: list[GetUserProfileResponse200RolesItem] | Unset = UNSET
    badges: list[GetUserProfileResponse200BadgesItem] | Unset = UNSET
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

        joined_at = self.joined_at

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        badges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.badges, Unset):
            badges = []
            for badges_item_data in self.badges:
                badges_item = badges_item_data.to_dict()
                badges.append(badges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if joined_at is not UNSET:
            field_dict["joined_at"] = joined_at
        if roles is not UNSET:
            field_dict["roles"] = roles
        if badges is not UNSET:
            field_dict["badges"] = badges

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_user_profile_response_200_badges_item import (
            GetUserProfileResponse200BadgesItem,
        )
        from ..models.get_user_profile_response_200_roles_item import (
            GetUserProfileResponse200RolesItem,
        )

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

        joined_at = d.pop("joined_at", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[GetUserProfileResponse200RolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = GetUserProfileResponse200RolesItem.from_dict(
                    roles_item_data
                )

                roles.append(roles_item)

        _badges = d.pop("badges", UNSET)
        badges: list[GetUserProfileResponse200BadgesItem] | Unset = UNSET
        if _badges is not UNSET:
            badges = []
            for badges_item_data in _badges:
                badges_item = GetUserProfileResponse200BadgesItem.from_dict(
                    badges_item_data
                )

                badges.append(badges_item)

        get_user_profile_response_200 = cls(
            public_key=public_key,
            display_name=display_name,
            avatar=avatar,
            joined_at=joined_at,
            roles=roles,
            badges=badges,
        )

        get_user_profile_response_200.additional_properties = d
        return get_user_profile_response_200

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
