from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.me_info_approval_status import MeInfoApprovalStatus

if TYPE_CHECKING:
    from ..models.me_info_favorite_hubs_item import MeInfoFavoriteHubsItem
    from ..models.role import Role


T = TypeVar("T", bound="MeInfo")


@_attrs_define
class MeInfo:
    """
    Attributes:
        public_key (str):
        display_name (None | str):
        avatar (None | str):
        bio (None | str):
        pronouns (None | str):
        status_message (None | str):
        activities (None | str):
        accent_color (None | str):
        cover (None | str):
        favorite_hubs (list[MeInfoFavoriteHubsItem]):
        show_hubs (bool):
        findable_by_allies (bool):
        approval_status (MeInfoApprovalStatus):
        roles (list[Role]):
        birthday (None | str):
        name_color (None | str):
    """

    public_key: str
    display_name: None | str
    avatar: None | str
    bio: None | str
    pronouns: None | str
    status_message: None | str
    activities: None | str
    accent_color: None | str
    cover: None | str
    favorite_hubs: list[MeInfoFavoriteHubsItem]
    show_hubs: bool
    findable_by_allies: bool
    approval_status: MeInfoApprovalStatus
    roles: list[Role]
    birthday: None | str
    name_color: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        display_name: None | str
        display_name = self.display_name

        avatar: None | str
        avatar = self.avatar

        bio: None | str
        bio = self.bio

        pronouns: None | str
        pronouns = self.pronouns

        status_message: None | str
        status_message = self.status_message

        activities: None | str
        activities = self.activities

        accent_color: None | str
        accent_color = self.accent_color

        cover: None | str
        cover = self.cover

        favorite_hubs = []
        for favorite_hubs_item_data in self.favorite_hubs:
            favorite_hubs_item = favorite_hubs_item_data.to_dict()
            favorite_hubs.append(favorite_hubs_item)

        show_hubs = self.show_hubs

        findable_by_allies = self.findable_by_allies

        approval_status = self.approval_status.value

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        birthday: None | str
        birthday = self.birthday

        name_color: None | str
        name_color = self.name_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "display_name": display_name,
                "avatar": avatar,
                "bio": bio,
                "pronouns": pronouns,
                "status_message": status_message,
                "activities": activities,
                "accent_color": accent_color,
                "cover": cover,
                "favorite_hubs": favorite_hubs,
                "show_hubs": show_hubs,
                "findable_by_allies": findable_by_allies,
                "approval_status": approval_status,
                "roles": roles,
                "birthday": birthday,
                "name_color": name_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_info_favorite_hubs_item import MeInfoFavoriteHubsItem
        from ..models.role import Role

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

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        def _parse_pronouns(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pronouns = _parse_pronouns(d.pop("pronouns"))

        def _parse_status_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_message = _parse_status_message(d.pop("status_message"))

        def _parse_activities(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        activities = _parse_activities(d.pop("activities"))

        def _parse_accent_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        accent_color = _parse_accent_color(d.pop("accent_color"))

        def _parse_cover(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover = _parse_cover(d.pop("cover"))

        favorite_hubs = []
        _favorite_hubs = d.pop("favorite_hubs")
        for favorite_hubs_item_data in _favorite_hubs:
            favorite_hubs_item = MeInfoFavoriteHubsItem.from_dict(
                favorite_hubs_item_data
            )

            favorite_hubs.append(favorite_hubs_item)

        show_hubs = d.pop("show_hubs")

        findable_by_allies = d.pop("findable_by_allies")

        approval_status = MeInfoApprovalStatus(d.pop("approval_status"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

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

        me_info = cls(
            public_key=public_key,
            display_name=display_name,
            avatar=avatar,
            bio=bio,
            pronouns=pronouns,
            status_message=status_message,
            activities=activities,
            accent_color=accent_color,
            cover=cover,
            favorite_hubs=favorite_hubs,
            show_hubs=show_hubs,
            findable_by_allies=findable_by_allies,
            approval_status=approval_status,
            roles=roles,
            birthday=birthday,
            name_color=name_color,
        )

        me_info.additional_properties = d
        return me_info

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
