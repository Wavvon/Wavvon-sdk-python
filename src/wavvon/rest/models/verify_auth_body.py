from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_auth_body_alliance_voice_grant import (
        VerifyAuthBodyAllianceVoiceGrant,
    )
    from ..models.verify_auth_body_subkey_cert import VerifyAuthBodySubkeyCert


T = TypeVar("T", bound="VerifyAuthBody")


@_attrs_define
class VerifyAuthBody:
    """
    Attributes:
        public_key (str):
        challenge (str):
        signature (str): Hex-encoded Ed25519 signature over the challenge bytes
        invite_code (str | Unset): Required for invite-only hubs
        security_nonce (int | Unset): PoW nonce
        security_level (int | Unset): Claimed PoW level
        subkey_cert (VerifyAuthBodySubkeyCert | Unset): Multi-device: links a device subkey to a master key
        challenge_token (str | Unset): Token from POST /challenge/verify (required when challenge_mode != off)
        is_hub (bool | Unset): Set by a hub authenticating to federate; yields a `peer` session unless the key is
            already a member
        alliance_voice_grant (VerifyAuthBodyAllianceVoiceGrant | Unset): Voice in alliance channels: an origin hub's
            signed assertion that the
            caller is its member and the named channel is shared with an alliance
            this hub belongs to. Minted by
            `POST /alliances/{alliance_id}/voice-grant` on the caller's own hub.

            Admits a **visitor** — a session scoped to `alliance_voice`, with no
            `users` row on this hub, no roles and no message access. Ignored for a
            caller who is already a member here, who gets their normal session.

            Requires the `voice.alliance` capability on this hub.
    """

    public_key: str
    challenge: str
    signature: str
    invite_code: str | Unset = UNSET
    security_nonce: int | Unset = UNSET
    security_level: int | Unset = UNSET
    subkey_cert: VerifyAuthBodySubkeyCert | Unset = UNSET
    challenge_token: str | Unset = UNSET
    is_hub: bool | Unset = UNSET
    alliance_voice_grant: VerifyAuthBodyAllianceVoiceGrant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        challenge = self.challenge

        signature = self.signature

        invite_code = self.invite_code

        security_nonce = self.security_nonce

        security_level = self.security_level

        subkey_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subkey_cert, Unset):
            subkey_cert = self.subkey_cert.to_dict()

        challenge_token = self.challenge_token

        is_hub = self.is_hub

        alliance_voice_grant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alliance_voice_grant, Unset):
            alliance_voice_grant = self.alliance_voice_grant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "challenge": challenge,
                "signature": signature,
            }
        )
        if invite_code is not UNSET:
            field_dict["invite_code"] = invite_code
        if security_nonce is not UNSET:
            field_dict["security_nonce"] = security_nonce
        if security_level is not UNSET:
            field_dict["security_level"] = security_level
        if subkey_cert is not UNSET:
            field_dict["subkey_cert"] = subkey_cert
        if challenge_token is not UNSET:
            field_dict["challenge_token"] = challenge_token
        if is_hub is not UNSET:
            field_dict["is_hub"] = is_hub
        if alliance_voice_grant is not UNSET:
            field_dict["alliance_voice_grant"] = alliance_voice_grant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.verify_auth_body_alliance_voice_grant import (
            VerifyAuthBodyAllianceVoiceGrant,
        )
        from ..models.verify_auth_body_subkey_cert import VerifyAuthBodySubkeyCert

        d = dict(src_dict)
        public_key = d.pop("public_key")

        challenge = d.pop("challenge")

        signature = d.pop("signature")

        invite_code = d.pop("invite_code", UNSET)

        security_nonce = d.pop("security_nonce", UNSET)

        security_level = d.pop("security_level", UNSET)

        _subkey_cert = d.pop("subkey_cert", UNSET)
        subkey_cert: VerifyAuthBodySubkeyCert | Unset
        if isinstance(_subkey_cert, Unset):
            subkey_cert = UNSET
        else:
            subkey_cert = VerifyAuthBodySubkeyCert.from_dict(_subkey_cert)

        challenge_token = d.pop("challenge_token", UNSET)

        is_hub = d.pop("is_hub", UNSET)

        _alliance_voice_grant = d.pop("alliance_voice_grant", UNSET)
        alliance_voice_grant: VerifyAuthBodyAllianceVoiceGrant | Unset
        if isinstance(_alliance_voice_grant, Unset):
            alliance_voice_grant = UNSET
        else:
            alliance_voice_grant = VerifyAuthBodyAllianceVoiceGrant.from_dict(
                _alliance_voice_grant
            )

        verify_auth_body = cls(
            public_key=public_key,
            challenge=challenge,
            signature=signature,
            invite_code=invite_code,
            security_nonce=security_nonce,
            security_level=security_level,
            subkey_cert=subkey_cert,
            challenge_token=challenge_token,
            is_hub=is_hub,
            alliance_voice_grant=alliance_voice_grant,
        )

        verify_auth_body.additional_properties = d
        return verify_auth_body

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
