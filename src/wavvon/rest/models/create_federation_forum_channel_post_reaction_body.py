from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateFederationForumChannelPostReactionBody")


@_attrs_define
class CreateFederationForumChannelPostReactionBody:
    """
    Attributes:
        author_pubkey (str):
        emoji (str):
    """

    author_pubkey: str
    emoji: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_pubkey = self.author_pubkey

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_pubkey": author_pubkey,
                "emoji": emoji,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        author_pubkey = d.pop("author_pubkey")

        emoji = d.pop("emoji")

        create_federation_forum_channel_post_reaction_body = cls(
            author_pubkey=author_pubkey,
            emoji=emoji,
        )

        create_federation_forum_channel_post_reaction_body.additional_properties = d
        return create_federation_forum_channel_post_reaction_body

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
