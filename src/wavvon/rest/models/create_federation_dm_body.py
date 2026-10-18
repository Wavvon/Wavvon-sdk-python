from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.encrypted_dm_envelope import EncryptedDmEnvelope
    from ..models.group_encrypted_envelope import GroupEncryptedEnvelope
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="CreateFederationDmBody")


@_attrs_define
class CreateFederationDmBody:
    """
    Attributes:
        message_id (str):
        conversation_id (str):
        conv_type (str):
        sender (str):
        members (list[str]):
        created_at (int):
        content (str | Unset):
        attachments (list[Attachment] | Unset):
        signature (str | Unset):
        encrypted_envelope (EncryptedDmEnvelope | Unset):
        group_encrypted_envelope (GroupEncryptedEnvelope | Unset):
        sender_hub_url (str | Unset):
        signer_cert (SubkeyCert | Unset):
        mirror (bool | Unset):
    """

    message_id: str
    conversation_id: str
    conv_type: str
    sender: str
    members: list[str]
    created_at: int
    content: str | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    signature: str | Unset = UNSET
    encrypted_envelope: EncryptedDmEnvelope | Unset = UNSET
    group_encrypted_envelope: GroupEncryptedEnvelope | Unset = UNSET
    sender_hub_url: str | Unset = UNSET
    signer_cert: SubkeyCert | Unset = UNSET
    mirror: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        conversation_id = self.conversation_id

        conv_type = self.conv_type

        sender = self.sender

        members = self.members

        created_at = self.created_at

        content = self.content

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        signature = self.signature

        encrypted_envelope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encrypted_envelope, Unset):
            encrypted_envelope = self.encrypted_envelope.to_dict()

        group_encrypted_envelope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_encrypted_envelope, Unset):
            group_encrypted_envelope = self.group_encrypted_envelope.to_dict()

        sender_hub_url = self.sender_hub_url

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        mirror = self.mirror

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_id": message_id,
                "conversation_id": conversation_id,
                "conv_type": conv_type,
                "sender": sender,
                "members": members,
                "created_at": created_at,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if signature is not UNSET:
            field_dict["signature"] = signature
        if encrypted_envelope is not UNSET:
            field_dict["encrypted_envelope"] = encrypted_envelope
        if group_encrypted_envelope is not UNSET:
            field_dict["group_encrypted_envelope"] = group_encrypted_envelope
        if sender_hub_url is not UNSET:
            field_dict["sender_hub_url"] = sender_hub_url
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert
        if mirror is not UNSET:
            field_dict["mirror"] = mirror

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.encrypted_dm_envelope import EncryptedDmEnvelope
        from ..models.group_encrypted_envelope import GroupEncryptedEnvelope
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        message_id = d.pop("message_id")

        conversation_id = d.pop("conversation_id")

        conv_type = d.pop("conv_type")

        sender = d.pop("sender")

        members = cast(list[str], d.pop("members"))

        created_at = d.pop("created_at")

        content = d.pop("content", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        signature = d.pop("signature", UNSET)

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

        sender_hub_url = d.pop("sender_hub_url", UNSET)

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: SubkeyCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = SubkeyCert.from_dict(_signer_cert)

        mirror = d.pop("mirror", UNSET)

        create_federation_dm_body = cls(
            message_id=message_id,
            conversation_id=conversation_id,
            conv_type=conv_type,
            sender=sender,
            members=members,
            created_at=created_at,
            content=content,
            attachments=attachments,
            signature=signature,
            encrypted_envelope=encrypted_envelope,
            group_encrypted_envelope=group_encrypted_envelope,
            sender_hub_url=sender_hub_url,
            signer_cert=signer_cert,
            mirror=mirror,
        )

        create_federation_dm_body.additional_properties = d
        return create_federation_dm_body

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
