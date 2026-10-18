from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminOutgoingWebhooksResponse200Item")


@_attrs_define
class ListAdminOutgoingWebhooksResponse200Item:
    """
    Attributes:
        id (str | Unset):
        url (str | Unset):
        display_name (None | str | Unset):
        active (bool | Unset):
        failure_count (int | Unset):
        last_delivery_at (int | None | Unset):
        last_failure_at (int | None | Unset):
        created_at (int | Unset):
        created_by_pubkey (str | Unset):
        subscription_count (int | Unset):
    """

    id: str | Unset = UNSET
    url: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    failure_count: int | Unset = UNSET
    last_delivery_at: int | None | Unset = UNSET
    last_failure_at: int | None | Unset = UNSET
    created_at: int | Unset = UNSET
    created_by_pubkey: str | Unset = UNSET
    subscription_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        active = self.active

        failure_count = self.failure_count

        last_delivery_at: int | None | Unset
        if isinstance(self.last_delivery_at, Unset):
            last_delivery_at = UNSET
        else:
            last_delivery_at = self.last_delivery_at

        last_failure_at: int | None | Unset
        if isinstance(self.last_failure_at, Unset):
            last_failure_at = UNSET
        else:
            last_failure_at = self.last_failure_at

        created_at = self.created_at

        created_by_pubkey = self.created_by_pubkey

        subscription_count = self.subscription_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if active is not UNSET:
            field_dict["active"] = active
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if last_delivery_at is not UNSET:
            field_dict["last_delivery_at"] = last_delivery_at
        if last_failure_at is not UNSET:
            field_dict["last_failure_at"] = last_failure_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_pubkey is not UNSET:
            field_dict["created_by_pubkey"] = created_by_pubkey
        if subscription_count is not UNSET:
            field_dict["subscription_count"] = subscription_count

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

        active = d.pop("active", UNSET)

        failure_count = d.pop("failure_count", UNSET)

        def _parse_last_delivery_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("last_delivery_at", UNSET))

        def _parse_last_failure_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_failure_at = _parse_last_failure_at(d.pop("last_failure_at", UNSET))

        created_at = d.pop("created_at", UNSET)

        created_by_pubkey = d.pop("created_by_pubkey", UNSET)

        subscription_count = d.pop("subscription_count", UNSET)

        list_admin_outgoing_webhooks_response_200_item = cls(
            id=id,
            url=url,
            display_name=display_name,
            active=active,
            failure_count=failure_count,
            last_delivery_at=last_delivery_at,
            last_failure_at=last_failure_at,
            created_at=created_at,
            created_by_pubkey=created_by_pubkey,
            subscription_count=subscription_count,
        )

        list_admin_outgoing_webhooks_response_200_item.additional_properties = d
        return list_admin_outgoing_webhooks_response_200_item

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
