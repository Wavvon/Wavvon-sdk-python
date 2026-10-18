from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListMeDevicesResponse200Item")


@_attrs_define
class ListMeDevicesResponse200Item:
    """
    Attributes:
        id (str | Unset):
        device_name (None | str | Unset):
        created_at (int | Unset):
        expires_at (int | Unset):
        last_used_at (int | None | Unset):
    """

    id: str | Unset = UNSET
    device_name: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    last_used_at: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        created_at = self.created_at

        expires_at = self.expires_at

        last_used_at: int | None | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("device_name", UNSET))

        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        def _parse_last_used_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        list_me_devices_response_200_item = cls(
            id=id,
            device_name=device_name,
            created_at=created_at,
            expires_at=expires_at,
            last_used_at=last_used_at,
        )

        list_me_devices_response_200_item.additional_properties = d
        return list_me_devices_response_200_item

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
