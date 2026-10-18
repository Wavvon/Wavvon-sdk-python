from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateFederationForumChannelPostBody")


@_attrs_define
class CreateFederationForumChannelPostBody:
    """
    Attributes:
        author_pubkey (str): The remote user the calling hub asserts
        title (str):
        body (str):
    """

    author_pubkey: str
    title: str
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_pubkey = self.author_pubkey

        title = self.title

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_pubkey": author_pubkey,
                "title": title,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        author_pubkey = d.pop("author_pubkey")

        title = d.pop("title")

        body = d.pop("body")

        create_federation_forum_channel_post_body = cls(
            author_pubkey=author_pubkey,
            title=title,
            body=body,
        )

        create_federation_forum_channel_post_body.additional_properties = d
        return create_federation_forum_channel_post_body

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
