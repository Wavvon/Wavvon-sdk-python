from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_push_subscription_body_keys import PutPushSubscriptionBodyKeys
    from ..models.put_push_subscription_body_notify import PutPushSubscriptionBodyNotify


T = TypeVar("T", bound="PutPushSubscriptionBody")


@_attrs_define
class PutPushSubscriptionBody:
    """
    Attributes:
        endpoint (str):
        keys (PutPushSubscriptionBodyKeys):
        notify (PutPushSubscriptionBodyNotify | Unset): The client's notify modes for this hub; mentions, replies and
            DMs push under all and mentions, never under silent (channel over hub).
    """

    endpoint: str
    keys: PutPushSubscriptionBodyKeys
    notify: PutPushSubscriptionBodyNotify | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        keys = self.keys.to_dict()

        notify: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notify, Unset):
            notify = self.notify.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "keys": keys,
            }
        )
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.put_push_subscription_body_keys import PutPushSubscriptionBodyKeys
        from ..models.put_push_subscription_body_notify import (
            PutPushSubscriptionBodyNotify,
        )

        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        keys = PutPushSubscriptionBodyKeys.from_dict(d.pop("keys"))

        _notify = d.pop("notify", UNSET)
        notify: PutPushSubscriptionBodyNotify | Unset
        if isinstance(_notify, Unset):
            notify = UNSET
        else:
            notify = PutPushSubscriptionBodyNotify.from_dict(_notify)

        put_push_subscription_body = cls(
            endpoint=endpoint,
            keys=keys,
            notify=notify,
        )

        put_push_subscription_body.additional_properties = d
        return put_push_subscription_body

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
