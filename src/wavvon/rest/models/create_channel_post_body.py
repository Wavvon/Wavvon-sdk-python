from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_channel_post_body_attachments_item import (
        CreateChannelPostBodyAttachmentsItem,
    )


T = TypeVar("T", bound="CreateChannelPostBody")


@_attrs_define
class CreateChannelPostBody:
    """
    Attributes:
        title (str):
        body (str):
        attachments (list[CreateChannelPostBodyAttachmentsItem] | Unset):
        tag_ids (list[str] | Unset):
    """

    title: str
    body: str
    attachments: list[CreateChannelPostBodyAttachmentsItem] | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "body": body,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_channel_post_body_attachments_item import (
            CreateChannelPostBodyAttachmentsItem,
        )

        d = dict(src_dict)
        title = d.pop("title")

        body = d.pop("body")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[CreateChannelPostBodyAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = CreateChannelPostBodyAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        tag_ids = cast(list[str], d.pop("tag_ids", UNSET))

        create_channel_post_body = cls(
            title=title,
            body=body,
            attachments=attachments,
            tag_ids=tag_ids,
        )

        create_channel_post_body.additional_properties = d
        return create_channel_post_body

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
