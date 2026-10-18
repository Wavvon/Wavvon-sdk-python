from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResponse200Item")


@_attrs_define
class SearchResponse200Item:
    """
    Attributes:
        message_id (str | Unset):
        channel_id (str | Unset):
        channel_name (str | Unset):
        sender (str | Unset):
        sender_name (None | str | Unset):
        content_preview (str | Unset):
        created_at (int | Unset):
    """

    message_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    channel_name: str | Unset = UNSET
    sender: str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    content_preview: str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        channel_id = self.channel_id

        channel_name = self.channel_name

        sender = self.sender

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        content_preview = self.content_preview

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if content_preview is not UNSET:
            field_dict["content_preview"] = content_preview
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message_id = d.pop("message_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        channel_name = d.pop("channel_name", UNSET)

        sender = d.pop("sender", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        content_preview = d.pop("content_preview", UNSET)

        created_at = d.pop("created_at", UNSET)

        search_response_200_item = cls(
            message_id=message_id,
            channel_id=channel_id,
            channel_name=channel_name,
            sender=sender,
            sender_name=sender_name,
            content_preview=content_preview,
            created_at=created_at,
        )

        search_response_200_item.additional_properties = d
        return search_response_200_item

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
