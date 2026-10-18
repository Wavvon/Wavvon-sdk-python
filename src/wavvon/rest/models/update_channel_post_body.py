from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChannelPostBody")


@_attrs_define
class UpdateChannelPostBody:
    """
    Attributes:
        title (str | Unset):
        body (str | Unset):
        tag_ids (list[str] | Unset):
    """

    title: str | Unset = UNSET
    body: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        tag_ids = cast(list[str], d.pop("tag_ids", UNSET))

        update_channel_post_body = cls(
            title=title,
            body=body,
            tag_ids=tag_ids,
        )

        update_channel_post_body.additional_properties = d
        return update_channel_post_body

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
