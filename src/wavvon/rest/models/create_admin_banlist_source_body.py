from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_admin_banlist_source_body_policy import (
    CreateAdminBanlistSourceBodyPolicy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminBanlistSourceBody")


@_attrs_define
class CreateAdminBanlistSourceBody:
    """
    Attributes:
        url (str):
        policy (CreateAdminBanlistSourceBodyPolicy | Unset):  Default: CreateAdminBanlistSourceBodyPolicy.HARD_REJECT.
    """

    url: str
    policy: CreateAdminBanlistSourceBodyPolicy | Unset = (
        CreateAdminBanlistSourceBodyPolicy.HARD_REJECT
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        _policy = d.pop("policy", UNSET)
        policy: CreateAdminBanlistSourceBodyPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = CreateAdminBanlistSourceBodyPolicy(_policy)

        create_admin_banlist_source_body = cls(
            url=url,
            policy=policy,
        )

        create_admin_banlist_source_body.additional_properties = d
        return create_admin_banlist_source_body

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
