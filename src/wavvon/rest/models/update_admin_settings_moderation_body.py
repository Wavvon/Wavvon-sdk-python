from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminSettingsModerationBody")


@_attrs_define
class UpdateAdminSettingsModerationBody:
    """
    Attributes:
        webhook_url (str | Unset):
        webhook_secret (str | Unset):
    """

    webhook_url: str | Unset = UNSET
    webhook_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        webhook_secret = self.webhook_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        webhook_url = d.pop("webhook_url", UNSET)

        webhook_secret = d.pop("webhook_secret", UNSET)

        update_admin_settings_moderation_body = cls(
            webhook_url=webhook_url,
            webhook_secret=webhook_secret,
        )

        update_admin_settings_moderation_body.additional_properties = d
        return update_admin_settings_moderation_body

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
