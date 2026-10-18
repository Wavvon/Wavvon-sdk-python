from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lobby_status_status import LobbyStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LobbyStatus")


@_attrs_define
class LobbyStatus:
    """
    Attributes:
        status (LobbyStatusStatus | Unset):
        required_level (int | Unset):
        current_level (int | Unset):
        entered_at (int | None | Unset):
        welcome_md (None | str | Unset):
    """

    status: LobbyStatusStatus | Unset = UNSET
    required_level: int | Unset = UNSET
    current_level: int | Unset = UNSET
    entered_at: int | None | Unset = UNSET
    welcome_md: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        required_level = self.required_level

        current_level = self.current_level

        entered_at: int | None | Unset
        if isinstance(self.entered_at, Unset):
            entered_at = UNSET
        else:
            entered_at = self.entered_at

        welcome_md: None | str | Unset
        if isinstance(self.welcome_md, Unset):
            welcome_md = UNSET
        else:
            welcome_md = self.welcome_md

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if required_level is not UNSET:
            field_dict["required_level"] = required_level
        if current_level is not UNSET:
            field_dict["current_level"] = current_level
        if entered_at is not UNSET:
            field_dict["entered_at"] = entered_at
        if welcome_md is not UNSET:
            field_dict["welcome_md"] = welcome_md

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: LobbyStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LobbyStatusStatus(_status)

        required_level = d.pop("required_level", UNSET)

        current_level = d.pop("current_level", UNSET)

        def _parse_entered_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        entered_at = _parse_entered_at(d.pop("entered_at", UNSET))

        def _parse_welcome_md(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        welcome_md = _parse_welcome_md(d.pop("welcome_md", UNSET))

        lobby_status = cls(
            status=status,
            required_level=required_level,
            current_level=current_level,
            entered_at=entered_at,
            welcome_md=welcome_md,
        )

        lobby_status.additional_properties = d
        return lobby_status

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
