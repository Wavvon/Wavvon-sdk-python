from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_admin_settings_banlist_response_200_sources_item import (
        GetAdminSettingsBanlistResponse200SourcesItem,
    )


T = TypeVar("T", bound="GetAdminSettingsBanlistResponse200")


@_attrs_define
class GetAdminSettingsBanlistResponse200:
    """
    Attributes:
        publish_banlist (bool | Unset):
        sources (list[GetAdminSettingsBanlistResponse200SourcesItem] | Unset):
    """

    publish_banlist: bool | Unset = UNSET
    sources: list[GetAdminSettingsBanlistResponse200SourcesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        publish_banlist = self.publish_banlist

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if publish_banlist is not UNSET:
            field_dict["publish_banlist"] = publish_banlist
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_admin_settings_banlist_response_200_sources_item import (
            GetAdminSettingsBanlistResponse200SourcesItem,
        )

        d = dict(src_dict)
        publish_banlist = d.pop("publish_banlist", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[GetAdminSettingsBanlistResponse200SourcesItem] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = GetAdminSettingsBanlistResponse200SourcesItem.from_dict(
                    sources_item_data
                )

                sources.append(sources_item)

        get_admin_settings_banlist_response_200 = cls(
            publish_banlist=publish_banlist,
            sources=sources,
        )

        get_admin_settings_banlist_response_200.additional_properties = d
        return get_admin_settings_banlist_response_200

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
