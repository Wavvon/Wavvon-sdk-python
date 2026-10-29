from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_admin_settings_challenge_body_challenge_mode import (
    PatchAdminSettingsChallengeBodyChallengeMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAdminSettingsChallengeBody")


@_attrs_define
class PatchAdminSettingsChallengeBody:
    """Absent fields keep their stored value.

    Attributes:
        challenge_mode (PatchAdminSettingsChallengeBodyChallengeMode | Unset):
        challenge_difficulty (str | Unset):
    """

    challenge_mode: PatchAdminSettingsChallengeBodyChallengeMode | Unset = UNSET
    challenge_difficulty: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_mode: str | Unset = UNSET
        if not isinstance(self.challenge_mode, Unset):
            challenge_mode = self.challenge_mode.value

        challenge_difficulty = self.challenge_difficulty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_mode is not UNSET:
            field_dict["challenge_mode"] = challenge_mode
        if challenge_difficulty is not UNSET:
            field_dict["challenge_difficulty"] = challenge_difficulty

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _challenge_mode = d.pop("challenge_mode", UNSET)
        challenge_mode: PatchAdminSettingsChallengeBodyChallengeMode | Unset
        if isinstance(_challenge_mode, Unset):
            challenge_mode = UNSET
        else:
            challenge_mode = PatchAdminSettingsChallengeBodyChallengeMode(
                _challenge_mode
            )

        challenge_difficulty = d.pop("challenge_difficulty", UNSET)

        patch_admin_settings_challenge_body = cls(
            challenge_mode=challenge_mode,
            challenge_difficulty=challenge_difficulty,
        )

        patch_admin_settings_challenge_body.additional_properties = d
        return patch_admin_settings_challenge_body

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
