from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmitLobbyPowBody")


@_attrs_define
class SubmitLobbyPowBody:
    """
    Attributes:
        nonce (int):
        claimed_level (int):
    """

    nonce: int
    claimed_level: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nonce = self.nonce

        claimed_level = self.claimed_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "claimed_level": claimed_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        nonce = d.pop("nonce")

        claimed_level = d.pop("claimed_level")

        submit_lobby_pow_body = cls(
            nonce=nonce,
            claimed_level=claimed_level,
        )

        submit_lobby_pow_body.additional_properties = d
        return submit_lobby_pow_body

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
