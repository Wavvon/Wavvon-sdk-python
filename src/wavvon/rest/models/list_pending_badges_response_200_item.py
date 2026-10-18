from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_payload import BadgePayload


T = TypeVar("T", bound="ListPendingBadgesResponse200Item")


@_attrs_define
class ListPendingBadgesResponse200Item:
    """
    Attributes:
        id (str | Unset):
        from_hub_pubkey (str | Unset):
        from_hub_url (str | Unset):
        label (str | Unset):
        note (None | str | Unset):
        payload (BadgePayload | Unset): Canonical badge payload signed by the issuing hub.
        created_at (str | Unset):
    """

    id: str | Unset = UNSET
    from_hub_pubkey: str | Unset = UNSET
    from_hub_url: str | Unset = UNSET
    label: str | Unset = UNSET
    note: None | str | Unset = UNSET
    payload: BadgePayload | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        from_hub_pubkey = self.from_hub_pubkey

        from_hub_url = self.from_hub_url

        label = self.label

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if from_hub_pubkey is not UNSET:
            field_dict["from_hub_pubkey"] = from_hub_pubkey
        if from_hub_url is not UNSET:
            field_dict["from_hub_url"] = from_hub_url
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if payload is not UNSET:
            field_dict["payload"] = payload
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.badge_payload import BadgePayload

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        from_hub_pubkey = d.pop("from_hub_pubkey", UNSET)

        from_hub_url = d.pop("from_hub_url", UNSET)

        label = d.pop("label", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _payload = d.pop("payload", UNSET)
        payload: BadgePayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = BadgePayload.from_dict(_payload)

        created_at = d.pop("created_at", UNSET)

        list_pending_badges_response_200_item = cls(
            id=id,
            from_hub_pubkey=from_hub_pubkey,
            from_hub_url=from_hub_url,
            label=label,
            note=note,
            payload=payload,
            created_at=created_at,
        )

        list_pending_badges_response_200_item.additional_properties = d
        return list_pending_badges_response_200_item

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
