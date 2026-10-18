from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embed import Embed


T = TypeVar("T", bound="UpdateChannelMessageBody")


@_attrs_define
class UpdateChannelMessageBody:
    """
    Attributes:
        content (str):
        embeds (list[Embed] | Unset):
    """

    content: str
    embeds: list[Embed] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        embeds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.embeds, Unset):
            embeds = []
            for embeds_item_data in self.embeds:
                embeds_item = embeds_item_data.to_dict()
                embeds.append(embeds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if embeds is not UNSET:
            field_dict["embeds"] = embeds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed import Embed

        d = dict(src_dict)
        content = d.pop("content")

        _embeds = d.pop("embeds", UNSET)
        embeds: list[Embed] | Unset = UNSET
        if _embeds is not UNSET:
            embeds = []
            for embeds_item_data in _embeds:
                embeds_item = Embed.from_dict(embeds_item_data)

                embeds.append(embeds_item)

        update_channel_message_body = cls(
            content=content,
            embeds=embeds,
        )

        update_channel_message_body.additional_properties = d
        return update_channel_message_body

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
