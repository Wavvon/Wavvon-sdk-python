from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminOutgoingWebhookBody")


@_attrs_define
class UpdateAdminOutgoingWebhookBody:
    """
    Attributes:
        url (str | Unset):
        display_name (str | Unset):
        active (bool | Unset):
    """

    url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        display_name = self.display_name

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        display_name = d.pop("display_name", UNSET)

        active = d.pop("active", UNSET)

        update_admin_outgoing_webhook_body = cls(
            url=url,
            display_name=display_name,
            active=active,
        )

        update_admin_outgoing_webhook_body.additional_properties = d
        return update_admin_outgoing_webhook_body

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
