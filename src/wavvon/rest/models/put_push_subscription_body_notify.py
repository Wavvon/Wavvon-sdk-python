from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_push_subscription_body_notify_hub import (
    PutPushSubscriptionBodyNotifyHub,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_push_subscription_body_notify_channels import (
        PutPushSubscriptionBodyNotifyChannels,
    )
    from ..models.put_push_subscription_body_notify_channels_until import (
        PutPushSubscriptionBodyNotifyChannelsUntil,
    )


T = TypeVar("T", bound="PutPushSubscriptionBodyNotify")


@_attrs_define
class PutPushSubscriptionBodyNotify:
    """The client's notify modes for this hub; mentions, replies and DMs push under all and mentions, never under silent
    (channel over hub).

        Attributes:
            hub (PutPushSubscriptionBodyNotifyHub | Unset):
            channels (PutPushSubscriptionBodyNotifyChannels | Unset):
            hub_until (int | Unset): Epoch-ms end of a timed hub mute; past it the hub mode counts as unset (capability
                push.web.muteuntil).
            channels_until (PutPushSubscriptionBodyNotifyChannelsUntil | Unset): Epoch-ms end of a timed mute per channel;
                past it the channel falls back to the hub mode.
    """

    hub: PutPushSubscriptionBodyNotifyHub | Unset = UNSET
    channels: PutPushSubscriptionBodyNotifyChannels | Unset = UNSET
    hub_until: int | Unset = UNSET
    channels_until: PutPushSubscriptionBodyNotifyChannelsUntil | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub: str | Unset = UNSET
        if not isinstance(self.hub, Unset):
            hub = self.hub.value

        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        hub_until = self.hub_until

        channels_until: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels_until, Unset):
            channels_until = self.channels_until.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hub is not UNSET:
            field_dict["hub"] = hub
        if channels is not UNSET:
            field_dict["channels"] = channels
        if hub_until is not UNSET:
            field_dict["hub_until"] = hub_until
        if channels_until is not UNSET:
            field_dict["channels_until"] = channels_until

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.put_push_subscription_body_notify_channels import (
            PutPushSubscriptionBodyNotifyChannels,
        )
        from ..models.put_push_subscription_body_notify_channels_until import (
            PutPushSubscriptionBodyNotifyChannelsUntil,
        )

        d = dict(src_dict)
        _hub = d.pop("hub", UNSET)
        hub: PutPushSubscriptionBodyNotifyHub | Unset
        if isinstance(_hub, Unset):
            hub = UNSET
        else:
            hub = PutPushSubscriptionBodyNotifyHub(_hub)

        _channels = d.pop("channels", UNSET)
        channels: PutPushSubscriptionBodyNotifyChannels | Unset
        if isinstance(_channels, Unset):
            channels = UNSET
        else:
            channels = PutPushSubscriptionBodyNotifyChannels.from_dict(_channels)

        hub_until = d.pop("hub_until", UNSET)

        _channels_until = d.pop("channels_until", UNSET)
        channels_until: PutPushSubscriptionBodyNotifyChannelsUntil | Unset
        if isinstance(_channels_until, Unset):
            channels_until = UNSET
        else:
            channels_until = PutPushSubscriptionBodyNotifyChannelsUntil.from_dict(
                _channels_until
            )

        put_push_subscription_body_notify = cls(
            hub=hub,
            channels=channels,
            hub_until=hub_until,
            channels_until=channels_until,
        )

        put_push_subscription_body_notify.additional_properties = d
        return put_push_subscription_body_notify

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
