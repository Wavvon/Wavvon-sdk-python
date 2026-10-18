from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_user_permissions_response_200_sources_item import (
        ExplainUserPermissionsResponse200SourcesItem,
    )


T = TypeVar("T", bound="ExplainUserPermissionsResponse200")


@_attrs_define
class ExplainUserPermissionsResponse200:
    """
    Attributes:
        public_key (str | Unset):
        permission (str | Unset):
        channel_id (None | str | Unset):
        allowed (bool | Unset):
        is_owner (bool | Unset):
        sources (list[ExplainUserPermissionsResponse200SourcesItem] | Unset):
    """

    public_key: str | Unset = UNSET
    permission: str | Unset = UNSET
    channel_id: None | str | Unset = UNSET
    allowed: bool | Unset = UNSET
    is_owner: bool | Unset = UNSET
    sources: list[ExplainUserPermissionsResponse200SourcesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        permission = self.permission

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        allowed = self.allowed

        is_owner = self.is_owner

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if permission is not UNSET:
            field_dict["permission"] = permission
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if is_owner is not UNSET:
            field_dict["is_owner"] = is_owner
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.explain_user_permissions_response_200_sources_item import (
            ExplainUserPermissionsResponse200SourcesItem,
        )

        d = dict(src_dict)
        public_key = d.pop("public_key", UNSET)

        permission = d.pop("permission", UNSET)

        def _parse_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        allowed = d.pop("allowed", UNSET)

        is_owner = d.pop("is_owner", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ExplainUserPermissionsResponse200SourcesItem] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ExplainUserPermissionsResponse200SourcesItem.from_dict(
                    sources_item_data
                )

                sources.append(sources_item)

        explain_user_permissions_response_200 = cls(
            public_key=public_key,
            permission=permission,
            channel_id=channel_id,
            allowed=allowed,
            is_owner=is_owner,
            sources=sources,
        )

        explain_user_permissions_response_200.additional_properties = d
        return explain_user_permissions_response_200

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
