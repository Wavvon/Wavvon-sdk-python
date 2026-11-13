from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sticker import Sticker


T = TypeVar("T", bound="StickerPack")


@_attrs_define
class StickerPack:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        created_by (str | Unset):
        created_at (int | Unset):
        stickers (list[Sticker] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: int | Unset = UNSET
    stickers: list[Sticker] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_by = self.created_by

        created_at = self.created_at

        stickers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stickers, Unset):
            stickers = []
            for stickers_item_data in self.stickers:
                stickers_item = stickers_item_data.to_dict()
                stickers.append(stickers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if stickers is not UNSET:
            field_dict["stickers"] = stickers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sticker import Sticker

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        _stickers = d.pop("stickers", UNSET)
        stickers: list[Sticker] | Unset = UNSET
        if _stickers is not UNSET:
            stickers = []
            for stickers_item_data in _stickers:
                stickers_item = Sticker.from_dict(stickers_item_data)

                stickers.append(stickers_item)

        sticker_pack = cls(
            id=id,
            name=name,
            created_by=created_by,
            created_at=created_at,
            stickers=stickers,
        )

        sticker_pack.additional_properties = d
        return sticker_pack

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
