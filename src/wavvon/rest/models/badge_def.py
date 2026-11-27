from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_def_holders import BadgeDefHolders
    from ..models.badge_level import BadgeLevel


T = TypeVar("T", bound="BadgeDef")


@_attrs_define
class BadgeDef:
    """
    Attributes:
        id (str):
        name (str):
        rule (str):
        keep_while (bool):
        hidden (bool):
        levels (list[BadgeLevel]):
        holders (BadgeDefHolders): Members per level number.
        icon (None | str | Unset):
        description (None | str | Unset):
        role_id (None | str | Unset):
        program_pubkey (None | str | Unset): The program that owns it.
        declared_rule (None | str | Unset): How to earn it
    """

    id: str
    name: str
    rule: str
    keep_while: bool
    hidden: bool
    levels: list[BadgeLevel]
    holders: BadgeDefHolders
    icon: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    role_id: None | str | Unset = UNSET
    program_pubkey: None | str | Unset = UNSET
    declared_rule: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rule = self.rule

        keep_while = self.keep_while

        hidden = self.hidden

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.to_dict()
            levels.append(levels_item)

        holders = self.holders.to_dict()

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        role_id: None | str | Unset
        if isinstance(self.role_id, Unset):
            role_id = UNSET
        else:
            role_id = self.role_id

        program_pubkey: None | str | Unset
        if isinstance(self.program_pubkey, Unset):
            program_pubkey = UNSET
        else:
            program_pubkey = self.program_pubkey

        declared_rule: None | str | Unset
        if isinstance(self.declared_rule, Unset):
            declared_rule = UNSET
        else:
            declared_rule = self.declared_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "rule": rule,
                "keep_while": keep_while,
                "hidden": hidden,
                "levels": levels,
                "holders": holders,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if program_pubkey is not UNSET:
            field_dict["program_pubkey"] = program_pubkey
        if declared_rule is not UNSET:
            field_dict["declared_rule"] = declared_rule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.badge_def_holders import BadgeDefHolders
        from ..models.badge_level import BadgeLevel

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        rule = d.pop("rule")

        keep_while = d.pop("keep_while")

        hidden = d.pop("hidden")

        levels = []
        _levels = d.pop("levels")
        for levels_item_data in _levels:
            levels_item = BadgeLevel.from_dict(levels_item_data)

            levels.append(levels_item)

        holders = BadgeDefHolders.from_dict(d.pop("holders"))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_id = _parse_role_id(d.pop("role_id", UNSET))

        def _parse_program_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_pubkey = _parse_program_pubkey(d.pop("program_pubkey", UNSET))

        def _parse_declared_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declared_rule = _parse_declared_rule(d.pop("declared_rule", UNSET))

        badge_def = cls(
            id=id,
            name=name,
            rule=rule,
            keep_while=keep_while,
            hidden=hidden,
            levels=levels,
            holders=holders,
            icon=icon,
            description=description,
            role_id=role_id,
            program_pubkey=program_pubkey,
            declared_rule=declared_rule,
        )

        badge_def.additional_properties = d
        return badge_def

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
