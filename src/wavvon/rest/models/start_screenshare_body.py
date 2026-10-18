from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartScreenshareBody")


@_attrs_define
class StartScreenshareBody:
    """
    Attributes:
        channel_id (str):
        kind (str | Unset): e.g. screen, webcam, video Default: 'screen'.
        mime (str | Unset):  Default: 'video/webm'.
        has_audio (bool | Unset):  Default: False.
    """

    channel_id: str
    kind: str | Unset = "screen"
    mime: str | Unset = "video/webm"
    has_audio: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        kind = self.kind

        mime = self.mime

        has_audio = self.has_audio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if mime is not UNSET:
            field_dict["mime"] = mime
        if has_audio is not UNSET:
            field_dict["has_audio"] = has_audio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        kind = d.pop("kind", UNSET)

        mime = d.pop("mime", UNSET)

        has_audio = d.pop("has_audio", UNSET)

        start_screenshare_body = cls(
            channel_id=channel_id,
            kind=kind,
            mime=mime,
            has_audio=has_audio,
        )

        start_screenshare_body.additional_properties = d
        return start_screenshare_body

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
