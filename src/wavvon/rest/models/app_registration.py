from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_registration_commands_item import AppRegistrationCommandsItem


T = TypeVar("T", bound="AppRegistration")


@_attrs_define
class AppRegistration:
    """The caller's own app profile and slash commands (GET /me/app, PUT /me/app/profile). Optional fields are omitted when
    unset, never null.

        Attributes:
            pubkey (str):
            name (str):
            commands (list[AppRegistrationCommandsItem]):
            avatar_url (str | Unset):
            description (str | Unset):
            webhook_url (str | Unset):
            homepage_url (str | Unset):
    """

    pubkey: str
    name: str
    commands: list[AppRegistrationCommandsItem]
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    homepage_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pubkey = self.pubkey

        name = self.name

        commands = []
        for commands_item_data in self.commands:
            commands_item = commands_item_data.to_dict()
            commands.append(commands_item)

        avatar_url = self.avatar_url

        description = self.description

        webhook_url = self.webhook_url

        homepage_url = self.homepage_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pubkey": pubkey,
                "name": name,
                "commands": commands,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_registration_commands_item import AppRegistrationCommandsItem

        d = dict(src_dict)
        pubkey = d.pop("pubkey")

        name = d.pop("name")

        commands = []
        _commands = d.pop("commands")
        for commands_item_data in _commands:
            commands_item = AppRegistrationCommandsItem.from_dict(commands_item_data)

            commands.append(commands_item)

        avatar_url = d.pop("avatar_url", UNSET)

        description = d.pop("description", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        homepage_url = d.pop("homepage_url", UNSET)

        app_registration = cls(
            pubkey=pubkey,
            name=name,
            commands=commands,
            avatar_url=avatar_url,
            description=description,
            webhook_url=webhook_url,
            homepage_url=homepage_url,
        )

        app_registration.additional_properties = d
        return app_registration

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
