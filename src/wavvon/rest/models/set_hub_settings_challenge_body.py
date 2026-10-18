from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_hub_settings_challenge_body_challenge_mode import (
    SetHubSettingsChallengeBodyChallengeMode,
)

T = TypeVar("T", bound="SetHubSettingsChallengeBody")


@_attrs_define
class SetHubSettingsChallengeBody:
    """
    Attributes:
        challenge_mode (SetHubSettingsChallengeBodyChallengeMode):
        challenge_difficulty (str):
    """

    challenge_mode: SetHubSettingsChallengeBodyChallengeMode
    challenge_difficulty: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_mode = self.challenge_mode.value

        challenge_difficulty = self.challenge_difficulty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge_mode": challenge_mode,
                "challenge_difficulty": challenge_difficulty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        challenge_mode = SetHubSettingsChallengeBodyChallengeMode(
            d.pop("challenge_mode")
        )

        challenge_difficulty = d.pop("challenge_difficulty")

        set_hub_settings_challenge_body = cls(
            challenge_mode=challenge_mode,
            challenge_difficulty=challenge_difficulty,
        )

        set_hub_settings_challenge_body.additional_properties = d
        return set_hub_settings_challenge_body

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
