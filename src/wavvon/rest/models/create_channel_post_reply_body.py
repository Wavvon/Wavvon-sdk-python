from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChannelPostReplyBody")


@_attrs_define
class CreateChannelPostReplyBody:
    """
    Attributes:
        body (str):
        reply_to_id (str | Unset): Optional parent reply within the same post
        attachment_ids (list[str] | Unset): Uploads to this channel; see POST /channels/{channel_id}/posts.
    """

    body: str
    reply_to_id: str | Unset = UNSET
    attachment_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        reply_to_id = self.reply_to_id

        attachment_ids: list[str] | Unset = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = self.attachment_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if reply_to_id is not UNSET:
            field_dict["reply_to_id"] = reply_to_id
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body = d.pop("body")

        reply_to_id = d.pop("reply_to_id", UNSET)

        attachment_ids = cast(list[str], d.pop("attachment_ids", UNSET))

        create_channel_post_reply_body = cls(
            body=body,
            reply_to_id=reply_to_id,
            attachment_ids=attachment_ids,
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
