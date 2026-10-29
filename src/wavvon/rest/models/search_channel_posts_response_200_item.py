from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchChannelPostsResponse200Item")


@_attrs_define
class SearchChannelPostsResponse200Item:
    """
    Attributes:
        post_id (str | Unset):
        title_snippet (str | Unset):
        body_snippet (str | Unset):
        is_reply (bool | Unset):
        reply_id (str | Unset):
    """

    post_id: str | Unset = UNSET
    title_snippet: str | Unset = UNSET
    body_snippet: str | Unset = UNSET
    is_reply: bool | Unset = UNSET
    reply_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        title_snippet = self.title_snippet

        body_snippet = self.body_snippet

        is_reply = self.is_reply

        reply_id = self.reply_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if title_snippet is not UNSET:
            field_dict["title_snippet"] = title_snippet
        if body_snippet is not UNSET:
            field_dict["body_snippet"] = body_snippet
        if is_reply is not UNSET:
            field_dict["is_reply"] = is_reply
        if reply_id is not UNSET:
            field_dict["reply_id"] = reply_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        post_id = d.pop("post_id", UNSET)

        title_snippet = d.pop("title_snippet", UNSET)

        body_snippet = d.pop("body_snippet", UNSET)

        is_reply = d.pop("is_reply", UNSET)

        reply_id = d.pop("reply_id", UNSET)

        search_channel_posts_response_200_item = cls(
            post_id=post_id,
            title_snippet=title_snippet,
            body_snippet=body_snippet,
            is_reply=is_reply,
            reply_id=reply_id,
        )

        search_channel_posts_response_200_item.additional_properties = d
        return search_channel_posts_response_200_item

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
