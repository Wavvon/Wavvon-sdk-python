from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_channel_poll_body_options_item import (
        CreateChannelPollBodyOptionsItem,
    )


T = TypeVar("T", bound="CreateChannelPollBody")


@_attrs_define
class CreateChannelPollBody:
    """
    Attributes:
        question (str):
        options (list[CreateChannelPollBodyOptionsItem]):
        ends_at (int | None | Unset):
        max_choices (int | Unset):  Default: 1.
    """

    question: str
    options: list[CreateChannelPollBodyOptionsItem]
    ends_at: int | None | Unset = UNSET
    max_choices: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question = self.question

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        ends_at: int | None | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = self.ends_at

        max_choices = self.max_choices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question": question,
                "options": options,
            }
        )
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if max_choices is not UNSET:
            field_dict["max_choices"] = max_choices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_channel_poll_body_options_item import (
            CreateChannelPollBodyOptionsItem,
        )

        d = dict(src_dict)
        question = d.pop("question")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CreateChannelPollBodyOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        def _parse_ends_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

        max_choices = d.pop("max_choices", UNSET)

        create_channel_poll_body = cls(
            question=question,
            options=options,
            ends_at=ends_at,
            max_choices=max_choices,
        )

        create_channel_poll_body.additional_properties = d
        return create_channel_poll_body

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
