from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEventBody")


@_attrs_define
class CreateEventBody:
    """
    Attributes:
        channel_id (str):
        title (str):
        starts_at (int): Unix timestamp
        description (str | Unset):
        ends_at (int | Unset):
        location (str | Unset):
    """

    channel_id: str
    title: str
    starts_at: int
    description: str | Unset = UNSET
    ends_at: int | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        title = self.title

        starts_at = self.starts_at

        description = self.description

        ends_at = self.ends_at

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "title": title,
                "starts_at": starts_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        title = d.pop("title")

        starts_at = d.pop("starts_at")

        description = d.pop("description", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        location = d.pop("location", UNSET)

        create_event_body = cls(
            channel_id=channel_id,
            title=title,
            starts_at=starts_at,
            description=description,
            ends_at=ends_at,
            location=location,
        )

        create_event_body.additional_properties = d
        return create_event_body

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
