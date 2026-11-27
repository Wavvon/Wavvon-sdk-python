from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HubInfoTheme")


@_attrs_define
class HubInfoTheme:
    """The hub default theme (`hub.theme`), present while one is set. The package is at `/hub/theme/{sha256}` and, when
    `has_preview`, its preview image at `/hub/theme/{sha256}/preview`.

        Attributes:
            sha256 (str): Hex SHA-256 of the package bytes
            has_preview (bool):
    """

    sha256: str
    has_preview: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        has_preview = self.has_preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "has_preview": has_preview,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        has_preview = d.pop("has_preview")

        hub_info_theme = cls(
            sha256=sha256,
            has_preview=has_preview,
        )

        hub_info_theme.additional_properties = d
        return hub_info_theme

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
