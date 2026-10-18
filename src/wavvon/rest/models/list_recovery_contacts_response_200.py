from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_recovery_contacts_response_200_contacts_item import (
        ListRecoveryContactsResponse200ContactsItem,
    )


T = TypeVar("T", bound="ListRecoveryContactsResponse200")


@_attrs_define
class ListRecoveryContactsResponse200:
    """
    Attributes:
        owner_pubkey (str | Unset):
        contacts (list[ListRecoveryContactsResponse200ContactsItem] | Unset):
        threshold (int | Unset):
    """

    owner_pubkey: str | Unset = UNSET
    contacts: list[ListRecoveryContactsResponse200ContactsItem] | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_pubkey = self.owner_pubkey

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_pubkey is not UNSET:
            field_dict["owner_pubkey"] = owner_pubkey
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_recovery_contacts_response_200_contacts_item import (
            ListRecoveryContactsResponse200ContactsItem,
        )

        d = dict(src_dict)
        owner_pubkey = d.pop("owner_pubkey", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[ListRecoveryContactsResponse200ContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = ListRecoveryContactsResponse200ContactsItem.from_dict(
                    contacts_item_data
                )

                contacts.append(contacts_item)

        threshold = d.pop("threshold", UNSET)

        list_recovery_contacts_response_200 = cls(
            owner_pubkey=owner_pubkey,
            contacts=contacts,
            threshold=threshold,
        )

        list_recovery_contacts_response_200.additional_properties = d
        return list_recovery_contacts_response_200

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
