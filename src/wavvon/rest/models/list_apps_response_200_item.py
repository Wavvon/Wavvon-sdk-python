from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_apps_response_200_item_commands_item import (
        ListAppsResponse200ItemCommandsItem,
    )
    from ..models.list_apps_response_200_item_game import ListAppsResponse200ItemGame


T = TypeVar("T", bound="ListAppsResponse200Item")


@_attrs_define
class ListAppsResponse200Item:
    """
    Attributes:
        pubkey (str | Unset):
        name (str | Unset):
        avatar_url (str | Unset):
        description (str | Unset):
        game (ListAppsResponse200ItemGame | Unset):
        commands (list[ListAppsResponse200ItemCommandsItem] | Unset):
    """

    pubkey: str | Unset = UNSET
    name: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    game: ListAppsResponse200ItemGame | Unset = UNSET
    commands: list[ListAppsResponse200ItemCommandsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pubkey = self.pubkey

        name = self.name

        avatar_url = self.avatar_url

        description = self.description

        game: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game, Unset):
            game = self.game.to_dict()

        commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = []
            for commands_item_data in self.commands:
                commands_item = commands_item_data.to_dict()
                commands.append(commands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if name is not UNSET:
            field_dict["name"] = name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if game is not UNSET:
            field_dict["game"] = game
        if commands is not UNSET:
            field_dict["commands"] = commands

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_apps_response_200_item_commands_item import (
            ListAppsResponse200ItemCommandsItem,
        )
        from ..models.list_apps_response_200_item_game import (
            ListAppsResponse200ItemGame,
        )

        d = dict(src_dict)
        pubkey = d.pop("pubkey", UNSET)

        name = d.pop("name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        description = d.pop("description", UNSET)

        _game = d.pop("game", UNSET)
        game: ListAppsResponse200ItemGame | Unset
        if isinstance(_game, Unset):
            game = UNSET
        else:
            game = ListAppsResponse200ItemGame.from_dict(_game)

        _commands = d.pop("commands", UNSET)
        commands: list[ListAppsResponse200ItemCommandsItem] | Unset = UNSET
        if _commands is not UNSET:
            commands = []
            for commands_item_data in _commands:
                commands_item = ListAppsResponse200ItemCommandsItem.from_dict(
                    commands_item_data
                )

                commands.append(commands_item)

        list_apps_response_200_item = cls(
            pubkey=pubkey,
            name=name,
            avatar_url=avatar_url,
            description=description,
            game=game,
            commands=commands,
        )

        list_apps_response_200_item.additional_properties = d
        return list_apps_response_200_item

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
