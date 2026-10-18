from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="DmMessage")


@_attrs_define
class DmMessage:
    """
    Attributes:
        id (str | Unset):
        conversation_id (str | Unset):
        sender (str | Unset):
        sender_name (None | str | Unset):
        content (str | Unset):
        created_at (int | Unset):
        attachments (list[Attachment] | Unset):
        is_encrypted (bool | Unset):
        delivery_failed (bool | Unset):
    """

    id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    sender: str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    content: str | Unset = UNSET
    created_at: int | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    delivery_failed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        sender = self.sender

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        content = self.content

        created_at = self.created_at

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        is_encrypted = self.is_encrypted

        delivery_failed = self.delivery_failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if is_encrypted is not UNSET:
            field_dict["is_encrypted"] = is_encrypted
        if delivery_failed is not UNSET:
            field_dict["delivery_failed"] = delivery_failed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        sender = d.pop("sender", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        content = d.pop("content", UNSET)

        created_at = d.pop("created_at", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        is_encrypted = d.pop("is_encrypted", UNSET)

        delivery_failed = d.pop("delivery_failed", UNSET)

        dm_message = cls(
            id=id,
            conversation_id=conversation_id,
            sender=sender,
            sender_name=sender_name,
            content=content,
            created_at=created_at,
            attachments=attachments,
            is_encrypted=is_encrypted,
            delivery_failed=delivery_failed,
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
