from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListMeCredentialsResponse200Item")


@_attrs_define
class ListMeCredentialsResponse200Item:
    """
    Attributes:
        id (str | Unset):
        friendly_name (None | str | Unset):
        aaguid (None | str | Unset):
        created_at (int | Unset):
        last_used_at (int | None | Unset):
    """

    id: str | Unset = UNSET
    friendly_name: None | str | Unset = UNSET
    aaguid: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    last_used_at: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        friendly_name: None | str | Unset
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        aaguid: None | str | Unset
        if isinstance(self.aaguid, Unset):
            aaguid = UNSET
        else:
            aaguid = self.aaguid

        created_at = self.created_at

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
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if aaguid is not UNSET:
            field_dict["aaguid"] = aaguid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_friendly_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        friendly_name = _parse_friendly_name(d.pop("friendly_name", UNSET))

        def _parse_aaguid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aaguid = _parse_aaguid(d.pop("aaguid", UNSET))

        created_at = d.pop("created_at", UNSET)

        def _parse_last_used_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        list_me_credentials_response_200_item = cls(
            id=id,
            friendly_name=friendly_name,
            aaguid=aaguid,
            created_at=created_at,
            last_used_at=last_used_at,
        )

        list_me_credentials_response_200_item.additional_properties = d
        return list_me_credentials_response_200_item

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
