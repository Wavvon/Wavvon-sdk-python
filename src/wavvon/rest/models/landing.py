from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Landing")


@_attrs_define
class Landing:
    """How the invite landing looks (hubs advertising `hub.landing`). Each field is omitted when unset.

    Attributes:
        image (str | Unset): Path of the image on this hub: /hub/landing-image.
        colors (list[str] | Unset):
    """

    image: str | Unset = UNSET
    colors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        colors: list[str] | Unset = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if colors is not UNSET:
            field_dict["colors"] = colors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        image = d.pop("image", UNSET)

        colors = cast(list[str], d.pop("colors", UNSET))

        landing = cls(
            image=image,
            colors=colors,
        )

        landing.additional_properties = d
        return landing

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
