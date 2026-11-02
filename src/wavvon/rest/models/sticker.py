from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sticker_state import StickerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Sticker")


@_attrs_define
class Sticker:
    """A sticker this hub holds (stickers.md). `url` is relative to the hub that holds it, which is the only hub a reader
    fetches from.

        Attributes:
            id (str | Unset):
            name (str | Unset):
            url (str | Unset): `/stickers/{sha256}`
            sha256 (str | Unset): Hash of the stored WebP, computed by this hub
            width (int | Unset):
            height (int | Unset):
            origin_hub_url (None | str | Unset): The hub whose pack it came from; null for this hub's own pack stickers.
                Verified: this hub fetched the hash from there.
            origin_hub_name (None | str | Unset):
            state (StickerState | Unset): `removed`: a moderator deleted it. `evicted`: space was needed; sending it again
                re-fetches it from its origin.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    sha256: str | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    origin_hub_url: None | str | Unset = UNSET
    origin_hub_name: None | str | Unset = UNSET
    state: StickerState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        sha256 = self.sha256

        width = self.width

        height = self.height

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

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if origin_hub_url is not UNSET:
            field_dict["origin_hub_url"] = origin_hub_url
        if origin_hub_name is not UNSET:
            field_dict["origin_hub_name"] = origin_hub_name
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        sha256 = d.pop("sha256", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

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

        _state = d.pop("state", UNSET)
        state: StickerState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StickerState(_state)

        sticker = cls(
            id=id,
            name=name,
            url=url,
            sha256=sha256,
            width=width,
            height=height,
            origin_hub_url=origin_hub_url,
            origin_hub_name=origin_hub_name,
            state=state,
        )

        sticker.additional_properties = d
        return sticker

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
