from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rsvp_event_body_status import RsvpEventBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RsvpEventBody")


@_attrs_define
class RsvpEventBody:
    """
    Attributes:
        status (RsvpEventBodyStatus):
        slot_id (str | Unset):
    """

    status: RsvpEventBodyStatus
    slot_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        slot_id = self.slot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if slot_id is not UNSET:
            field_dict["slot_id"] = slot_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = RsvpEventBodyStatus(d.pop("status"))

        slot_id = d.pop("slot_id", UNSET)

        rsvp_event_body = cls(
            status=status,
            slot_id=slot_id,
        )

        rsvp_event_body.additional_properties = d
        return rsvp_event_body

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
