from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteFederationForumChannelPostReplyBody")


@_attrs_define
class DeleteFederationForumChannelPostReplyBody:
    """
    Attributes:
        author_pubkey (str):
    """

    author_pubkey: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_pubkey = self.author_pubkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_pubkey": author_pubkey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        author_pubkey = d.pop("author_pubkey")

        delete_federation_forum_channel_post_reply_body = cls(
            author_pubkey=author_pubkey,
        )

        delete_federation_forum_channel_post_reply_body.additional_properties = d
        return delete_federation_forum_channel_post_reply_body

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
