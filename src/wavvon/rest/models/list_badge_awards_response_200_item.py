from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListBadgeAwardsResponse200Item")


@_attrs_define
class ListBadgeAwardsResponse200Item:
    """
    Attributes:
        subject_pubkey (str):
        level (int):
        awarded_at (int):
    """

    subject_pubkey: str
    level: int
    awarded_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_pubkey = self.subject_pubkey

        level = self.level

        awarded_at = self.awarded_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_pubkey": subject_pubkey,
                "level": level,
                "awarded_at": awarded_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        subject_pubkey = d.pop("subject_pubkey")

        level = d.pop("level")

        awarded_at = d.pop("awarded_at")

        list_badge_awards_response_200_item = cls(
            subject_pubkey=subject_pubkey,
            level=level,
            awarded_at=awarded_at,
        )

        list_badge_awards_response_200_item.additional_properties = d
        return list_badge_awards_response_200_item

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
