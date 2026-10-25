from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListAdminWebhooksResponse200Item")


@_attrs_define
class ListAdminWebhooksResponse200Item:
    """
    Attributes:
        id (str):
        display_name (str):
        channel_id (str):
        channel_name (None | str):
        webhook_url (str): Base URL only; the token is stored hashed and cannot be recovered. Regenerate to get a
            working URL.
        created_by (str):
        created_at (int):
    """

    id: str
    display_name: str
    channel_id: str
    channel_name: None | str
    webhook_url: str
    created_by: str
    created_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        channel_id = self.channel_id

        channel_name: None | str
        channel_name = self.channel_name

        webhook_url = self.webhook_url

        created_by = self.created_by

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "channel_id": channel_id,
                "channel_name": channel_name,
                "webhook_url": webhook_url,
                "created_by": created_by,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        channel_id = d.pop("channel_id")

        def _parse_channel_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        channel_name = _parse_channel_name(d.pop("channel_name"))

        webhook_url = d.pop("webhook_url")

        created_by = d.pop("created_by")

        created_at = d.pop("created_at")

        list_admin_webhooks_response_200_item = cls(
            id=id,
            display_name=display_name,
            channel_id=channel_id,
            channel_name=channel_name,
            webhook_url=webhook_url,
            created_by=created_by,
            created_at=created_at,
        )

        list_admin_webhooks_response_200_item.additional_properties = d
        return list_admin_webhooks_response_200_item

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
