from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetConversationSenderKeysBodySignerCert")


@_attrs_define
class SetConversationSenderKeysBodySignerCert:
    """Present when a paired device's subkey signed the distribution. The signature is then checked against
    signer_cert.subkey_pubkey, and the cert's master against the authenticated session. Absent means the canonical key
    signed for itself.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        set_conversation_sender_keys_body_signer_cert = cls()

        set_conversation_sender_keys_body_signer_cert.additional_properties = d
        return set_conversation_sender_keys_body_signer_cert

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
