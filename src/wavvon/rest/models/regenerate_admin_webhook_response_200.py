from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegenerateAdminWebhookResponse200")


@_attrs_define
class RegenerateAdminWebhookResponse200:
    """
    Attributes:
        id (str):
        webhook_url (str):
        display_name (str):
    """

    id: str
    webhook_url: str
    display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        webhook_url = self.webhook_url

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "webhook_url": webhook_url,
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        webhook_url = d.pop("webhook_url")

        display_name = d.pop("display_name")

        regenerate_admin_webhook_response_200 = cls(
            id=id,
            webhook_url=webhook_url,
            display_name=display_name,
        )

        regenerate_admin_webhook_response_200.additional_properties = d
        return regenerate_admin_webhook_response_200

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
