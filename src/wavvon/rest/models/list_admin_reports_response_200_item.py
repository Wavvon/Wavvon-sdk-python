from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdminReportsResponse200Item")


@_attrs_define
class ListAdminReportsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        message_id (str | Unset):
        message_content (None | str | Unset):
        channel_id (str | Unset):
        reporter_pubkey (str | Unset):
        reason (str | Unset):
        reported_at (int | Unset):
        status (str | Unset):
    """

    id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    message_content: None | str | Unset = UNSET
    channel_id: str | Unset = UNSET
    reporter_pubkey: str | Unset = UNSET
    reason: str | Unset = UNSET
    reported_at: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message_id = self.message_id

        message_content: None | str | Unset
        if isinstance(self.message_content, Unset):
            message_content = UNSET
        else:
            message_content = self.message_content

        channel_id = self.channel_id

        reporter_pubkey = self.reporter_pubkey

        reason = self.reason

        reported_at = self.reported_at

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if message_content is not UNSET:
            field_dict["message_content"] = message_content
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if reporter_pubkey is not UNSET:
            field_dict["reporter_pubkey"] = reporter_pubkey
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reported_at is not UNSET:
            field_dict["reported_at"] = reported_at
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        message_id = d.pop("message_id", UNSET)

        def _parse_message_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_content = _parse_message_content(d.pop("message_content", UNSET))

        channel_id = d.pop("channel_id", UNSET)

        reporter_pubkey = d.pop("reporter_pubkey", UNSET)

        reason = d.pop("reason", UNSET)

        reported_at = d.pop("reported_at", UNSET)

        status = d.pop("status", UNSET)

        list_admin_reports_response_200_item = cls(
            id=id,
            message_id=message_id,
            message_content=message_content,
            channel_id=channel_id,
            reporter_pubkey=reporter_pubkey,
            reason=reason,
            reported_at=reported_at,
            status=status,
        )

        list_admin_reports_response_200_item.additional_properties = d
        return list_admin_reports_response_200_item

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
