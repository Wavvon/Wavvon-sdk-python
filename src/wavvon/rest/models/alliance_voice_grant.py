from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alliance_voice_grant_payload import AllianceVoiceGrantPayload


T = TypeVar("T", bound="AllianceVoiceGrant")


@_attrs_define
class AllianceVoiceGrant:
    """
    Attributes:
        payload (AllianceVoiceGrantPayload):
        signature (str): Hex Ed25519 signature by origin_hub_pubkey over the payload JSON
    """

    payload: AllianceVoiceGrantPayload
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload.to_dict()

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alliance_voice_grant_payload import AllianceVoiceGrantPayload

        d = dict(src_dict)
        payload = AllianceVoiceGrantPayload.from_dict(d.pop("payload"))

        signature = d.pop("signature")

        alliance_voice_grant = cls(
            payload=payload,
            signature=signature,
        )

        alliance_voice_grant.additional_properties = d
        return alliance_voice_grant

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
