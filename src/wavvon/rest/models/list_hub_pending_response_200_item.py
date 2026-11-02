from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListHubPendingResponse200Item")


@_attrs_define
class ListHubPendingResponse200Item:
    """
    Attributes:
        public_key (str):
        first_seen_at (int):
        display_name (None | str | Unset):
        has_application (bool | Unset): Whether they filled the join application.
        ban_evasion_match (None | str | Unset): The banned identity whose last address this joiner arrived from, when
            that is why they wait. Approving clears it. Present on hubs advertising `admission.banevasion`.
    """

    public_key: str
    first_seen_at: int
    display_name: None | str | Unset = UNSET
    has_application: bool | Unset = UNSET
    ban_evasion_match: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        first_seen_at = self.first_seen_at

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        has_application = self.has_application

        ban_evasion_match: None | str | Unset
        if isinstance(self.ban_evasion_match, Unset):
            ban_evasion_match = UNSET
        else:
            ban_evasion_match = self.ban_evasion_match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "first_seen_at": first_seen_at,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if has_application is not UNSET:
            field_dict["has_application"] = has_application
        if ban_evasion_match is not UNSET:
            field_dict["ban_evasion_match"] = ban_evasion_match

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_key = d.pop("public_key")

        first_seen_at = d.pop("first_seen_at")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        has_application = d.pop("has_application", UNSET)

        def _parse_ban_evasion_match(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ban_evasion_match = _parse_ban_evasion_match(d.pop("ban_evasion_match", UNSET))

        list_hub_pending_response_200_item = cls(
            public_key=public_key,
            first_seen_at=first_seen_at,
            display_name=display_name,
            has_application=has_application,
            ban_evasion_match=ban_evasion_match,
        )

        list_hub_pending_response_200_item.additional_properties = d
        return list_hub_pending_response_200_item

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
