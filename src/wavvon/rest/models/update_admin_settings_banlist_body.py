from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAdminSettingsBanlistBody")


@_attrs_define
class UpdateAdminSettingsBanlistBody:
    """
    Attributes:
        publish_banlist (bool):
    """

    publish_banlist: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        publish_banlist = self.publish_banlist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publish_banlist": publish_banlist,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        publish_banlist = d.pop("publish_banlist")

        update_admin_settings_banlist_body = cls(
            publish_banlist=publish_banlist,
        )

        update_admin_settings_banlist_body.additional_properties = d
        return update_admin_settings_banlist_body

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
