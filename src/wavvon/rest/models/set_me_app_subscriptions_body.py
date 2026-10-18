from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_me_app_subscriptions_body_subscriptions_item import (
        SetMeAppSubscriptionsBodySubscriptionsItem,
    )


T = TypeVar("T", bound="SetMeAppSubscriptionsBody")


@_attrs_define
class SetMeAppSubscriptionsBody:
    """
    Attributes:
        subscriptions (list[SetMeAppSubscriptionsBodySubscriptionsItem]):
    """

    subscriptions: list[SetMeAppSubscriptionsBodySubscriptionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriptions = []
        for subscriptions_item_data in self.subscriptions:
            subscriptions_item = subscriptions_item_data.to_dict()
            subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptions": subscriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_me_app_subscriptions_body_subscriptions_item import (
            SetMeAppSubscriptionsBodySubscriptionsItem,
        )

        d = dict(src_dict)
        subscriptions = []
        _subscriptions = d.pop("subscriptions")
        for subscriptions_item_data in _subscriptions:
            subscriptions_item = SetMeAppSubscriptionsBodySubscriptionsItem.from_dict(
                subscriptions_item_data
            )

            subscriptions.append(subscriptions_item)

        set_me_app_subscriptions_body = cls(
            subscriptions=subscriptions,
        )

        set_me_app_subscriptions_body.additional_properties = d
        return set_me_app_subscriptions_body

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
