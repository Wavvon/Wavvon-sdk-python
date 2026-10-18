from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.dm_message_encrypted_envelope_type_0 import (
        DmMessageEncryptedEnvelopeType0,
    )
    from ..models.dm_message_group_encrypted_envelope_type_0 import (
        DmMessageGroupEncryptedEnvelopeType0,
    )


T = TypeVar("T", bound="DmMessage")


@_attrs_define
class DmMessage:
    """
    Attributes:
        id (str):
        conversation_id (str):
        sender (str):
        sender_name (None | str):
        content (None | str):
        created_at (int):
        attachments (list[Attachment]):
        delivery_failed (bool):
        is_encrypted (bool):
        encrypted_envelope (DmMessageEncryptedEnvelopeType0 | None): 1-on-1 encrypted envelope (docs/wire-format.md).
        group_encrypted_envelope (DmMessageGroupEncryptedEnvelopeType0 | None): Group sender-key envelope (docs/wire-
            format.md).
    """

    id: str
    conversation_id: str
    sender: str
    sender_name: None | str
    content: None | str
    created_at: int
    attachments: list[Attachment]
    delivery_failed: bool
    is_encrypted: bool
    encrypted_envelope: DmMessageEncryptedEnvelopeType0 | None
    group_encrypted_envelope: DmMessageGroupEncryptedEnvelopeType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dm_message_encrypted_envelope_type_0 import (
            DmMessageEncryptedEnvelopeType0,
        )
        from ..models.dm_message_group_encrypted_envelope_type_0 import (
            DmMessageGroupEncryptedEnvelopeType0,
        )

        id = self.id

        conversation_id = self.conversation_id

        sender = self.sender

        sender_name: None | str
        sender_name = self.sender_name

        content: None | str
        content = self.content

        created_at = self.created_at

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        delivery_failed = self.delivery_failed

        is_encrypted = self.is_encrypted

        encrypted_envelope: dict[str, Any] | None
        if isinstance(self.encrypted_envelope, DmMessageEncryptedEnvelopeType0):
            encrypted_envelope = self.encrypted_envelope.to_dict()
        else:
            encrypted_envelope = self.encrypted_envelope

        group_encrypted_envelope: dict[str, Any] | None
        if isinstance(
            self.group_encrypted_envelope, DmMessageGroupEncryptedEnvelopeType0
        ):
            group_encrypted_envelope = self.group_encrypted_envelope.to_dict()
        else:
            group_encrypted_envelope = self.group_encrypted_envelope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conversation_id": conversation_id,
                "sender": sender,
                "sender_name": sender_name,
                "content": content,
                "created_at": created_at,
                "attachments": attachments,
                "delivery_failed": delivery_failed,
                "is_encrypted": is_encrypted,
                "encrypted_envelope": encrypted_envelope,
                "group_encrypted_envelope": group_encrypted_envelope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.dm_message_encrypted_envelope_type_0 import (
            DmMessageEncryptedEnvelopeType0,
        )
        from ..models.dm_message_group_encrypted_envelope_type_0 import (
            DmMessageGroupEncryptedEnvelopeType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        conversation_id = d.pop("conversation_id")

        sender = d.pop("sender")

        def _parse_sender_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender_name = _parse_sender_name(d.pop("sender_name"))

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        created_at = d.pop("created_at")

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        delivery_failed = d.pop("delivery_failed")

        is_encrypted = d.pop("is_encrypted")

        def _parse_encrypted_envelope(
            data: object,
        ) -> DmMessageEncryptedEnvelopeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                encrypted_envelope_type_0 = DmMessageEncryptedEnvelopeType0.from_dict(
                    data
                )

                return encrypted_envelope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DmMessageEncryptedEnvelopeType0 | None, data)

        encrypted_envelope = _parse_encrypted_envelope(d.pop("encrypted_envelope"))

        def _parse_group_encrypted_envelope(
            data: object,
        ) -> DmMessageGroupEncryptedEnvelopeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_encrypted_envelope_type_0 = (
                    DmMessageGroupEncryptedEnvelopeType0.from_dict(data)
                )

                return group_encrypted_envelope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DmMessageGroupEncryptedEnvelopeType0 | None, data)

        group_encrypted_envelope = _parse_group_encrypted_envelope(
            d.pop("group_encrypted_envelope")
        )

        dm_message = cls(
            id=id,
            conversation_id=conversation_id,
            sender=sender,
            sender_name=sender_name,
            content=content,
            created_at=created_at,
            attachments=attachments,
            delivery_failed=delivery_failed,
            is_encrypted=is_encrypted,
            encrypted_envelope=encrypted_envelope,
            group_encrypted_envelope=group_encrypted_envelope,
        )

        dm_message.additional_properties = d
        return dm_message

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
