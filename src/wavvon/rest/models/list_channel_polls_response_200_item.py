from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_channel_polls_response_200_item_totals import (
        ListChannelPollsResponse200ItemTotals,
    )


T = TypeVar("T", bound="ListChannelPollsResponse200Item")


@_attrs_define
class ListChannelPollsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        creator_pubkey (str | Unset):
        question (str | Unset):
        options (str | Unset): JSON-encoded array of {id, text}
        ends_at (int | None | Unset):
        max_choices (int | Unset):
        created_at (int | Unset):
        totals (ListChannelPollsResponse200ItemTotals | Unset): option_id → vote count
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    creator_pubkey: str | Unset = UNSET
    question: str | Unset = UNSET
    options: str | Unset = UNSET
    ends_at: int | None | Unset = UNSET
    max_choices: int | Unset = UNSET
    created_at: int | Unset = UNSET
    totals: ListChannelPollsResponse200ItemTotals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        creator_pubkey = self.creator_pubkey

        question = self.question

        options = self.options

        ends_at: int | None | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = self.ends_at

        max_choices = self.max_choices

        created_at = self.created_at

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if creator_pubkey is not UNSET:
            field_dict["creator_pubkey"] = creator_pubkey
        if question is not UNSET:
            field_dict["question"] = question
        if options is not UNSET:
            field_dict["options"] = options
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if max_choices is not UNSET:
            field_dict["max_choices"] = max_choices
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_channel_polls_response_200_item_totals import (
            ListChannelPollsResponse200ItemTotals,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        creator_pubkey = d.pop("creator_pubkey", UNSET)

        question = d.pop("question", UNSET)

        options = d.pop("options", UNSET)

        def _parse_ends_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

        max_choices = d.pop("max_choices", UNSET)

        created_at = d.pop("created_at", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: ListChannelPollsResponse200ItemTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = ListChannelPollsResponse200ItemTotals.from_dict(_totals)

        list_channel_polls_response_200_item = cls(
            id=id,
            channel_id=channel_id,
            creator_pubkey=creator_pubkey,
            question=question,
            options=options,
            ends_at=ends_at,
            max_choices=max_choices,
            created_at=created_at,
            totals=totals,
        )

        list_channel_polls_response_200_item.additional_properties = d
        return list_channel_polls_response_200_item

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
