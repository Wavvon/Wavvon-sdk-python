from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameLaunchCard")


@_attrs_define
class GameLaunchCard:
    """
    Attributes:
        entry_url (str):
        name (str):
        description (str | Unset):
        thumbnail_url (str | Unset):
    """

    entry_url: str
    name: str
    description: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_url = self.entry_url

        name = self.name

        description = self.description

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_url": entry_url,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        entry_url = d.pop("entry_url")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        game_launch_card = cls(
            entry_url=entry_url,
            name=name,
            description=description,
            thumbnail_url=thumbnail_url,
        )

        game_launch_card.additional_properties = d
        return game_launch_card

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
