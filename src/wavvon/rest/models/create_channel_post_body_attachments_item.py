from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateChannelPostBodyAttachmentsItem")


@_attrs_define
class CreateChannelPostBodyAttachmentsItem:
    """
    Attributes:
        url (str):
        name (str):
        mime (str):
        size (int):
    """

    url: str
    name: str
    mime: str
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        name = self.name

        mime = self.mime

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "name": name,
                "mime": mime,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        name = d.pop("name")

        mime = d.pop("mime")

        size = d.pop("size")

        create_channel_post_body_attachments_item = cls(
            url=url,
            name=name,
            mime=mime,
            size=size,
        )

        create_channel_post_body_attachments_item.additional_properties = d
        return create_channel_post_body_attachments_item

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
