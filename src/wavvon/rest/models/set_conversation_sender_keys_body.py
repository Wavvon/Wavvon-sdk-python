from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sender_key_recipient_blob import SenderKeyRecipientBlob
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="SetConversationSenderKeysBody")


@_attrs_define
class SetConversationSenderKeysBody:
    """
    Attributes:
        sender_key_version (int):
        recipients (list[SenderKeyRecipientBlob]):
        signature_hex (str): Ed25519 signature over canonical bytes
        signer_cert (SubkeyCert | Unset):
    """

    sender_key_version: int
    recipients: list[SenderKeyRecipientBlob]
    signature_hex: str
    signer_cert: SubkeyCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_key_version = self.sender_key_version

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        signature_hex = self.signature_hex

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender_key_version": sender_key_version,
                "recipients": recipients,
                "signature_hex": signature_hex,
            }
        )
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sender_key_recipient_blob import SenderKeyRecipientBlob
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        sender_key_version = d.pop("sender_key_version")

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = SenderKeyRecipientBlob.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        signature_hex = d.pop("signature_hex")

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: SubkeyCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = SubkeyCert.from_dict(_signer_cert)

        set_conversation_sender_keys_body = cls(
            sender_key_version=sender_key_version,
            recipients=recipients,
            signature_hex=signature_hex,
            signer_cert=signer_cert,
        )

        set_conversation_sender_keys_body.additional_properties = d
        return set_conversation_sender_keys_body

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
