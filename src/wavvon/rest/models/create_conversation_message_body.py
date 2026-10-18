from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.encrypted_dm_envelope import EncryptedDmEnvelope
    from ..models.group_encrypted_envelope import GroupEncryptedEnvelope
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="CreateConversationMessageBody")


@_attrs_define
class CreateConversationMessageBody:
    """
    Attributes:
        content (str | Unset):
        attachments (list[Attachment] | Unset):
        encrypted_envelope (EncryptedDmEnvelope | Unset):
        group_encrypted_envelope (GroupEncryptedEnvelope | Unset):
        plaintext_signature (str | Unset): Hex Ed25519 signature over the federated plaintext DM bytes (wire-format.md).
            A recipient on another hub refuses an unsigned plaintext DM.
        plaintext_signer_cert (SubkeyCert | Unset):
    """

    content: str | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    encrypted_envelope: EncryptedDmEnvelope | Unset = UNSET
    group_encrypted_envelope: GroupEncryptedEnvelope | Unset = UNSET
    plaintext_signature: str | Unset = UNSET
    plaintext_signer_cert: SubkeyCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        encrypted_envelope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encrypted_envelope, Unset):
            encrypted_envelope = self.encrypted_envelope.to_dict()

        group_encrypted_envelope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_encrypted_envelope, Unset):
            group_encrypted_envelope = self.group_encrypted_envelope.to_dict()

        plaintext_signature = self.plaintext_signature

        plaintext_signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plaintext_signer_cert, Unset):
            plaintext_signer_cert = self.plaintext_signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if encrypted_envelope is not UNSET:
            field_dict["encrypted_envelope"] = encrypted_envelope
        if group_encrypted_envelope is not UNSET:
            field_dict["group_encrypted_envelope"] = group_encrypted_envelope
        if plaintext_signature is not UNSET:
            field_dict["plaintext_signature"] = plaintext_signature
        if plaintext_signer_cert is not UNSET:
            field_dict["plaintext_signer_cert"] = plaintext_signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.encrypted_dm_envelope import EncryptedDmEnvelope
        from ..models.group_encrypted_envelope import GroupEncryptedEnvelope
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        content = d.pop("content", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _encrypted_envelope = d.pop("encrypted_envelope", UNSET)
        encrypted_envelope: EncryptedDmEnvelope | Unset
        if isinstance(_encrypted_envelope, Unset):
            encrypted_envelope = UNSET
        else:
            encrypted_envelope = EncryptedDmEnvelope.from_dict(_encrypted_envelope)

        _group_encrypted_envelope = d.pop("group_encrypted_envelope", UNSET)
        group_encrypted_envelope: GroupEncryptedEnvelope | Unset
        if isinstance(_group_encrypted_envelope, Unset):
            group_encrypted_envelope = UNSET
        else:
            group_encrypted_envelope = GroupEncryptedEnvelope.from_dict(
                _group_encrypted_envelope
            )

        plaintext_signature = d.pop("plaintext_signature", UNSET)

        _plaintext_signer_cert = d.pop("plaintext_signer_cert", UNSET)
        plaintext_signer_cert: SubkeyCert | Unset
        if isinstance(_plaintext_signer_cert, Unset):
            plaintext_signer_cert = UNSET
        else:
            plaintext_signer_cert = SubkeyCert.from_dict(_plaintext_signer_cert)

        create_conversation_message_body = cls(
            content=content,
            attachments=attachments,
            encrypted_envelope=encrypted_envelope,
            group_encrypted_envelope=group_encrypted_envelope,
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
