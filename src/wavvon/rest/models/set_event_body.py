from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetEventBody")


@_attrs_define
class SetEventBody:
    """
    Attributes:
        title (str | Unset):
        description (str | Unset):
        starts_at (int | Unset):
        ends_at (int | Unset):
        location (str | Unset):
        reminder_minutes (int | None | Unset):
        hub_wide (bool | Unset):
    """

    title: str | Unset = UNSET
    description: str | Unset = UNSET
    starts_at: int | Unset = UNSET
    ends_at: int | Unset = UNSET
    location: str | Unset = UNSET
    reminder_minutes: int | None | Unset = UNSET
    hub_wide: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        starts_at = self.starts_at

        ends_at = self.ends_at

        location = self.location

        reminder_minutes: int | None | Unset
        if isinstance(self.reminder_minutes, Unset):
            reminder_minutes = UNSET
        else:
            reminder_minutes = self.reminder_minutes

        hub_wide = self.hub_wide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if location is not UNSET:
            field_dict["location"] = location
        if reminder_minutes is not UNSET:
            field_dict["reminder_minutes"] = reminder_minutes
        if hub_wide is not UNSET:
            field_dict["hub_wide"] = hub_wide

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        location = d.pop("location", UNSET)

        def _parse_reminder_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reminder_minutes = _parse_reminder_minutes(d.pop("reminder_minutes", UNSET))

        hub_wide = d.pop("hub_wide", UNSET)

        set_event_body = cls(
            title=title,
            description=description,
            starts_at=starts_at,
            ends_at=ends_at,
            location=location,
            reminder_minutes=reminder_minutes,
            hub_wide=hub_wide,
        )

        set_event_body.additional_properties = d
        return set_event_body

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
