from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verify_auth_response_200_scope import VerifyAuthResponse200Scope

T = TypeVar("T", bound="VerifyAuthResponse200")


@_attrs_define
class VerifyAuthResponse200:
    """
    Attributes:
        token (str): Session token, 32 random bytes hex. Send as `Authorization: Bearer <token>` and as `/ws?token=`.
        scope (VerifyAuthResponse200Scope): 'lobby' means the user must complete PoW in /lobby before full access.
            'alliance_voice' is a visitor from an allied hub, admitted to one shared
            voice channel and confined to /info, the DH-key routes and /ws.
            'peer' is a federating hub (sent `is_hub: true` and is not a member),
            confined to the federation routes and refused at /ws.
        canonical_pubkey (str): The identity this session acts as. Equals `public_key` for a
            single-key sign-in; for a device authenticating with a
            `subkey_cert` it is the master (or the pre-existing legacy key)
            the hub attributes that device's actions to. Use it to recognise
            yourself in rosters and message authors.
    """

    token: str
    scope: VerifyAuthResponse200Scope
    canonical_pubkey: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        scope = self.scope.value

        canonical_pubkey = self.canonical_pubkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "scope": scope,
                "canonical_pubkey": canonical_pubkey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        scope = VerifyAuthResponse200Scope(d.pop("scope"))

        canonical_pubkey = d.pop("canonical_pubkey")

        verify_auth_response_200 = cls(
            token=token,
            scope=scope,
            canonical_pubkey=canonical_pubkey,
        )

        verify_auth_response_200.additional_properties = d
        return verify_auth_response_200

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
