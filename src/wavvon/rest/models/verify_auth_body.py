from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alliance_voice_grant import AllianceVoiceGrant
    from ..models.certification import Certification
    from ..models.pow_proof import PowProof
    from ..models.subkey_cert import SubkeyCert


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
        pow_proof (PowProof | Unset):
        subkey_cert (SubkeyCert | Unset):
        challenge_token (str | Unset): Token from POST /challenge/verify (required when challenge_mode != off)
        is_hub (bool | Unset): Set by a hub authenticating to federate; yields a `peer` session unless the key is
            already a member
        certifications (list[Certification] | Unset):
        alliance_voice_grant (AllianceVoiceGrant | Unset):
    """

    public_key: str
    challenge: str
    signature: str
    invite_code: str | Unset = UNSET
    security_nonce: int | Unset = UNSET
    security_level: int | Unset = UNSET
    pow_proof: PowProof | Unset = UNSET
    subkey_cert: SubkeyCert | Unset = UNSET
    challenge_token: str | Unset = UNSET
    is_hub: bool | Unset = UNSET
    certifications: list[Certification] | Unset = UNSET
    alliance_voice_grant: AllianceVoiceGrant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        challenge = self.challenge

        signature = self.signature

        invite_code = self.invite_code

        security_nonce = self.security_nonce

        security_level = self.security_level

        pow_proof: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pow_proof, Unset):
            pow_proof = self.pow_proof.to_dict()

        subkey_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subkey_cert, Unset):
            subkey_cert = self.subkey_cert.to_dict()

        challenge_token = self.challenge_token

        is_hub = self.is_hub

        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)

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
        if pow_proof is not UNSET:
            field_dict["pow_proof"] = pow_proof
        if subkey_cert is not UNSET:
            field_dict["subkey_cert"] = subkey_cert
        if challenge_token is not UNSET:
            field_dict["challenge_token"] = challenge_token
        if is_hub is not UNSET:
            field_dict["is_hub"] = is_hub
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if alliance_voice_grant is not UNSET:
            field_dict["alliance_voice_grant"] = alliance_voice_grant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alliance_voice_grant import AllianceVoiceGrant
        from ..models.certification import Certification
        from ..models.pow_proof import PowProof
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        public_key = d.pop("public_key")

        challenge = d.pop("challenge")

        signature = d.pop("signature")

        invite_code = d.pop("invite_code", UNSET)

        security_nonce = d.pop("security_nonce", UNSET)

        security_level = d.pop("security_level", UNSET)

        _pow_proof = d.pop("pow_proof", UNSET)
        pow_proof: PowProof | Unset
        if isinstance(_pow_proof, Unset):
            pow_proof = UNSET
        else:
            pow_proof = PowProof.from_dict(_pow_proof)

        _subkey_cert = d.pop("subkey_cert", UNSET)
        subkey_cert: SubkeyCert | Unset
        if isinstance(_subkey_cert, Unset):
            subkey_cert = UNSET
        else:
            subkey_cert = SubkeyCert.from_dict(_subkey_cert)

        challenge_token = d.pop("challenge_token", UNSET)

        is_hub = d.pop("is_hub", UNSET)

        _certifications = d.pop("certifications", UNSET)
        certifications: list[Certification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = Certification.from_dict(certifications_item_data)

                certifications.append(certifications_item)

        _alliance_voice_grant = d.pop("alliance_voice_grant", UNSET)
        alliance_voice_grant: AllianceVoiceGrant | Unset
        if isinstance(_alliance_voice_grant, Unset):
            alliance_voice_grant = UNSET
        else:
            alliance_voice_grant = AllianceVoiceGrant.from_dict(_alliance_voice_grant)

        verify_auth_body = cls(
            public_key=public_key,
            challenge=challenge,
            signature=signature,
            invite_code=invite_code,
            security_nonce=security_nonce,
            security_level=security_level,
            pow_proof=pow_proof,
            subkey_cert=subkey_cert,
            challenge_token=challenge_token,
            is_hub=is_hub,
            certifications=certifications,
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
