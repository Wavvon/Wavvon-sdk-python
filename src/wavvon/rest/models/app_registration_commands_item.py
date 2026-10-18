from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppRegistrationCommandsItem")


@_attrs_define
class AppRegistrationCommandsItem:
    """
    Attributes:
        name (str):
        description (str):
        args (str | Unset):
        scope (str | Unset):
        privileged (bool | Unset):
        cooldown_seconds (int | Unset):
    """

    name: str
    description: str
    args: str | Unset = UNSET
    scope: str | Unset = UNSET
    privileged: bool | Unset = UNSET
    cooldown_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        args = self.args

        scope = self.scope

        privileged = self.privileged

        cooldown_seconds = self.cooldown_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if scope is not UNSET:
            field_dict["scope"] = scope
        if privileged is not UNSET:
            field_dict["privileged"] = privileged
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        args = d.pop("args", UNSET)

        scope = d.pop("scope", UNSET)

        privileged = d.pop("privileged", UNSET)

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        app_registration_commands_item = cls(
            name=name,
            description=description,
            args=args,
            scope=scope,
            privileged=privileged,
            cooldown_seconds=cooldown_seconds,
        )

        app_registration_commands_item.additional_properties = d
        return app_registration_commands_item

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
