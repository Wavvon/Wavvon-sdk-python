from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_admin_banlist_sources_response_200_item_policy import (
    ListAdminBanlistSourcesResponse200ItemPolicy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminBanlistSourcesResponse200Item")


@_attrs_define
class ListAdminBanlistSourcesResponse200Item:
    """
    Attributes:
        url (str | Unset):
        policy (ListAdminBanlistSourcesResponse200ItemPolicy | Unset):
        added_at (int | Unset):
        issuer_pubkey (None | str | Unset):
    """

    url: str | Unset = UNSET
    policy: ListAdminBanlistSourcesResponse200ItemPolicy | Unset = UNSET
    added_at: int | Unset = UNSET
    issuer_pubkey: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

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

        _policy = d.pop("policy", UNSET)
        policy: ListAdminBanlistSourcesResponse200ItemPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ListAdminBanlistSourcesResponse200ItemPolicy(_policy)

        added_at = d.pop("added_at", UNSET)

        def _parse_issuer_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_pubkey = _parse_issuer_pubkey(d.pop("issuer_pubkey", UNSET))

        list_admin_banlist_sources_response_200_item = cls(
            url=url,
            policy=policy,
            added_at=added_at,
            issuer_pubkey=issuer_pubkey,
        )

        list_admin_banlist_sources_response_200_item.additional_properties = d
        return list_admin_banlist_sources_response_200_item

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
