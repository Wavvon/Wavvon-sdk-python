from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateModerationVoiceMuteBody")


@_attrs_define
class CreateModerationVoiceMuteBody:
    """
    Attributes:
        target_public_key (str):
        reason (str | Unset):
    """

    target_public_key: str
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_public_key = self.target_public_key

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_public_key": target_public_key,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_public_key = d.pop("target_public_key")

        reason = d.pop("reason", UNSET)

        create_moderation_voice_mute_body = cls(
            target_public_key=target_public_key,
            reason=reason,
        )

        create_moderation_voice_mute_body.additional_properties = d
        return create_moderation_voice_mute_body

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
