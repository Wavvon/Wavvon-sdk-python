from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyAuthBodyAllianceVoiceGrantPayload")


@_attrs_define
class VerifyAuthBodyAllianceVoiceGrantPayload:
    """
    Attributes:
        alliance_id (str):
        owner_hub_pubkey (str): Must be this hub, so a grant cannot be replayed elsewhere
        channel_id (str):
        subject_pubkey (str): The visitor's canonical pubkey. Must equal the identity this
            challenge-response just authenticated — the grant vouches for
            membership of the origin hub, never for identity.
        origin_hub_pubkey (str):
        origin_hub_url (str):
        issued_at (int):
        expires_at (int):
        display_name (None | str | Unset): Roster display only. Hub-vouched, not proven.
    """

    alliance_id: str
    owner_hub_pubkey: str
    channel_id: str
    subject_pubkey: str
    origin_hub_pubkey: str
    origin_hub_url: str
    issued_at: int
    expires_at: int
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alliance_id = self.alliance_id

        owner_hub_pubkey = self.owner_hub_pubkey

        channel_id = self.channel_id

        subject_pubkey = self.subject_pubkey

        origin_hub_pubkey = self.origin_hub_pubkey

        origin_hub_url = self.origin_hub_url

        issued_at = self.issued_at

        expires_at = self.expires_at

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alliance_id": alliance_id,
                "owner_hub_pubkey": owner_hub_pubkey,
                "channel_id": channel_id,
                "subject_pubkey": subject_pubkey,
                "origin_hub_pubkey": origin_hub_pubkey,
                "origin_hub_url": origin_hub_url,
                "issued_at": issued_at,
                "expires_at": expires_at,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alliance_id = d.pop("alliance_id")

        owner_hub_pubkey = d.pop("owner_hub_pubkey")

        channel_id = d.pop("channel_id")

        subject_pubkey = d.pop("subject_pubkey")

        origin_hub_pubkey = d.pop("origin_hub_pubkey")

        origin_hub_url = d.pop("origin_hub_url")

        issued_at = d.pop("issued_at")

        expires_at = d.pop("expires_at")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        verify_auth_body_alliance_voice_grant_payload = cls(
            alliance_id=alliance_id,
            owner_hub_pubkey=owner_hub_pubkey,
            channel_id=channel_id,
            subject_pubkey=subject_pubkey,
            origin_hub_pubkey=origin_hub_pubkey,
            origin_hub_url=origin_hub_url,
            issued_at=issued_at,
            expires_at=expires_at,
            display_name=display_name,
        )

        verify_auth_body_alliance_voice_grant_payload.additional_properties = d
        return verify_auth_body_alliance_voice_grant_payload

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
