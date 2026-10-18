from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminBanlistSourceResponse201")


@_attrs_define
class CreateAdminBanlistSourceResponse201:
    """
    Attributes:
        url (str | Unset):
        policy (str | Unset):
        added_at (int | Unset):
        issuer_pubkey (None | str | Unset):
    """

    url: str | Unset = UNSET
    policy: str | Unset = UNSET
    added_at: int | Unset = UNSET
    issuer_pubkey: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        policy = self.policy

        added_at = self.added_at

        issuer_pubkey: None | str | Unset
        if isinstance(self.issuer_pubkey, Unset):
            issuer_pubkey = UNSET
        else:
            issuer_pubkey = self.issuer_pubkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if policy is not UNSET:
            field_dict["policy"] = policy
        if added_at is not UNSET:
            field_dict["added_at"] = added_at
        if issuer_pubkey is not UNSET:
            field_dict["issuer_pubkey"] = issuer_pubkey

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        policy = d.pop("policy", UNSET)

        added_at = d.pop("added_at", UNSET)

        def _parse_issuer_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_pubkey = _parse_issuer_pubkey(d.pop("issuer_pubkey", UNSET))

        create_admin_banlist_source_response_201 = cls(
            url=url,
            policy=policy,
            added_at=added_at,
            issuer_pubkey=issuer_pubkey,
        )

        create_admin_banlist_source_response_201.additional_properties = d
        return create_admin_banlist_source_response_201

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
