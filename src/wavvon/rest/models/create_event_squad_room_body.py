from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEventSquadRoomBody")


@_attrs_define
class CreateEventSquadRoomBody:
    """
    Attributes:
        count (int):
        name_prefix (str | Unset):  Default: 'Squad'.
    """

    count: int
    name_prefix: str | Unset = "Squad"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        name_prefix = self.name_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if name_prefix is not UNSET:
            field_dict["name_prefix"] = name_prefix

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        name_prefix = d.pop("name_prefix", UNSET)

        create_event_squad_room_body = cls(
            count=count,
            name_prefix=name_prefix,
        )

        create_event_squad_room_body.additional_properties = d
        return create_event_squad_room_body

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
