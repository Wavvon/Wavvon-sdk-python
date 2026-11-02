from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_sticker_state import AdminStickerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminSticker")


@_attrs_define
class AdminSticker:
    """
    Attributes:
        id (str | Unset):
        sha256 (str | Unset):
        name (str | Unset):
        size_bytes (int | Unset):
        width (int | Unset):
        height (int | Unset):
        pack_id (None | str | Unset): Null for a copy
        uploader (str | Unset):
        origin_hub_url (None | str | Unset):
        origin_hub_name (None | str | Unset):
        created_at (int | Unset):
        last_used_at (int | Unset):
        state (AdminStickerState | Unset):
        message_count (int | Unset):
    """

    id: str | Unset = UNSET
    sha256: str | Unset = UNSET
    name: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    pack_id: None | str | Unset = UNSET
    uploader: str | Unset = UNSET
    origin_hub_url: None | str | Unset = UNSET
    origin_hub_name: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    last_used_at: int | Unset = UNSET
    state: AdminStickerState | Unset = UNSET
    message_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sha256 = self.sha256

        name = self.name

        size_bytes = self.size_bytes

        width = self.width

        height = self.height

        pack_id: None | str | Unset
        if isinstance(self.pack_id, Unset):
            pack_id = UNSET
        else:
            pack_id = self.pack_id

        uploader = self.uploader

        origin_hub_url: None | str | Unset
        if isinstance(self.origin_hub_url, Unset):
            origin_hub_url = UNSET
        else:
            origin_hub_url = self.origin_hub_url

        origin_hub_name: None | str | Unset
        if isinstance(self.origin_hub_name, Unset):
            origin_hub_name = UNSET
        else:
            origin_hub_name = self.origin_hub_name

        created_at = self.created_at

        last_used_at = self.last_used_at

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        message_count = self.message_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if name is not UNSET:
            field_dict["name"] = name
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if pack_id is not UNSET:
            field_dict["pack_id"] = pack_id
        if uploader is not UNSET:
            field_dict["uploader"] = uploader
        if origin_hub_url is not UNSET:
            field_dict["origin_hub_url"] = origin_hub_url
        if origin_hub_name is not UNSET:
            field_dict["origin_hub_name"] = origin_hub_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if state is not UNSET:
            field_dict["state"] = state
        if message_count is not UNSET:
            field_dict["message_count"] = message_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sha256 = d.pop("sha256", UNSET)

        name = d.pop("name", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        def _parse_pack_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pack_id = _parse_pack_id(d.pop("pack_id", UNSET))

        uploader = d.pop("uploader", UNSET)

        def _parse_origin_hub_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_hub_url = _parse_origin_hub_url(d.pop("origin_hub_url", UNSET))

        def _parse_origin_hub_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_hub_name = _parse_origin_hub_name(d.pop("origin_hub_name", UNSET))

        created_at = d.pop("created_at", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        _state = d.pop("state", UNSET)
        state: AdminStickerState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AdminStickerState(_state)

        message_count = d.pop("message_count", UNSET)

        admin_sticker = cls(
            id=id,
            sha256=sha256,
            name=name,
            size_bytes=size_bytes,
            width=width,
            height=height,
            pack_id=pack_id,
            uploader=uploader,
            origin_hub_url=origin_hub_url,
            origin_hub_name=origin_hub_name,
            created_at=created_at,
            last_used_at=last_used_at,
            state=state,
            message_count=message_count,
        )

        admin_sticker.additional_properties = d
        return admin_sticker

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
