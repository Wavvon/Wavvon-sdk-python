from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LockdownSettings")


@_attrs_define
class LockdownSettings:
    """
    Attributes:
        enabled (bool):
        freeze_minutes (int):
        raid_join_threshold (int): Joins per minute that raise a raid alert; 0 is off
        auto_lockdown (bool):
    """

    enabled: bool
    freeze_minutes: int
    raid_join_threshold: int
    auto_lockdown: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        freeze_minutes = self.freeze_minutes

        raid_join_threshold = self.raid_join_threshold

        auto_lockdown = self.auto_lockdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "freeze_minutes": freeze_minutes,
                "raid_join_threshold": raid_join_threshold,
                "auto_lockdown": auto_lockdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        freeze_minutes = d.pop("freeze_minutes")

        raid_join_threshold = d.pop("raid_join_threshold")

        auto_lockdown = d.pop("auto_lockdown")

        lockdown_settings = cls(
            enabled=enabled,
            freeze_minutes=freeze_minutes,
            raid_join_threshold=raid_join_threshold,
            auto_lockdown=auto_lockdown,
        )

        lockdown_settings.additional_properties = d
        return lockdown_settings

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
