from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetConversationSenderKeysBodyRecipientsItem")


@_attrs_define
class SetConversationSenderKeysBodyRecipientsItem:
    """
    Attributes:
        recipient_pubkey (str):
        wrapped_key_hex (str):
        wrap_nonce_hex (str):
        iteration (int):
    """

    recipient_pubkey: str
    wrapped_key_hex: str
    wrap_nonce_hex: str
    iteration: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipient_pubkey = self.recipient_pubkey

        wrapped_key_hex = self.wrapped_key_hex

        wrap_nonce_hex = self.wrap_nonce_hex

        iteration = self.iteration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipient_pubkey": recipient_pubkey,
                "wrapped_key_hex": wrapped_key_hex,
                "wrap_nonce_hex": wrap_nonce_hex,
                "iteration": iteration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        recipient_pubkey = d.pop("recipient_pubkey")

        wrapped_key_hex = d.pop("wrapped_key_hex")

        wrap_nonce_hex = d.pop("wrap_nonce_hex")

        iteration = d.pop("iteration")

        set_conversation_sender_keys_body_recipients_item = cls(
            recipient_pubkey=recipient_pubkey,
            wrapped_key_hex=wrapped_key_hex,
            wrap_nonce_hex=wrap_nonce_hex,
            iteration=iteration,
        )

        set_conversation_sender_keys_body_recipients_item.additional_properties = d
        return set_conversation_sender_keys_body_recipients_item

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
