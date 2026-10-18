from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotChannelScope")


@_attrs_define
class BotChannelScope:
    """
    Attributes:
        bot_pubkey (str | Unset):
        channel_ids (list[str] | Unset): Empty means hub-wide access.
    """

    bot_pubkey: str | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_pubkey = self.bot_pubkey

        channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bot_pubkey is not UNSET:
            field_dict["bot_pubkey"] = bot_pubkey
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bot_pubkey = d.pop("bot_pubkey", UNSET)

        channel_ids = cast(list[str], d.pop("channel_ids", UNSET))

        bot_channel_scope = cls(
            bot_pubkey=bot_pubkey,
            channel_ids=channel_ids,
        )

        bot_channel_scope.additional_properties = d
        return bot_channel_scope

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
