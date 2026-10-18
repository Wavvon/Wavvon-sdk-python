from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ListAdminOutgoingWebhookSubscriptionsResponse200SubscriptionsItem"
)


@_attrs_define
class ListAdminOutgoingWebhookSubscriptionsResponse200SubscriptionsItem:
    """
    Attributes:
        event (str | Unset):
        channels (list[str] | None | Unset):
    """

    event: str | Unset = UNSET
    channels: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        channels: list[str] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = self.channels

        else:
            channels = self.channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        def _parse_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = cast(list[str], data)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))

        list_admin_outgoing_webhook_subscriptions_response_200_subscriptions_item = cls(
            event=event,
            channels=channels,
        )

        list_admin_outgoing_webhook_subscriptions_response_200_subscriptions_item.additional_properties = d
        return list_admin_outgoing_webhook_subscriptions_response_200_subscriptions_item

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
