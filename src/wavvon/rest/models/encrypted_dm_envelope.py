from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="EncryptedDmEnvelope")


@_attrs_define
class EncryptedDmEnvelope:
    """
    Attributes:
        sender_pubkey (str):
        conv_id (str):
        ciphertext_hex (str):
        nonce_hex (str):
        dh_pubkey_hex (str):
        signature_hex (str):
        v (int | Unset):
        message_index (int | Unset):
        prev_count (int | Unset):
        signer_cert (SubkeyCert | Unset):
    """

    sender_pubkey: str
    conv_id: str
    ciphertext_hex: str
    nonce_hex: str
    dh_pubkey_hex: str
    signature_hex: str
    v: int | Unset = UNSET
    message_index: int | Unset = UNSET
    prev_count: int | Unset = UNSET
    signer_cert: SubkeyCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_pubkey = self.sender_pubkey

        conv_id = self.conv_id

        ciphertext_hex = self.ciphertext_hex

        nonce_hex = self.nonce_hex

        dh_pubkey_hex = self.dh_pubkey_hex

        signature_hex = self.signature_hex

        v = self.v

        message_index = self.message_index

        prev_count = self.prev_count

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender_pubkey": sender_pubkey,
                "conv_id": conv_id,
                "ciphertext_hex": ciphertext_hex,
                "nonce_hex": nonce_hex,
                "dh_pubkey_hex": dh_pubkey_hex,
                "signature_hex": signature_hex,
            }
        )
        if v is not UNSET:
            field_dict["v"] = v
        if message_index is not UNSET:
            field_dict["message_index"] = message_index
        if prev_count is not UNSET:
            field_dict["prev_count"] = prev_count
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        sender_pubkey = d.pop("sender_pubkey")

        conv_id = d.pop("conv_id")

        ciphertext_hex = d.pop("ciphertext_hex")

        nonce_hex = d.pop("nonce_hex")

        dh_pubkey_hex = d.pop("dh_pubkey_hex")

        signature_hex = d.pop("signature_hex")

        v = d.pop("v", UNSET)

        message_index = d.pop("message_index", UNSET)

        prev_count = d.pop("prev_count", UNSET)

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: SubkeyCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = SubkeyCert.from_dict(_signer_cert)

        encrypted_dm_envelope = cls(
            sender_pubkey=sender_pubkey,
            conv_id=conv_id,
            ciphertext_hex=ciphertext_hex,
            nonce_hex=nonce_hex,
            dh_pubkey_hex=dh_pubkey_hex,
            signature_hex=signature_hex,
            v=v,
            message_index=message_index,
            prev_count=prev_count,
            signer_cert=signer_cert,
        )

        encrypted_dm_envelope.additional_properties = d
        return encrypted_dm_envelope

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
