from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminWebhookBody")


@_attrs_define
class CreateAdminWebhookBody:
    """
    Attributes:
        channel_id (str):
        display_name (str):
        avatar_url (str | Unset):
        rate_limit (int | Unset):  Default: 5.
    """

    channel_id: str
    display_name: str
    avatar_url: str | Unset = UNSET
    rate_limit: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        display_name = self.display_name

        avatar_url = self.avatar_url

        rate_limit = self.rate_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "display_name": display_name,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        display_name = d.pop("display_name")

        avatar_url = d.pop("avatar_url", UNSET)

        rate_limit = d.pop("rate_limit", UNSET)

        create_admin_webhook_body = cls(
            channel_id=channel_id,
            display_name=display_name,
            avatar_url=avatar_url,
            rate_limit=rate_limit,
        )

        create_admin_webhook_body.additional_properties = d
        return create_admin_webhook_body

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
