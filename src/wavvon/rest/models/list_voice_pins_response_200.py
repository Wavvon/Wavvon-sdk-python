from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListVoicePinsResponse200")


@_attrs_define
class ListVoicePinsResponse200:
    """
    Attributes:
        public_keys (list[str]): In pin order
        can_pin (bool): The caller's own `voice.stage` in this channel
    """

    public_keys: list[str]
    can_pin: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_keys = self.public_keys

        can_pin = self.can_pin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_keys": public_keys,
                "can_pin": can_pin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_keys = cast(list[str], d.pop("public_keys"))

        can_pin = d.pop("can_pin")

        list_voice_pins_response_200 = cls(
            public_keys=public_keys,
            can_pin=can_pin,
        )

        list_voice_pins_response_200.additional_properties = d
        return list_voice_pins_response_200

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
