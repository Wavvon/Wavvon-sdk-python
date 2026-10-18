from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHubBody")


@_attrs_define
class UpdateHubBody:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        icon (str | Unset):
        require_approval (bool | Unset):
        min_security_level (int | Unset):
        max_channel_depth (int | Unset):
        welcome_label (str | Unset):
        welcome_invite_url (str | Unset):
        farewell_label (str | Unset):
        default_invite_role_id (str | Unset):
        timezone (str | Unset):
        birthdays_enabled (bool | Unset):
        afk_channel_id (str | Unset):
        afk_timeout_secs (int | Unset):
        max_attachment_bytes (int | Unset):
        max_upload_bytes (int | Unset):
        name_color_mode (str | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    require_approval: bool | Unset = UNSET
    min_security_level: int | Unset = UNSET
    max_channel_depth: int | Unset = UNSET
    welcome_label: str | Unset = UNSET
    welcome_invite_url: str | Unset = UNSET
    farewell_label: str | Unset = UNSET
    default_invite_role_id: str | Unset = UNSET
    timezone: str | Unset = UNSET
    birthdays_enabled: bool | Unset = UNSET
    afk_channel_id: str | Unset = UNSET
    afk_timeout_secs: int | Unset = UNSET
    max_attachment_bytes: int | Unset = UNSET
    max_upload_bytes: int | Unset = UNSET
    name_color_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        icon = self.icon

        require_approval = self.require_approval

        min_security_level = self.min_security_level

        max_channel_depth = self.max_channel_depth

        welcome_label = self.welcome_label

        welcome_invite_url = self.welcome_invite_url

        farewell_label = self.farewell_label

        default_invite_role_id = self.default_invite_role_id

        timezone = self.timezone

        birthdays_enabled = self.birthdays_enabled

        afk_channel_id = self.afk_channel_id

        afk_timeout_secs = self.afk_timeout_secs

        max_attachment_bytes = self.max_attachment_bytes

        max_upload_bytes = self.max_upload_bytes

        name_color_mode = self.name_color_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if require_approval is not UNSET:
            field_dict["require_approval"] = require_approval
        if min_security_level is not UNSET:
            field_dict["min_security_level"] = min_security_level
        if max_channel_depth is not UNSET:
            field_dict["max_channel_depth"] = max_channel_depth
        if welcome_label is not UNSET:
            field_dict["welcome_label"] = welcome_label
        if welcome_invite_url is not UNSET:
            field_dict["welcome_invite_url"] = welcome_invite_url
        if farewell_label is not UNSET:
            field_dict["farewell_label"] = farewell_label
        if default_invite_role_id is not UNSET:
            field_dict["default_invite_role_id"] = default_invite_role_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if birthdays_enabled is not UNSET:
            field_dict["birthdays_enabled"] = birthdays_enabled
        if afk_channel_id is not UNSET:
            field_dict["afk_channel_id"] = afk_channel_id
        if afk_timeout_secs is not UNSET:
            field_dict["afk_timeout_secs"] = afk_timeout_secs
        if max_attachment_bytes is not UNSET:
            field_dict["max_attachment_bytes"] = max_attachment_bytes
        if max_upload_bytes is not UNSET:
            field_dict["max_upload_bytes"] = max_upload_bytes
        if name_color_mode is not UNSET:
            field_dict["name_color_mode"] = name_color_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        require_approval = d.pop("require_approval", UNSET)

        min_security_level = d.pop("min_security_level", UNSET)

        max_channel_depth = d.pop("max_channel_depth", UNSET)

        welcome_label = d.pop("welcome_label", UNSET)

        welcome_invite_url = d.pop("welcome_invite_url", UNSET)

        farewell_label = d.pop("farewell_label", UNSET)

        default_invite_role_id = d.pop("default_invite_role_id", UNSET)

        timezone = d.pop("timezone", UNSET)

        birthdays_enabled = d.pop("birthdays_enabled", UNSET)

        afk_channel_id = d.pop("afk_channel_id", UNSET)

        afk_timeout_secs = d.pop("afk_timeout_secs", UNSET)

        max_attachment_bytes = d.pop("max_attachment_bytes", UNSET)

        max_upload_bytes = d.pop("max_upload_bytes", UNSET)

        name_color_mode = d.pop("name_color_mode", UNSET)

        update_hub_body = cls(
            name=name,
            description=description,
            icon=icon,
            require_approval=require_approval,
            min_security_level=min_security_level,
            max_channel_depth=max_channel_depth,
            welcome_label=welcome_label,
            welcome_invite_url=welcome_invite_url,
            farewell_label=farewell_label,
            default_invite_role_id=default_invite_role_id,
            timezone=timezone,
            birthdays_enabled=birthdays_enabled,
            afk_channel_id=afk_channel_id,
            afk_timeout_secs=afk_timeout_secs,
            max_attachment_bytes=max_attachment_bytes,
            max_upload_bytes=max_upload_bytes,
            name_color_mode=name_color_mode,
        )

        update_hub_body.additional_properties = d
        return update_hub_body

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
