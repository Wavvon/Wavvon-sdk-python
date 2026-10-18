from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_channel_post_reply_body_attachments_item import (
        CreateChannelPostReplyBodyAttachmentsItem,
    )


T = TypeVar("T", bound="CreateChannelPostReplyBody")


@_attrs_define
class CreateChannelPostReplyBody:
    """
    Attributes:
        body (str):
        reply_to_id (str | Unset): Optional parent reply within the same post
        attachments (list[CreateChannelPostReplyBodyAttachmentsItem] | Unset):
    """

    body: str
    reply_to_id: str | Unset = UNSET
    attachments: list[CreateChannelPostReplyBodyAttachmentsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        reply_to_id = self.reply_to_id

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if reply_to_id is not UNSET:
            field_dict["reply_to_id"] = reply_to_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_channel_post_reply_body_attachments_item import (
            CreateChannelPostReplyBodyAttachmentsItem,
        )

        d = dict(src_dict)
        body = d.pop("body")

        reply_to_id = d.pop("reply_to_id", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[CreateChannelPostReplyBodyAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = CreateChannelPostReplyBodyAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        create_channel_post_reply_body = cls(
            body=body,
            reply_to_id=reply_to_id,
            attachments=attachments,
        )

        create_channel_post_reply_body.additional_properties = d
        return create_channel_post_reply_body

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
