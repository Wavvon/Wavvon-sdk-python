from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.favorite_hub import FavoriteHub


T = TypeVar("T", bound="UpdateMeBody")


@_attrs_define
class UpdateMeBody:
    """
    Attributes:
        display_name (str | Unset):
        avatar (None | str | Unset):
        bio (str | Unset):
        pronouns (str | Unset):
        status_message (str | Unset):
        activities (str | Unset):
        accent_color (str | Unset):
        cover (str | Unset):
        favorite_hubs (list[FavoriteHub] | Unset):
        show_hubs (bool | Unset):
        findable_by_allies (bool | Unset): List me to members of allied hubs (see `GET
            /alliances/{alliance_id}/people`). Per hub, off by default; only takes effect while the alliance's own
            `people_visible` switch is on. Hubs advertising `alliance.people`.
        birthday (str | Unset):
        name_color (str | Unset):
    """

    display_name: str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    bio: str | Unset = UNSET
    pronouns: str | Unset = UNSET
    status_message: str | Unset = UNSET
    activities: str | Unset = UNSET
    accent_color: str | Unset = UNSET
    cover: str | Unset = UNSET
    favorite_hubs: list[FavoriteHub] | Unset = UNSET
    show_hubs: bool | Unset = UNSET
    findable_by_allies: bool | Unset = UNSET
    birthday: str | Unset = UNSET
    name_color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        bio = self.bio

        pronouns = self.pronouns

        status_message = self.status_message

        activities = self.activities

        accent_color = self.accent_color

        cover = self.cover

        favorite_hubs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.favorite_hubs, Unset):
            favorite_hubs = []
            for favorite_hubs_item_data in self.favorite_hubs:
                favorite_hubs_item = favorite_hubs_item_data.to_dict()
                favorite_hubs.append(favorite_hubs_item)

        show_hubs = self.show_hubs

        findable_by_allies = self.findable_by_allies

        birthday = self.birthday

        name_color = self.name_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if bio is not UNSET:
            field_dict["bio"] = bio
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if activities is not UNSET:
            field_dict["activities"] = activities
        if accent_color is not UNSET:
            field_dict["accent_color"] = accent_color
        if cover is not UNSET:
            field_dict["cover"] = cover
        if favorite_hubs is not UNSET:
            field_dict["favorite_hubs"] = favorite_hubs
        if show_hubs is not UNSET:
            field_dict["show_hubs"] = show_hubs
        if findable_by_allies is not UNSET:
            field_dict["findable_by_allies"] = findable_by_allies
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if name_color is not UNSET:
            field_dict["name_color"] = name_color

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.favorite_hub import FavoriteHub

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        bio = d.pop("bio", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        status_message = d.pop("status_message", UNSET)

        activities = d.pop("activities", UNSET)

        accent_color = d.pop("accent_color", UNSET)

        cover = d.pop("cover", UNSET)

        _favorite_hubs = d.pop("favorite_hubs", UNSET)
        favorite_hubs: list[FavoriteHub] | Unset = UNSET
        if _favorite_hubs is not UNSET:
            favorite_hubs = []
            for favorite_hubs_item_data in _favorite_hubs:
                favorite_hubs_item = FavoriteHub.from_dict(favorite_hubs_item_data)

                favorite_hubs.append(favorite_hubs_item)

        show_hubs = d.pop("show_hubs", UNSET)

        findable_by_allies = d.pop("findable_by_allies", UNSET)

        birthday = d.pop("birthday", UNSET)

        name_color = d.pop("name_color", UNSET)

        update_me_body = cls(
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
            birthday=birthday,
            name_color=name_color,
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
