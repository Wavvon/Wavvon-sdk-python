from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChannelBody")


@_attrs_define
class CreateChannelBody:
    """
    Attributes:
        name (str):
        parent_id (None | str | Unset):
        is_category (bool | Unset):
        description (str | Unset):
        channel_type (str | Unset):
        banner_url (str | Unset):
        banner_file_id (str | Unset):
        spawner_name_template (str | Unset):
        nsfw (bool | Unset):
    """

    name: str
    parent_id: None | str | Unset = UNSET
    is_category: bool | Unset = UNSET
    description: str | Unset = UNSET
    channel_type: str | Unset = UNSET
    banner_url: str | Unset = UNSET
    banner_file_id: str | Unset = UNSET
    spawner_name_template: str | Unset = UNSET
    nsfw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        is_category = self.is_category

        description = self.description

        channel_type = self.channel_type

        banner_url = self.banner_url

        banner_file_id = self.banner_file_id

        spawner_name_template = self.spawner_name_template

        nsfw = self.nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if is_category is not UNSET:
            field_dict["is_category"] = is_category
        if description is not UNSET:
            field_dict["description"] = description
        if channel_type is not UNSET:
            field_dict["channel_type"] = channel_type
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
        if banner_file_id is not UNSET:
            field_dict["banner_file_id"] = banner_file_id
        if spawner_name_template is not UNSET:
            field_dict["spawner_name_template"] = spawner_name_template
        if nsfw is not UNSET:
            field_dict["nsfw"] = nsfw

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        is_category = d.pop("is_category", UNSET)

        description = d.pop("description", UNSET)

        channel_type = d.pop("channel_type", UNSET)

        banner_url = d.pop("banner_url", UNSET)

        banner_file_id = d.pop("banner_file_id", UNSET)

        spawner_name_template = d.pop("spawner_name_template", UNSET)

        nsfw = d.pop("nsfw", UNSET)

        create_channel_body = cls(
            name=name,
            parent_id=parent_id,
            is_category=is_category,
            description=description,
            channel_type=channel_type,
            banner_url=banner_url,
            banner_file_id=banner_file_id,
            spawner_name_template=spawner_name_template,
            nsfw=nsfw,
        )

        create_channel_body.additional_properties = d
        return create_channel_body

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
