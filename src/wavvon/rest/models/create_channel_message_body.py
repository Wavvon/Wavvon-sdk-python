from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="CreateChannelMessageBody")


@_attrs_define
class CreateChannelMessageBody:
    """
    Attributes:
        content (str):
        attachments (list[Attachment] | Unset):
        reply_to (str | Unset): Message ID being replied to
    """

    content: str
    attachments: list[Attachment] | Unset = UNSET
    reply_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        reply_to = self.reply_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        content = d.pop("content")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        reply_to = d.pop("reply_to", UNSET)

        create_channel_message_body = cls(
            content=content,
            attachments=attachments,
            reply_to=reply_to,
        )

        create_channel_message_body.additional_properties = d
        return create_channel_message_body

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
