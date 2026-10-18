from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminOutgoingWebhookResponse201")


@_attrs_define
class CreateAdminOutgoingWebhookResponse201:
    """
    Attributes:
        id (str | Unset):
        url (str | Unset):
        display_name (None | str | Unset):
        secret (str | Unset): Shown once. Never persisted or returned again.
    """

    id: str | Unset = UNSET
    url: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        secret = d.pop("secret", UNSET)

        create_admin_outgoing_webhook_response_201 = cls(
            id=id,
            url=url,
            display_name=display_name,
            secret=secret,
        )

        create_admin_outgoing_webhook_response_201.additional_properties = d
        return create_admin_outgoing_webhook_response_201

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
