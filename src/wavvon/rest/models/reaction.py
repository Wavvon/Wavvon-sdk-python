from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reaction")


@_attrs_define
class Reaction:
    """
    Attributes:
        emoji (str | Unset):
        count (int | Unset):
        me (bool | Unset):
    """

    emoji: str | Unset = UNSET
    count: int | Unset = UNSET
    me: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emoji = self.emoji

        count = self.count

        me = self.me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if count is not UNSET:
            field_dict["count"] = count
        if me is not UNSET:
            field_dict["me"] = me

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        emoji = d.pop("emoji", UNSET)

        count = d.pop("count", UNSET)

        me = d.pop("me", UNSET)

        reaction = cls(
            emoji=emoji,
            count=count,
            me=me,
        )

        reaction.additional_properties = d
        return reaction

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
