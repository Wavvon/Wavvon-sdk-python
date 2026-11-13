from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnsureChannelStickerBody")


@_attrs_define
class EnsureChannelStickerBody:
    """
    Attributes:
        sha256 (str):
        origin_hub_url (str):
        name (str | Unset):
    """

    sha256: str
    origin_hub_url: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        origin_hub_url = self.origin_hub_url

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "origin_hub_url": origin_hub_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        origin_hub_url = d.pop("origin_hub_url")

        name = d.pop("name", UNSET)

        ensure_channel_sticker_body = cls(
            sha256=sha256,
            origin_hub_url=origin_hub_url,
            name=name,
        )

        ensure_channel_sticker_body.additional_properties = d
        return ensure_channel_sticker_body

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
