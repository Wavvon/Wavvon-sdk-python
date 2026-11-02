from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sticker_usage_response_200_copies import (
        GetStickerUsageResponse200Copies,
    )
    from ..models.get_sticker_usage_response_200_packs import (
        GetStickerUsageResponse200Packs,
    )


T = TypeVar("T", bound="GetStickerUsageResponse200")


@_attrs_define
class GetStickerUsageResponse200:
    """
    Attributes:
        packs (GetStickerUsageResponse200Packs | Unset):
        packs_warning (bool | Unset): Packs are at or past `stickers_packs_warn_percent` of their cap
        copies (GetStickerUsageResponse200Copies | Unset):
        evictions (int | Unset): Copies whose bytes were dropped for space and have not come back
    """

    packs: GetStickerUsageResponse200Packs | Unset = UNSET
    packs_warning: bool | Unset = UNSET
    copies: GetStickerUsageResponse200Copies | Unset = UNSET
    evictions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.packs, Unset):
            packs = self.packs.to_dict()

        packs_warning = self.packs_warning

        copies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copies, Unset):
            copies = self.copies.to_dict()

        evictions = self.evictions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packs is not UNSET:
            field_dict["packs"] = packs
        if packs_warning is not UNSET:
            field_dict["packs_warning"] = packs_warning
        if copies is not UNSET:
            field_dict["copies"] = copies
        if evictions is not UNSET:
            field_dict["evictions"] = evictions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_sticker_usage_response_200_copies import (
            GetStickerUsageResponse200Copies,
        )
        from ..models.get_sticker_usage_response_200_packs import (
            GetStickerUsageResponse200Packs,
        )

        d = dict(src_dict)
        _packs = d.pop("packs", UNSET)
        packs: GetStickerUsageResponse200Packs | Unset
        if isinstance(_packs, Unset):
            packs = UNSET
        else:
            packs = GetStickerUsageResponse200Packs.from_dict(_packs)

        packs_warning = d.pop("packs_warning", UNSET)

        _copies = d.pop("copies", UNSET)
        copies: GetStickerUsageResponse200Copies | Unset
        if isinstance(_copies, Unset):
            copies = UNSET
        else:
            copies = GetStickerUsageResponse200Copies.from_dict(_copies)

        evictions = d.pop("evictions", UNSET)

        get_sticker_usage_response_200 = cls(
            packs=packs,
            packs_warning=packs_warning,
            copies=copies,
            evictions=evictions,
        )

        get_sticker_usage_response_200.additional_properties = d
        return get_sticker_usage_response_200

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
