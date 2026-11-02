from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListStickerBlocklistResponse200Item")


@_attrs_define
class ListStickerBlocklistResponse200Item:
    """
    Attributes:
        sha256 (str | Unset):
        blocked_by (str | Unset):
        reason (None | str | Unset):
        created_at (int | Unset):
    """

    sha256: str | Unset = UNSET
    blocked_by: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        blocked_by = self.blocked_by

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if blocked_by is not UNSET:
            field_dict["blocked_by"] = blocked_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha256 = d.pop("sha256", UNSET)

        blocked_by = d.pop("blocked_by", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        created_at = d.pop("created_at", UNSET)

        list_sticker_blocklist_response_200_item = cls(
            sha256=sha256,
            blocked_by=blocked_by,
            reason=reason,
            created_at=created_at,
        )

        list_sticker_blocklist_response_200_item.additional_properties = d
        return list_sticker_blocklist_response_200_item

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
