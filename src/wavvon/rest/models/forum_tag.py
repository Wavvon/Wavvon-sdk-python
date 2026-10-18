from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForumTag")


@_attrs_define
class ForumTag:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        label (str | Unset):
        color (None | str | Unset):
        position (int | Unset):
        created_at (int | Unset):
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    label: str | Unset = UNSET
    color: None | str | Unset = UNSET
    position: int | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        label = self.label

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position = self.position

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if label is not UNSET:
            field_dict["label"] = label
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        label = d.pop("label", UNSET)

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        position = d.pop("position", UNSET)

        created_at = d.pop("created_at", UNSET)

        forum_tag = cls(
            id=id,
            channel_id=channel_id,
            label=label,
            color=color,
            position=position,
            created_at=created_at,
        )

        forum_tag.additional_properties = d
        return forum_tag

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
