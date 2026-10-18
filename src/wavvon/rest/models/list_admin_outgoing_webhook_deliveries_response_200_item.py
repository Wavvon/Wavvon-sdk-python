from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminOutgoingWebhookDeliveriesResponse200Item")


@_attrs_define
class ListAdminOutgoingWebhookDeliveriesResponse200Item:
    """
    Attributes:
        id (str | Unset):
        webhook_id (str | Unset):
        event_type (str | Unset):
        event_seq (int | None | Unset):
        attempted_at (int | Unset):
        attempt_number (int | Unset):
        status_code (int | None | Unset):
        success (bool | Unset):
        error_msg (None | str | Unset):
    """

    id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    event_seq: int | None | Unset = UNSET
    attempted_at: int | Unset = UNSET
    attempt_number: int | Unset = UNSET
    status_code: int | None | Unset = UNSET
    success: bool | Unset = UNSET
    error_msg: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        webhook_id = self.webhook_id

        event_type = self.event_type

        event_seq: int | None | Unset
        if isinstance(self.event_seq, Unset):
            event_seq = UNSET
        else:
            event_seq = self.event_seq

        attempted_at = self.attempted_at

        attempt_number = self.attempt_number

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        success = self.success

        error_msg: None | str | Unset
        if isinstance(self.error_msg, Unset):
            error_msg = UNSET
        else:
            error_msg = self.error_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if event_seq is not UNSET:
            field_dict["event_seq"] = event_seq
        if attempted_at is not UNSET:
            field_dict["attempted_at"] = attempted_at
        if attempt_number is not UNSET:
            field_dict["attempt_number"] = attempt_number
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if success is not UNSET:
            field_dict["success"] = success
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        webhook_id = d.pop("webhook_id", UNSET)

        event_type = d.pop("event_type", UNSET)

        def _parse_event_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        event_seq = _parse_event_seq(d.pop("event_seq", UNSET))

        attempted_at = d.pop("attempted_at", UNSET)

        attempt_number = d.pop("attempt_number", UNSET)

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        success = d.pop("success", UNSET)

        def _parse_error_msg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_msg = _parse_error_msg(d.pop("error_msg", UNSET))

        list_admin_outgoing_webhook_deliveries_response_200_item = cls(
            id=id,
            webhook_id=webhook_id,
            event_type=event_type,
            event_seq=event_seq,
            attempted_at=attempted_at,
            attempt_number=attempt_number,
            status_code=status_code,
            success=success,
            error_msg=error_msg,
        )

        list_admin_outgoing_webhook_deliveries_response_200_item.additional_properties = d
        return list_admin_outgoing_webhook_deliveries_response_200_item

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
