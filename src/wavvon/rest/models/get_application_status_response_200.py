from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_application_status_response_200_state import (
    GetApplicationStatusResponse200State,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApplicationStatusResponse200")


@_attrs_define
class GetApplicationStatusResponse200:
    """
    Attributes:
        state (GetApplicationStatusResponse200State):
        reason (str | Unset):
        retry_after (int | Unset): Unix seconds from which a rejected applicant may apply again.
    """

    state: GetApplicationStatusResponse200State
    reason: str | Unset = UNSET
    retry_after: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        reason = self.reason

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if retry_after is not UNSET:
            field_dict["retry_after"] = retry_after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = GetApplicationStatusResponse200State(d.pop("state"))

        reason = d.pop("reason", UNSET)

        retry_after = d.pop("retry_after", UNSET)

        get_application_status_response_200 = cls(
            state=state,
            reason=reason,
            retry_after=retry_after,
        )

        get_application_status_response_200.additional_properties = d
        return get_application_status_response_200

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
