from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEventSlotResponse200")


@_attrs_define
class UpdateEventSlotResponse200:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        capacity (int | None | Unset):
        position (int | Unset):
        claimed (int | Unset):
        claimants (list[str] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    capacity: int | None | Unset = UNSET
    position: int | Unset = UNSET
    claimed: int | Unset = UNSET
    claimants: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        position = self.position

        claimed = self.claimed

        claimants: list[str] | Unset = UNSET
        if not isinstance(self.claimants, Unset):
            claimants = self.claimants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if position is not UNSET:
            field_dict["position"] = position
        if claimed is not UNSET:
            field_dict["claimed"] = claimed
        if claimants is not UNSET:
            field_dict["claimants"] = claimants

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        position = d.pop("position", UNSET)

        claimed = d.pop("claimed", UNSET)

        claimants = cast(list[str], d.pop("claimants", UNSET))

        update_event_slot_response_200 = cls(
            id=id,
            name=name,
            capacity=capacity,
            position=position,
            claimed=claimed,
            claimants=claimants,
        )

        update_event_slot_response_200.additional_properties = d
        return update_event_slot_response_200

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
