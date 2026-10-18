from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueAdminBadgeBody")


@_attrs_define
class IssueAdminBadgeBody:
    """
    Attributes:
        recipient_hub_url (str):
        label (str):
        note (str | Unset):
        expires_days (int | Unset):
    """

    recipient_hub_url: str
    label: str
    note: str | Unset = UNSET
    expires_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipient_hub_url = self.recipient_hub_url

        label = self.label

        note = self.note

        expires_days = self.expires_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipient_hub_url": recipient_hub_url,
                "label": label,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if expires_days is not UNSET:
            field_dict["expires_days"] = expires_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        recipient_hub_url = d.pop("recipient_hub_url")

        label = d.pop("label")

        note = d.pop("note", UNSET)

        expires_days = d.pop("expires_days", UNSET)

        issue_admin_badge_body = cls(
            recipient_hub_url=recipient_hub_url,
            label=label,
            note=note,
            expires_days=expires_days,
        )

        issue_admin_badge_body.additional_properties = d
        return issue_admin_badge_body

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
