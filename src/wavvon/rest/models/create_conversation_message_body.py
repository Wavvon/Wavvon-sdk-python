from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.create_conversation_message_body_plaintext_signer_cert import (
        CreateConversationMessageBodyPlaintextSignerCert,
    )


T = TypeVar("T", bound="CreateConversationMessageBody")


@_attrs_define
class CreateConversationMessageBody:
    """
    Attributes:
        content (str):
        attachments (list[Attachment] | Unset):
        is_encrypted (bool | Unset):
        plaintext_signature (str | Unset): Hex Ed25519 signature over the federated plaintext DM bytes (wire-format.md).
            A recipient on another hub refuses an unsigned plaintext DM.
        plaintext_signer_cert (CreateConversationMessageBodyPlaintextSignerCert | Unset): When the signing key is not
            the sender's canonical key: the master-signed cert tying the two. Only on a hub advertising
            `dms.plaintext.signercert`.
    """

    content: str
    attachments: list[Attachment] | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    plaintext_signature: str | Unset = UNSET
    plaintext_signer_cert: CreateConversationMessageBodyPlaintextSignerCert | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        is_encrypted = self.is_encrypted

        plaintext_signature = self.plaintext_signature

        plaintext_signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plaintext_signer_cert, Unset):
            plaintext_signer_cert = self.plaintext_signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if is_encrypted is not UNSET:
            field_dict["is_encrypted"] = is_encrypted
        if plaintext_signature is not UNSET:
            field_dict["plaintext_signature"] = plaintext_signature
        if plaintext_signer_cert is not UNSET:
            field_dict["plaintext_signer_cert"] = plaintext_signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.create_conversation_message_body_plaintext_signer_cert import (
            CreateConversationMessageBodyPlaintextSignerCert,
        )

        d = dict(src_dict)
        content = d.pop("content")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        is_encrypted = d.pop("is_encrypted", UNSET)

        plaintext_signature = d.pop("plaintext_signature", UNSET)

        _plaintext_signer_cert = d.pop("plaintext_signer_cert", UNSET)
        plaintext_signer_cert: CreateConversationMessageBodyPlaintextSignerCert | Unset
        if isinstance(_plaintext_signer_cert, Unset):
            plaintext_signer_cert = UNSET
        else:
            plaintext_signer_cert = (
                CreateConversationMessageBodyPlaintextSignerCert.from_dict(
                    _plaintext_signer_cert
                )
            )

        create_conversation_message_body = cls(
            content=content,
            attachments=attachments,
            is_encrypted=is_encrypted,
            plaintext_signature=plaintext_signature,
            plaintext_signer_cert=plaintext_signer_cert,
        )

        create_conversation_message_body.additional_properties = d
        return create_conversation_message_body

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
