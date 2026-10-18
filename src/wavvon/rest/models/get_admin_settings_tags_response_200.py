from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAdminSettingsTagsResponse200")


@_attrs_define
class GetAdminSettingsTagsResponse200:
    """
    Attributes:
        tags (list[str] | Unset):
        nsfw (bool | Unset):
    """

    tags: list[str] | Unset = UNSET
    nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        nsfw = self.nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if nsfw is not UNSET:
            field_dict["nsfw"] = nsfw

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        nsfw = d.pop("nsfw", UNSET)

        get_admin_settings_tags_response_200 = cls(
            tags=tags,
            nsfw=nsfw,
        )

        get_admin_settings_tags_response_200.additional_properties = d
        return get_admin_settings_tags_response_200

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
