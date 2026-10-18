from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.verify_auth_body_alliance_voice_grant_payload import (
        VerifyAuthBodyAllianceVoiceGrantPayload,
    )


T = TypeVar("T", bound="VerifyAuthBodyAllianceVoiceGrant")


@_attrs_define
class VerifyAuthBodyAllianceVoiceGrant:
    """Voice in alliance channels: an origin hub's signed assertion that the
    caller is its member and the named channel is shared with an alliance
    this hub belongs to. Minted by
    `POST /alliances/{alliance_id}/voice-grant` on the caller's own hub.

    Admits a **visitor** — a session scoped to `alliance_voice`, with no
    `users` row on this hub, no roles and no message access. Ignored for a
    caller who is already a member here, who gets their normal session.

    Requires the `voice.alliance` capability on this hub.

        Attributes:
            payload (VerifyAuthBodyAllianceVoiceGrantPayload):
            signature (str): Hex Ed25519 signature by origin_hub_pubkey over the payload JSON
    """

    payload: VerifyAuthBodyAllianceVoiceGrantPayload
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
        from ..models.verify_auth_body_alliance_voice_grant_payload import (
            VerifyAuthBodyAllianceVoiceGrantPayload,
        )

        d = dict(src_dict)
        payload = VerifyAuthBodyAllianceVoiceGrantPayload.from_dict(d.pop("payload"))

        signature = d.pop("signature")

        verify_auth_body_alliance_voice_grant = cls(
            payload=payload,
            signature=signature,
        )

        verify_auth_body_alliance_voice_grant.additional_properties = d
        return verify_auth_body_alliance_voice_grant

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
