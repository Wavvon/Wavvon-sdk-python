from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VotePollBody")


@_attrs_define
class VotePollBody:
    """
    Attributes:
        option_ids (list[str]): Must not exceed the poll's max_choices
    """

    option_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_ids = self.option_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option_ids": option_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        option_ids = cast(list[str], d.pop("option_ids"))

        vote_poll_body = cls(
            option_ids=option_ids,
        )

        vote_poll_body.additional_properties = d
        return vote_poll_body

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
