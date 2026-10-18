from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dm_message_group_encrypted_envelope_type_0_signer_cert import (
        DmMessageGroupEncryptedEnvelopeType0SignerCert,
    )


T = TypeVar("T", bound="DmMessageGroupEncryptedEnvelopeType0")


@_attrs_define
class DmMessageGroupEncryptedEnvelopeType0:
    """Group sender-key envelope (docs/wire-format.md).

    Attributes:
        sender_pubkey (str):
        conv_id (str):
        sender_key_version (int):
        iteration (int):
        ciphertext_hex (str):
        nonce_hex (str):
        signature_hex (str):
        signer_cert (DmMessageGroupEncryptedEnvelopeType0SignerCert | Unset): Device subkey cert when a subkey signed.
            Omitted unless set.
    """

    sender_pubkey: str
    conv_id: str
    sender_key_version: int
    iteration: int
    ciphertext_hex: str
    nonce_hex: str
    signature_hex: str
    signer_cert: DmMessageGroupEncryptedEnvelopeType0SignerCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_pubkey = self.sender_pubkey

        conv_id = self.conv_id

        sender_key_version = self.sender_key_version

        iteration = self.iteration

        ciphertext_hex = self.ciphertext_hex

        nonce_hex = self.nonce_hex

        signature_hex = self.signature_hex

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender_pubkey": sender_pubkey,
                "conv_id": conv_id,
                "sender_key_version": sender_key_version,
                "iteration": iteration,
                "ciphertext_hex": ciphertext_hex,
                "nonce_hex": nonce_hex,
                "signature_hex": signature_hex,
            }
        )
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dm_message_group_encrypted_envelope_type_0_signer_cert import (
            DmMessageGroupEncryptedEnvelopeType0SignerCert,
        )

        d = dict(src_dict)
        sender_pubkey = d.pop("sender_pubkey")

        conv_id = d.pop("conv_id")

        sender_key_version = d.pop("sender_key_version")

        iteration = d.pop("iteration")

        ciphertext_hex = d.pop("ciphertext_hex")

        nonce_hex = d.pop("nonce_hex")

        signature_hex = d.pop("signature_hex")

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: DmMessageGroupEncryptedEnvelopeType0SignerCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = DmMessageGroupEncryptedEnvelopeType0SignerCert.from_dict(
                _signer_cert
            )

        dm_message_group_encrypted_envelope_type_0 = cls(
            sender_pubkey=sender_pubkey,
            conv_id=conv_id,
            sender_key_version=sender_key_version,
            iteration=iteration,
            ciphertext_hex=ciphertext_hex,
            nonce_hex=nonce_hex,
            signature_hex=signature_hex,
            signer_cert=signer_cert,
        )

        dm_message_group_encrypted_envelope_type_0.additional_properties = d
        return dm_message_group_encrypted_envelope_type_0

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
