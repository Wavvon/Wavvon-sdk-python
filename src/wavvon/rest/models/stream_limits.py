from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamLimits")


@_attrs_define
class StreamLimits:
    """The most a screen share or camera may declare in `screen_share_start` (hubs advertising `screenshare.limits`). Each
    field is omitted when uncapped. Read-only on `/info` and `GET /hub/settings`; in `PATCH /hub` the object replaces
    all four, and a field left out or 0 clears it.

        Attributes:
            max_width (int | Unset):
            max_height (int | Unset):
            max_fps (int | Unset):
            max_kbps (int | Unset):
    """

    max_width: int | Unset = UNSET
    max_height: int | Unset = UNSET
    max_fps: int | Unset = UNSET
    max_kbps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_width = self.max_width

        max_height = self.max_height

        max_fps = self.max_fps

        max_kbps = self.max_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_width is not UNSET:
            field_dict["max_width"] = max_width
        if max_height is not UNSET:
            field_dict["max_height"] = max_height
        if max_fps is not UNSET:
            field_dict["max_fps"] = max_fps
        if max_kbps is not UNSET:
            field_dict["max_kbps"] = max_kbps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_width = d.pop("max_width", UNSET)

        max_height = d.pop("max_height", UNSET)

        max_fps = d.pop("max_fps", UNSET)

        max_kbps = d.pop("max_kbps", UNSET)

        stream_limits = cls(
            max_width=max_width,
            max_height=max_height,
            max_fps=max_fps,
            max_kbps=max_kbps,
        )

        stream_limits.additional_properties = d
        return stream_limits

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
