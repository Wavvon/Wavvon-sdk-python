from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        created_by (str | Unset):
        parent_id (None | str | Unset):
        is_category (bool | Unset):
        display_order (int | Unset):
        description (None | str | Unset):
        icon (None | str | Unset):
        color (None | str | Unset):
        custom_icon_svg (None | str | Unset):
        created_at (int | Unset): Unix timestamp
        can_move_members (bool | Unset): The caller's own `voice.move_members` on this channel, resolved channel-scoped,
            so a move-destination picker can offer only the channels that will accept the move (events.md §7.1). Advertised
            as the `channels.move.targets` capability; absent on hubs that do not advertise it, which is not the same as
            `false`.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    created_by: str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    is_category: bool | Unset = UNSET
    display_order: int | Unset = UNSET
    description: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    custom_icon_svg: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    can_move_members: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_by = self.created_by

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        is_category = self.is_category

        display_order = self.display_order

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        created_at = self.created_at

        can_move_members = self.can_move_members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if is_category is not UNSET:
            field_dict["is_category"] = is_category
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if color is not UNSET:
            field_dict["color"] = color
        if custom_icon_svg is not UNSET:
            field_dict["custom_icon_svg"] = custom_icon_svg
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if can_move_members is not UNSET:
            field_dict["can_move_members"] = can_move_members

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        created_by = d.pop("created_by", UNSET)

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        is_category = d.pop("is_category", UNSET)

        display_order = d.pop("display_order", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        created_at = d.pop("created_at", UNSET)

        can_move_members = d.pop("can_move_members", UNSET)

        channel = cls(
            id=id,
            name=name,
            created_by=created_by,
            parent_id=parent_id,
            is_category=is_category,
            display_order=display_order,
            description=description,
            icon=icon,
            color=color,
            custom_icon_svg=custom_icon_svg,
            created_at=created_at,
            can_move_members=can_move_members,
        )

        channel.additional_properties = d
        return channel

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
