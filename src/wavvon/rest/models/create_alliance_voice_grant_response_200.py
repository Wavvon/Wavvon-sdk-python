from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alliance_voice_grant_response_200_grant import (
        CreateAllianceVoiceGrantResponse200Grant,
    )


T = TypeVar("T", bound="CreateAllianceVoiceGrantResponse200")


@_attrs_define
class CreateAllianceVoiceGrantResponse200:
    """
    Attributes:
        grant (CreateAllianceVoiceGrantResponse200Grant | Unset): Present verbatim as auth/verify's alliance_voice_grant
        owner_hub_url (str | Unset):
        owner_hub_pubkey (str | Unset):
        channel_name (str | Unset):
    """

    grant: CreateAllianceVoiceGrantResponse200Grant | Unset = UNSET
    owner_hub_url: str | Unset = UNSET
    owner_hub_pubkey: str | Unset = UNSET
    channel_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grant, Unset):
            grant = self.grant.to_dict()

        owner_hub_url = self.owner_hub_url

        owner_hub_pubkey = self.owner_hub_pubkey

        channel_name = self.channel_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grant is not UNSET:
            field_dict["grant"] = grant
        if owner_hub_url is not UNSET:
            field_dict["owner_hub_url"] = owner_hub_url
        if owner_hub_pubkey is not UNSET:
            field_dict["owner_hub_pubkey"] = owner_hub_pubkey
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_alliance_voice_grant_response_200_grant import (
            CreateAllianceVoiceGrantResponse200Grant,
        )

        d = dict(src_dict)
        _grant = d.pop("grant", UNSET)
        grant: CreateAllianceVoiceGrantResponse200Grant | Unset
        if isinstance(_grant, Unset):
            grant = UNSET
        else:
            grant = CreateAllianceVoiceGrantResponse200Grant.from_dict(_grant)

        owner_hub_url = d.pop("owner_hub_url", UNSET)

        owner_hub_pubkey = d.pop("owner_hub_pubkey", UNSET)

        channel_name = d.pop("channel_name", UNSET)

        create_alliance_voice_grant_response_200 = cls(
            grant=grant,
            owner_hub_url=owner_hub_url,
            owner_hub_pubkey=owner_hub_pubkey,
            channel_name=channel_name,
        )

        create_alliance_voice_grant_response_200.additional_properties = d
        return create_alliance_voice_grant_response_200

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
