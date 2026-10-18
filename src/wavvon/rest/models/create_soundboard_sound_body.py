from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateSoundboardSoundBody")


@_attrs_define
class CreateSoundboardSoundBody:
    """
    Attributes:
        name (str):
        audio (File):
        emoji (str | Unset):
    """

    name: str
    audio: File
    emoji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        audio = self.audio.to_tuple()

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "audio": audio,
            }
        )
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("audio", self.audio.to_tuple()))

        if not isinstance(self.emoji, Unset):
            files.append(("emoji", (None, str(self.emoji).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        audio = File(payload=BytesIO(d.pop("audio")))

        emoji = d.pop("emoji", UNSET)

        create_soundboard_sound_body = cls(
            name=name,
            audio=audio,
            emoji=emoji,
        )

        create_soundboard_sound_body.additional_properties = d
        return create_soundboard_sound_body

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
