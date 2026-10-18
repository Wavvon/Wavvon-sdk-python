from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListConversationSenderKeysResponse200Item")


@_attrs_define
class ListConversationSenderKeysResponse200Item:
    """
    Attributes:
        sender_pubkey (str | Unset):
        sender_key_version (int | Unset):
        iteration (int | Unset):
        wrapped_key_hex (str | Unset):
        wrap_nonce_hex (str | Unset):
        created_at (int | Unset):
    """

    sender_pubkey: str | Unset = UNSET
    sender_key_version: int | Unset = UNSET
    iteration: int | Unset = UNSET
    wrapped_key_hex: str | Unset = UNSET
    wrap_nonce_hex: str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_pubkey = self.sender_pubkey

        sender_key_version = self.sender_key_version

        iteration = self.iteration

        wrapped_key_hex = self.wrapped_key_hex

        wrap_nonce_hex = self.wrap_nonce_hex

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_pubkey is not UNSET:
            field_dict["sender_pubkey"] = sender_pubkey
        if sender_key_version is not UNSET:
            field_dict["sender_key_version"] = sender_key_version
        if iteration is not UNSET:
            field_dict["iteration"] = iteration
        if wrapped_key_hex is not UNSET:
            field_dict["wrapped_key_hex"] = wrapped_key_hex
        if wrap_nonce_hex is not UNSET:
            field_dict["wrap_nonce_hex"] = wrap_nonce_hex
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sender_pubkey = d.pop("sender_pubkey", UNSET)

        sender_key_version = d.pop("sender_key_version", UNSET)

        iteration = d.pop("iteration", UNSET)

        wrapped_key_hex = d.pop("wrapped_key_hex", UNSET)

        wrap_nonce_hex = d.pop("wrap_nonce_hex", UNSET)

        created_at = d.pop("created_at", UNSET)

        list_conversation_sender_keys_response_200_item = cls(
            sender_pubkey=sender_pubkey,
            sender_key_version=sender_key_version,
            iteration=iteration,
            wrapped_key_hex=wrapped_key_hex,
            wrap_nonce_hex=wrap_nonce_hex,
            created_at=created_at,
        )

        list_conversation_sender_keys_response_200_item.additional_properties = d
        return list_conversation_sender_keys_response_200_item

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
