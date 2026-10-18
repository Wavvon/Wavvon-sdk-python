from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEventRsvpsResponse200Item")


@_attrs_define
class ListEventRsvpsResponse200Item:
    """
    Attributes:
        user_pubkey (str | Unset):
        status (str | Unset):
    """

    user_pubkey: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_pubkey = self.user_pubkey

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_pubkey is not UNSET:
            field_dict["user_pubkey"] = user_pubkey
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_pubkey = d.pop("user_pubkey", UNSET)

        status = d.pop("status", UNSET)

        list_event_rsvps_response_200_item = cls(
            user_pubkey=user_pubkey,
            status=status,
        )

        list_event_rsvps_response_200_item.additional_properties = d
        return list_event_rsvps_response_200_item

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
