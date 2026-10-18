from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_federation_banlist_response_200_payload import (
        GetFederationBanlistResponse200Payload,
    )


T = TypeVar("T", bound="GetFederationBanlistResponse200")


@_attrs_define
class GetFederationBanlistResponse200:
    """
    Attributes:
        payload (GetFederationBanlistResponse200Payload | Unset):
        signature (str | Unset):
    """

    payload: GetFederationBanlistResponse200Payload | Unset = UNSET
    signature: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_federation_banlist_response_200_payload import (
            GetFederationBanlistResponse200Payload,
        )

        d = dict(src_dict)
        _payload = d.pop("payload", UNSET)
        payload: GetFederationBanlistResponse200Payload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = GetFederationBanlistResponse200Payload.from_dict(_payload)

        signature = d.pop("signature", UNSET)

        get_federation_banlist_response_200 = cls(
            payload=payload,
            signature=signature,
        )

        get_federation_banlist_response_200.additional_properties = d
        return get_federation_banlist_response_200

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
