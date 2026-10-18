from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAlliancePushInviteBody")


@_attrs_define
class CreateAlliancePushInviteBody:
    """
    Attributes:
        target_hub_url (str):
        own_hub_url (str):
        message (None | str | Unset):
    """

    target_hub_url: str
    own_hub_url: str
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_hub_url = self.target_hub_url

        own_hub_url = self.own_hub_url

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_hub_url": target_hub_url,
                "own_hub_url": own_hub_url,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target_hub_url = d.pop("target_hub_url")

        own_hub_url = d.pop("own_hub_url")

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        create_alliance_push_invite_body = cls(
            target_hub_url=target_hub_url,
            own_hub_url=own_hub_url,
            message=message,
        )

        create_alliance_push_invite_body.additional_properties = d
        return create_alliance_push_invite_body

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
