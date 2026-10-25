from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hub_event_type import HubEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hub_event_payload import HubEventPayload


T = TypeVar("T", bound="HubEvent")


@_attrs_define
class HubEvent:
    """One envelope for live push, replay, polling and outgoing webhooks (docs/apps.md).

    Attributes:
        type_ (HubEventType):
        seq (int):
        event (str):  Example: member.joined.
        hub_url (str):
        at (int): Unix seconds
        payload (HubEventPayload):
        actor_pubkey (str | Unset):
        target_pubkey (str | Unset):
        channel_id (str | Unset):
        replayed (bool | Unset): Set on events read back from the audit log (Resume and polling).
        webhook_id (str | Unset): Outgoing webhooks only.
        truncated (bool | Unset): Outgoing webhooks only, when the payload was cut to the size cap.
    """

    type_: HubEventType
    seq: int
    event: str
    hub_url: str
    at: int
    payload: HubEventPayload
    actor_pubkey: str | Unset = UNSET
    target_pubkey: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    replayed: bool | Unset = UNSET
    webhook_id: str | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        seq = self.seq

        event = self.event

        hub_url = self.hub_url

        at = self.at

        payload = self.payload.to_dict()

        actor_pubkey = self.actor_pubkey

        target_pubkey = self.target_pubkey

        channel_id = self.channel_id

        replayed = self.replayed

        webhook_id = self.webhook_id

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "seq": seq,
                "event": event,
                "hub_url": hub_url,
                "at": at,
                "payload": payload,
            }
        )
        if actor_pubkey is not UNSET:
            field_dict["actor_pubkey"] = actor_pubkey
        if target_pubkey is not UNSET:
            field_dict["target_pubkey"] = target_pubkey
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if replayed is not UNSET:
            field_dict["replayed"] = replayed
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hub_event_payload import HubEventPayload

        d = dict(src_dict)
        type_ = HubEventType(d.pop("type"))

        seq = d.pop("seq")

        event = d.pop("event")

        hub_url = d.pop("hub_url")

        at = d.pop("at")

        payload = HubEventPayload.from_dict(d.pop("payload"))

        actor_pubkey = d.pop("actor_pubkey", UNSET)

        target_pubkey = d.pop("target_pubkey", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        replayed = d.pop("replayed", UNSET)

        webhook_id = d.pop("webhook_id", UNSET)

        truncated = d.pop("truncated", UNSET)

        hub_event = cls(
            type_=type_,
            seq=seq,
            event=event,
            hub_url=hub_url,
            at=at,
            payload=payload,
            actor_pubkey=actor_pubkey,
            target_pubkey=target_pubkey,
            channel_id=channel_id,
            replayed=replayed,
            webhook_id=webhook_id,
            truncated=truncated,
        )

        hub_event.additional_properties = d
        return hub_event

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
