from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetHealthResponse200")


@_attrs_define
class GetHealthResponse200:
    """
    Attributes:
        status (str):  Example: ok.
        version (str): The hub's version.
        uptime_seconds (int):
        db_status (str): `ok`, or `error: ` followed by the reason the database did not answer.
    """

    status: str
    version: str
    uptime_seconds: int
    db_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        version = self.version

        uptime_seconds = self.uptime_seconds

        db_status = self.db_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "version": version,
                "uptime_seconds": uptime_seconds,
                "db_status": db_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        version = d.pop("version")

        uptime_seconds = d.pop("uptime_seconds")

        db_status = d.pop("db_status")

        get_health_response_200 = cls(
            status=status,
            version=version,
            uptime_seconds=uptime_seconds,
            db_status=db_status,
        )

        get_health_response_200.additional_properties = d
        return get_health_response_200

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
