from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminWebhookResponse201")


@_attrs_define
class CreateAdminWebhookResponse201:
    """
    Attributes:
        id (str | Unset):
        webhook_url (str | Unset): Full URL including the secret token
        display_name (str | Unset):
    """

    id: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        webhook_url = self.webhook_url

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        display_name = d.pop("display_name", UNSET)

        create_admin_webhook_response_201 = cls(
            id=id,
            webhook_url=webhook_url,
            display_name=display_name,
        )

        create_admin_webhook_response_201.additional_properties = d
        return create_admin_webhook_response_201

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
