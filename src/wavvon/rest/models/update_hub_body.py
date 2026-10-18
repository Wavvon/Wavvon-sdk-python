from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHubBody")


@_attrs_define
class UpdateHubBody:
    """
    Attributes:
        hub_name (str | Unset):
        hub_icon (None | str | Unset):
    """

    hub_name: str | Unset = UNSET
    hub_icon: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub_name = self.hub_name

        hub_icon: None | str | Unset
        if isinstance(self.hub_icon, Unset):
            hub_icon = UNSET
        else:
            hub_icon = self.hub_icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hub_name is not UNSET:
            field_dict["hub_name"] = hub_name
        if hub_icon is not UNSET:
            field_dict["hub_icon"] = hub_icon

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hub_name = d.pop("hub_name", UNSET)

        def _parse_hub_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hub_icon = _parse_hub_icon(d.pop("hub_icon", UNSET))

        update_hub_body = cls(
            hub_name=hub_name,
            hub_icon=hub_icon,
        )

        update_hub_body.additional_properties = d
        return update_hub_body

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
