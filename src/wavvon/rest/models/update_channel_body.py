from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_channel_body_channel_type import UpdateChannelBodyChannelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChannelBody")


@_attrs_define
class UpdateChannelBody:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        parent_id (None | str | Unset):
        icon (None | str | Unset):
        color (None | str | Unset):
        custom_icon_svg (None | str | Unset):
        min_talk_power (int | Unset):
        retention_days (int | None | Unset):
        banner_url (str | Unset):
        banner_file_id (str | Unset):
        forum_require_tag (bool | Unset):
        nsfw (bool | Unset):
        channel_type (UpdateChannelBodyChannelType | Unset): Switch between text and voice; both keep their chat.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    custom_icon_svg: None | str | Unset = UNSET
    min_talk_power: int | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    banner_url: str | Unset = UNSET
    banner_file_id: str | Unset = UNSET
    forum_require_tag: bool | Unset = UNSET
    nsfw: bool | Unset = UNSET
    channel_type: UpdateChannelBodyChannelType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        custom_icon_svg: None | str | Unset
        if isinstance(self.custom_icon_svg, Unset):
            custom_icon_svg = UNSET
        else:
            custom_icon_svg = self.custom_icon_svg

        min_talk_power = self.min_talk_power

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        banner_url = self.banner_url

        banner_file_id = self.banner_file_id

        forum_require_tag = self.forum_require_tag

        nsfw = self.nsfw

        channel_type: str | Unset = UNSET
        if not isinstance(self.channel_type, Unset):
            channel_type = self.channel_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if icon is not UNSET:
            field_dict["icon"] = icon
        if color is not UNSET:
            field_dict["color"] = color
        if custom_icon_svg is not UNSET:
            field_dict["custom_icon_svg"] = custom_icon_svg
        if min_talk_power is not UNSET:
            field_dict["min_talk_power"] = min_talk_power
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
        if banner_file_id is not UNSET:
            field_dict["banner_file_id"] = banner_file_id
        if forum_require_tag is not UNSET:
            field_dict["forum_require_tag"] = forum_require_tag
        if nsfw is not UNSET:
            field_dict["nsfw"] = nsfw
        if channel_type is not UNSET:
            field_dict["channel_type"] = channel_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_custom_icon_svg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_icon_svg = _parse_custom_icon_svg(d.pop("custom_icon_svg", UNSET))

        min_talk_power = d.pop("min_talk_power", UNSET)

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        banner_url = d.pop("banner_url", UNSET)

        banner_file_id = d.pop("banner_file_id", UNSET)

        forum_require_tag = d.pop("forum_require_tag", UNSET)

        nsfw = d.pop("nsfw", UNSET)

        _channel_type = d.pop("channel_type", UNSET)
        channel_type: UpdateChannelBodyChannelType | Unset
        if isinstance(_channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = UpdateChannelBodyChannelType(_channel_type)

        update_channel_body = cls(
            name=name,
            description=description,
            parent_id=parent_id,
            icon=icon,
            color=color,
            custom_icon_svg=custom_icon_svg,
            min_talk_power=min_talk_power,
            retention_days=retention_days,
            banner_url=banner_url,
            banner_file_id=banner_file_id,
            forum_require_tag=forum_require_tag,
            nsfw=nsfw,
            channel_type=channel_type,
        )

        update_channel_body.additional_properties = d
        return update_channel_body

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
