from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embed_field import EmbedField
    from ..models.embed_footer import EmbedFooter


T = TypeVar("T", bound="Embed")


@_attrs_define
class Embed:
    """
    Attributes:
        title (str | Unset):
        url (str | Unset):
        description (str | Unset):
        color (str | Unset):
        fields (list[EmbedField] | Unset):
        thumbnail_url (str | Unset):
        image_url (str | Unset):
        footer (EmbedFooter | Unset):
    """

    title: str | Unset = UNSET
    url: str | Unset = UNSET
    description: str | Unset = UNSET
    color: str | Unset = UNSET
    fields: list[EmbedField] | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    image_url: str | Unset = UNSET
    footer: EmbedFooter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        description = self.description

        color = self.color

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        thumbnail_url = self.thumbnail_url

        image_url = self.image_url

        footer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footer, Unset):
            footer = self.footer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if fields is not UNSET:
            field_dict["fields"] = fields
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if footer is not UNSET:
            field_dict["footer"] = footer

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed_field import EmbedField
        from ..models.embed_footer import EmbedFooter

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[EmbedField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = EmbedField.from_dict(fields_item_data)

                fields.append(fields_item)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        image_url = d.pop("image_url", UNSET)

        _footer = d.pop("footer", UNSET)
        footer: EmbedFooter | Unset
        if isinstance(_footer, Unset):
            footer = UNSET
        else:
            footer = EmbedFooter.from_dict(_footer)

        embed = cls(
            title=title,
            url=url,
            description=description,
            color=color,
            fields=fields,
            thumbnail_url=thumbnail_url,
            image_url=image_url,
            footer=footer,
        )

        embed.additional_properties = d
        return embed

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
