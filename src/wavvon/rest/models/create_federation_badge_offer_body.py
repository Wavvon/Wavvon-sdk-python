from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFederationBadgeOfferBody")


@_attrs_define
class CreateFederationBadgeOfferBody:
    """
    Attributes:
        from_hub_pubkey (str):
        from_hub_url (str):
        label (str):
        payload (str): Canonical BadgePayload JSON string
        signature (str): Hex Ed25519 signature over payload bytes
        note (None | str | Unset):
    """

    from_hub_pubkey: str
    from_hub_url: str
    label: str
    payload: str
    signature: str
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_hub_pubkey = self.from_hub_pubkey

        from_hub_url = self.from_hub_url

        label = self.label

        payload = self.payload

        signature = self.signature

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_hub_pubkey": from_hub_pubkey,
                "from_hub_url": from_hub_url,
                "label": label,
                "payload": payload,
                "signature": signature,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_hub_pubkey = d.pop("from_hub_pubkey")

        from_hub_url = d.pop("from_hub_url")

        label = d.pop("label")

        payload = d.pop("payload")

        signature = d.pop("signature")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        create_federation_badge_offer_body = cls(
            from_hub_pubkey=from_hub_pubkey,
            from_hub_url=from_hub_url,
            label=label,
            payload=payload,
            signature=signature,
            note=note,
        )

        create_federation_badge_offer_body.additional_properties = d
        return create_federation_badge_offer_body

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
