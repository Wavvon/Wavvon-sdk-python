from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.explain_user_permissions_response_200_sources_item_kind import (
    ExplainUserPermissionsResponse200SourcesItemKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExplainUserPermissionsResponse200SourcesItem")


@_attrs_define
class ExplainUserPermissionsResponse200SourcesItem:
    """
    Attributes:
        role_id (str | Unset):
        role_name (str | Unset):
        kind (ExplainUserPermissionsResponse200SourcesItemKind | Unset):
        channel_id (None | str | Unset):
    """

    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    kind: ExplainUserPermissionsResponse200SourcesItemKind | Unset = UNSET
    channel_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        role_name = self.role_name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role_id = d.pop("role_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: ExplainUserPermissionsResponse200SourcesItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ExplainUserPermissionsResponse200SourcesItemKind(_kind)

        def _parse_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        explain_user_permissions_response_200_sources_item = cls(
            role_id=role_id,
            role_name=role_name,
            kind=kind,
            channel_id=channel_id,
        )

        explain_user_permissions_response_200_sources_item.additional_properties = d
        return explain_user_permissions_response_200_sources_item

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
