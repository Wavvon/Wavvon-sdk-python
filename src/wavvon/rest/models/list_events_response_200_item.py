from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_events_response_200_item_my_rsvp import (
    ListEventsResponse200ItemMyRsvp,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_events_response_200_item_rsvp_counts import (
        ListEventsResponse200ItemRsvpCounts,
    )


T = TypeVar("T", bound="ListEventsResponse200Item")


@_attrs_define
class ListEventsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        creator_pubkey (str | Unset):
        title (str | Unset):
        description (str | Unset):
        starts_at (int | Unset):
        ends_at (int | None | Unset):
        location (None | str | Unset):
        created_at (int | Unset):
        rsvp_counts (ListEventsResponse200ItemRsvpCounts | Unset):
        my_rsvp (ListEventsResponse200ItemMyRsvp | Unset): The caller's own RSVP; absent when they have none.
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    creator_pubkey: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    starts_at: int | Unset = UNSET
    ends_at: int | None | Unset = UNSET
    location: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    rsvp_counts: ListEventsResponse200ItemRsvpCounts | Unset = UNSET
    my_rsvp: ListEventsResponse200ItemMyRsvp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        creator_pubkey = self.creator_pubkey

        title = self.title

        description = self.description

        starts_at = self.starts_at

        ends_at: int | None | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = self.ends_at

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        created_at = self.created_at

        rsvp_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rsvp_counts, Unset):
            rsvp_counts = self.rsvp_counts.to_dict()

        my_rsvp: str | Unset = UNSET
        if not isinstance(self.my_rsvp, Unset):
            my_rsvp = self.my_rsvp.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if creator_pubkey is not UNSET:
            field_dict["creator_pubkey"] = creator_pubkey
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if rsvp_counts is not UNSET:
            field_dict["rsvp_counts"] = rsvp_counts
        if my_rsvp is not UNSET:
            field_dict["my_rsvp"] = my_rsvp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_events_response_200_item_rsvp_counts import (
            ListEventsResponse200ItemRsvpCounts,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        creator_pubkey = d.pop("creator_pubkey", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        def _parse_ends_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        created_at = d.pop("created_at", UNSET)

        _rsvp_counts = d.pop("rsvp_counts", UNSET)
        rsvp_counts: ListEventsResponse200ItemRsvpCounts | Unset
        if isinstance(_rsvp_counts, Unset):
            rsvp_counts = UNSET
        else:
            rsvp_counts = ListEventsResponse200ItemRsvpCounts.from_dict(_rsvp_counts)

        _my_rsvp = d.pop("my_rsvp", UNSET)
        my_rsvp: ListEventsResponse200ItemMyRsvp | Unset
        if isinstance(_my_rsvp, Unset):
            my_rsvp = UNSET
        else:
            my_rsvp = ListEventsResponse200ItemMyRsvp(_my_rsvp)

        list_events_response_200_item = cls(
            id=id,
            channel_id=channel_id,
            creator_pubkey=creator_pubkey,
            title=title,
            description=description,
            starts_at=starts_at,
            ends_at=ends_at,
            location=location,
            created_at=created_at,
            rsvp_counts=rsvp_counts,
            my_rsvp=my_rsvp,
        )

        list_events_response_200_item.additional_properties = d
        return list_events_response_200_item

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
