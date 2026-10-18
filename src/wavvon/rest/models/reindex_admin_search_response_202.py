from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reindex_admin_search_response_202_status import (
    ReindexAdminSearchResponse202Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexAdminSearchResponse202")


@_attrs_define
class ReindexAdminSearchResponse202:
    """
    Attributes:
        status (ReindexAdminSearchResponse202Status | Unset):
    """

    status: ReindexAdminSearchResponse202Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ReindexAdminSearchResponse202Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReindexAdminSearchResponse202Status(_status)

        reindex_admin_search_response_202 = cls(
            status=status,
        )

        reindex_admin_search_response_202.additional_properties = d
        return reindex_admin_search_response_202

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
