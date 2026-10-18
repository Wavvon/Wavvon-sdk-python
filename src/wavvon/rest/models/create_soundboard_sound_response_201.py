from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSoundboardSoundResponse201")


@_attrs_define
class CreateSoundboardSoundResponse201:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        emoji (None | str | Unset):
        uploader (str | Unset):
        size_bytes (int | Unset):
        duration_ms (int | Unset):
        created_at (int | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    emoji: None | str | Unset = UNSET
    uploader: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    duration_ms: int | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        emoji: None | str | Unset
        if isinstance(self.emoji, Unset):
            emoji = UNSET
        else:
            emoji = self.emoji

        uploader = self.uploader

        size_bytes = self.size_bytes

        duration_ms = self.duration_ms

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if uploader is not UNSET:
            field_dict["uploader"] = uploader
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_emoji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        emoji = _parse_emoji(d.pop("emoji", UNSET))

        uploader = d.pop("uploader", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        created_at = d.pop("created_at", UNSET)

        create_soundboard_sound_response_201 = cls(
            id=id,
            name=name,
            emoji=emoji,
            uploader=uploader,
            size_bytes=size_bytes,
            duration_ms=duration_ms,
            created_at=created_at,
        )

        create_soundboard_sound_response_201.additional_properties = d
        return create_soundboard_sound_response_201

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
