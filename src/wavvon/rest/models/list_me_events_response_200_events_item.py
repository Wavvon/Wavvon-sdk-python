from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListMeEventsResponse200EventsItem")


@_attrs_define
class ListMeEventsResponse200EventsItem:
    """
    Attributes:
        id (str):
        event_type (str):
        payload (str): The event payload as a JSON-encoded string; parse it
        created_at (int): Unix seconds
    """

    id: str
    event_type: str
    payload: str
    created_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_type = self.event_type

        payload = self.payload

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_type": event_type,
                "payload": payload,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        event_type = d.pop("event_type")

        payload = d.pop("payload")

        created_at = d.pop("created_at")

        list_me_events_response_200_events_item = cls(
            id=id,
            event_type=event_type,
            payload=payload,
            created_at=created_at,
        )

        list_me_events_response_200_events_item.additional_properties = d
        return list_me_events_response_200_events_item

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
