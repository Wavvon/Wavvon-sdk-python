from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_moderation_history_response_200_entries_item_policy import (
    GetModerationHistoryResponse200EntriesItemPolicy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetModerationHistoryResponse200EntriesItem")


@_attrs_define
class GetModerationHistoryResponse200EntriesItem:
    """
    Attributes:
        source_hub_pubkey (str | Unset):
        policy (GetModerationHistoryResponse200EntriesItemPolicy | Unset):
        reason (None | str | Unset):
        added_at (int | Unset):
    """

    source_hub_pubkey: str | Unset = UNSET
    policy: GetModerationHistoryResponse200EntriesItemPolicy | Unset = UNSET
    reason: None | str | Unset = UNSET
    added_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_hub_pubkey = self.source_hub_pubkey

        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_hub_pubkey is not UNSET:
            field_dict["source_hub_pubkey"] = source_hub_pubkey
        if policy is not UNSET:
            field_dict["policy"] = policy
        if reason is not UNSET:
            field_dict["reason"] = reason
        if added_at is not UNSET:
            field_dict["added_at"] = added_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_hub_pubkey = d.pop("source_hub_pubkey", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: GetModerationHistoryResponse200EntriesItemPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = GetModerationHistoryResponse200EntriesItemPolicy(_policy)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        added_at = d.pop("added_at", UNSET)

        get_moderation_history_response_200_entries_item = cls(
            source_hub_pubkey=source_hub_pubkey,
            policy=policy,
            reason=reason,
            added_at=added_at,
        )

        get_moderation_history_response_200_entries_item.additional_properties = d
        return get_moderation_history_response_200_entries_item

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
