from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_admin_audit_log_response_200_item_payload import (
        ListAdminAuditLogResponse200ItemPayload,
    )


T = TypeVar("T", bound="ListAdminAuditLogResponse200Item")


@_attrs_define
class ListAdminAuditLogResponse200Item:
    """
    Attributes:
        seq (int | Unset):
        event_type (str | Unset):
        at (int | Unset):
        actor_pubkey (None | str | Unset):
        target_pubkey (None | str | Unset):
        channel_id (None | str | Unset):
        payload (ListAdminAuditLogResponse200ItemPayload | Unset):
    """

    seq: int | Unset = UNSET
    event_type: str | Unset = UNSET
    at: int | Unset = UNSET
    actor_pubkey: None | str | Unset = UNSET
    target_pubkey: None | str | Unset = UNSET
    channel_id: None | str | Unset = UNSET
    payload: ListAdminAuditLogResponse200ItemPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        event_type = self.event_type

        at = self.at

        actor_pubkey: None | str | Unset
        if isinstance(self.actor_pubkey, Unset):
            actor_pubkey = UNSET
        else:
            actor_pubkey = self.actor_pubkey

        target_pubkey: None | str | Unset
        if isinstance(self.target_pubkey, Unset):
            target_pubkey = UNSET
        else:
            target_pubkey = self.target_pubkey

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seq is not UNSET:
            field_dict["seq"] = seq
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if at is not UNSET:
            field_dict["at"] = at
        if actor_pubkey is not UNSET:
            field_dict["actor_pubkey"] = actor_pubkey
        if target_pubkey is not UNSET:
            field_dict["target_pubkey"] = target_pubkey
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_admin_audit_log_response_200_item_payload import (
            ListAdminAuditLogResponse200ItemPayload,
        )

        d = dict(src_dict)
        seq = d.pop("seq", UNSET)

        event_type = d.pop("event_type", UNSET)

        at = d.pop("at", UNSET)

        def _parse_actor_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_pubkey = _parse_actor_pubkey(d.pop("actor_pubkey", UNSET))

        def _parse_target_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_pubkey = _parse_target_pubkey(d.pop("target_pubkey", UNSET))

        def _parse_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        _payload = d.pop("payload", UNSET)
        payload: ListAdminAuditLogResponse200ItemPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ListAdminAuditLogResponse200ItemPayload.from_dict(_payload)

        list_admin_audit_log_response_200_item = cls(
            seq=seq,
            event_type=event_type,
            at=at,
            actor_pubkey=actor_pubkey,
            target_pubkey=target_pubkey,
            channel_id=channel_id,
            payload=payload,
        )

        list_admin_audit_log_response_200_item.additional_properties = d
        return list_admin_audit_log_response_200_item

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
