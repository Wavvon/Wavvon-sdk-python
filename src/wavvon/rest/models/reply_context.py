from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplyContext")


@_attrs_define
class ReplyContext:
    """
    Attributes:
        message_id (str | Unset):
        sender (str | Unset):
        sender_name (None | str | Unset):
        content_preview (str | Unset):
    """

    message_id: str | Unset = UNSET
    sender: str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    content_preview: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        sender = self.sender

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        content_preview = self.content_preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if content_preview is not UNSET:
            field_dict["content_preview"] = content_preview

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message_id = d.pop("message_id", UNSET)

        sender = d.pop("sender", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        content_preview = d.pop("content_preview", UNSET)

        reply_context = cls(
            message_id=message_id,
            sender=sender,
            sender_name=sender_name,
            content_preview=content_preview,
        )

        reply_context.additional_properties = d
        return reply_context

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
