from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateMeCredentialBody")


@_attrs_define
class UpdateMeCredentialBody:
    """
    Attributes:
        friendly_name (str):
    """

    friendly_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friendly_name = self.friendly_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "friendly_name": friendly_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        friendly_name = d.pop("friendly_name")

        update_me_credential_body = cls(
            friendly_name=friendly_name,
        )

        update_me_credential_body.additional_properties = d
        return update_me_credential_body

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
