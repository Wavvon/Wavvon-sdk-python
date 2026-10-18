from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_channel_pins_response_200_item_message import (
        ListChannelPinsResponse200ItemMessage,
    )


T = TypeVar("T", bound="ListChannelPinsResponse200Item")


@_attrs_define
class ListChannelPinsResponse200Item:
    """
    Attributes:
        message_id (str | Unset):
        pinned_by (str | Unset):
        pinned_at (int | Unset):
        message (ListChannelPinsResponse200ItemMessage | Unset):
    """

    message_id: str | Unset = UNSET
    pinned_by: str | Unset = UNSET
    pinned_at: int | Unset = UNSET
    message: ListChannelPinsResponse200ItemMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        pinned_by = self.pinned_by

        pinned_at = self.pinned_at

        message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if pinned_by is not UNSET:
            field_dict["pinned_by"] = pinned_by
        if pinned_at is not UNSET:
            field_dict["pinned_at"] = pinned_at
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_channel_pins_response_200_item_message import (
            ListChannelPinsResponse200ItemMessage,
        )

        d = dict(src_dict)
        message_id = d.pop("message_id", UNSET)

        pinned_by = d.pop("pinned_by", UNSET)

        pinned_at = d.pop("pinned_at", UNSET)

        _message = d.pop("message", UNSET)
        message: ListChannelPinsResponse200ItemMessage | Unset
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ListChannelPinsResponse200ItemMessage.from_dict(_message)

        list_channel_pins_response_200_item = cls(
            message_id=message_id,
            pinned_by=pinned_by,
            pinned_at=pinned_at,
            message=message,
        )

        list_channel_pins_response_200_item.additional_properties = d
        return list_channel_pins_response_200_item

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
