from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStickerUsageResponse200Packs")


@_attrs_define
class GetStickerUsageResponse200Packs:
    """
    Attributes:
        count (int | Unset):
        bytes_ (int | Unset):
        cap_bytes (int | Unset):
    """

    count: int | Unset = UNSET
    bytes_: int | Unset = UNSET
    cap_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        bytes_ = self.bytes_

        cap_bytes = self.cap_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if cap_bytes is not UNSET:
            field_dict["cap_bytes"] = cap_bytes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        cap_bytes = d.pop("cap_bytes", UNSET)

        get_sticker_usage_response_200_packs = cls(
            count=count,
            bytes_=bytes_,
            cap_bytes=cap_bytes,
        )

        get_sticker_usage_response_200_packs.additional_properties = d
        return get_sticker_usage_response_200_packs

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
