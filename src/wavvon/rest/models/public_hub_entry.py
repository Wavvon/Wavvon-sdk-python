from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicHubEntry")


@_attrs_define
class PublicHubEntry:
    """
    Attributes:
        hub_url (str):
        hub_name (str):
        joined_at (int):
    """

    hub_url: str
    hub_name: str
    joined_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub_url = self.hub_url

        hub_name = self.hub_name

        joined_at = self.joined_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hub_url": hub_url,
                "hub_name": hub_name,
                "joined_at": joined_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hub_url = d.pop("hub_url")

        hub_name = d.pop("hub_name")

        joined_at = d.pop("joined_at")

        public_hub_entry = cls(
            hub_url=hub_url,
            hub_name=hub_name,
            joined_at=joined_at,
        )

        public_hub_entry.additional_properties = d
        return public_hub_entry

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
