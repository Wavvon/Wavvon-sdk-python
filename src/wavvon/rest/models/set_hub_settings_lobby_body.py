from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetHubSettingsLobbyBody")


@_attrs_define
class SetHubSettingsLobbyBody:
    """
    Attributes:
        lobby_enabled (bool):
        welcome_md (None | str | Unset):
    """

    lobby_enabled: bool
    welcome_md: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lobby_enabled = self.lobby_enabled

        welcome_md: None | str | Unset
        if isinstance(self.welcome_md, Unset):
            welcome_md = UNSET
        else:
            welcome_md = self.welcome_md

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lobby_enabled": lobby_enabled,
            }
        )
        if welcome_md is not UNSET:
            field_dict["welcome_md"] = welcome_md

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lobby_enabled = d.pop("lobby_enabled")

        def _parse_welcome_md(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        welcome_md = _parse_welcome_md(d.pop("welcome_md", UNSET))

        set_hub_settings_lobby_body = cls(
            lobby_enabled=lobby_enabled,
            welcome_md=welcome_md,
        )

        set_hub_settings_lobby_body.additional_properties = d
        return set_hub_settings_lobby_body

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
