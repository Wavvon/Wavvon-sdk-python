from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListChannelPinsResponse200ItemMessage")


@_attrs_define
class ListChannelPinsResponse200ItemMessage:
    """
    Attributes:
        id (str | Unset):
        content (str | Unset):
        sender (str | Unset):
        sender_name (None | str | Unset):
        created_at (int | Unset):
    """

    id: str | Unset = UNSET
    content: str | Unset = UNSET
    sender: str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        sender = self.sender

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if content is not UNSET:
            field_dict["content"] = content
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        content = d.pop("content", UNSET)

        sender = d.pop("sender", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        created_at = d.pop("created_at", UNSET)

        list_channel_pins_response_200_item_message = cls(
            id=id,
            content=content,
            sender=sender,
            sender_name=sender_name,
            created_at=created_at,
        )

        list_channel_pins_response_200_item_message.additional_properties = d
        return list_channel_pins_response_200_item_message

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
