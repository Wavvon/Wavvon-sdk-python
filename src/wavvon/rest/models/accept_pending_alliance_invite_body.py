from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AcceptPendingAllianceInviteBody")


@_attrs_define
class AcceptPendingAllianceInviteBody:
    """
    Attributes:
        own_hub_url (str):
    """

    own_hub_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        own_hub_url = self.own_hub_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "own_hub_url": own_hub_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        own_hub_url = d.pop("own_hub_url")

        accept_pending_alliance_invite_body = cls(
            own_hub_url=own_hub_url,
        )

        accept_pending_alliance_invite_body.additional_properties = d
        return accept_pending_alliance_invite_body

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
