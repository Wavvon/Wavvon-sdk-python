from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminSettingsTagsBody")


@_attrs_define
class UpdateAdminSettingsTagsBody:
    """
    Attributes:
        tags (list[str]):
        nsfw (bool | Unset):
    """

    tags: list[str]
    nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        nsfw = self.nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )
        if nsfw is not UNSET:
            field_dict["nsfw"] = nsfw

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags"))

        nsfw = d.pop("nsfw", UNSET)

        update_admin_settings_tags_body = cls(
            tags=tags,
            nsfw=nsfw,
        )

        update_admin_settings_tags_body.additional_properties = d
        return update_admin_settings_tags_body

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
