from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAdminSettingsModerationResponse200")


@_attrs_define
class GetAdminSettingsModerationResponse200:
    """
    Attributes:
        webhook_secret_set (bool):
        circuit_open (bool):
        circuit_open_until (int | None):
        webhook_url (str | Unset): Omitted unless set.
    """

    webhook_secret_set: bool
    circuit_open: bool
    circuit_open_until: int | None
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_secret_set = self.webhook_secret_set

        circuit_open = self.circuit_open

        circuit_open_until: int | None
        circuit_open_until = self.circuit_open_until

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook_secret_set": webhook_secret_set,
                "circuit_open": circuit_open,
                "circuit_open_until": circuit_open_until,
            }
        )
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        webhook_secret_set = d.pop("webhook_secret_set")

        circuit_open = d.pop("circuit_open")

        def _parse_circuit_open_until(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        circuit_open_until = _parse_circuit_open_until(d.pop("circuit_open_until"))

        webhook_url = d.pop("webhook_url", UNSET)

        get_admin_settings_moderation_response_200 = cls(
            webhook_secret_set=webhook_secret_set,
            circuit_open=circuit_open,
            circuit_open_until=circuit_open_until,
            webhook_url=webhook_url,
        )

        get_admin_settings_moderation_response_200.additional_properties = d
        return get_admin_settings_moderation_response_200

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
