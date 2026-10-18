from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subkey_cert import SubkeyCert


T = TypeVar("T", bound="CreateFederationDmMemberChangeBody")


@_attrs_define
class CreateFederationDmMemberChangeBody:
    """
    Attributes:
        conversation_id (str):
        actor (str):
        issued_at (int): unix seconds
        signature (str):
        added (list[str] | Unset):
        removed (list[str] | Unset):
        signer_cert (SubkeyCert | Unset):
    """

    conversation_id: str
    actor: str
    issued_at: int
    signature: str
    added: list[str] | Unset = UNSET
    removed: list[str] | Unset = UNSET
    signer_cert: SubkeyCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        actor = self.actor

        issued_at = self.issued_at

        signature = self.signature

        added: list[str] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added

        removed: list[str] | Unset = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "actor": actor,
                "issued_at": issued_at,
                "signature": signature,
            }
        )
        if added is not UNSET:
            field_dict["added"] = added
        if removed is not UNSET:
            field_dict["removed"] = removed
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.subkey_cert import SubkeyCert

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        actor = d.pop("actor")

        issued_at = d.pop("issued_at")

        signature = d.pop("signature")

        added = cast(list[str], d.pop("added", UNSET))

        removed = cast(list[str], d.pop("removed", UNSET))

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: SubkeyCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = SubkeyCert.from_dict(_signer_cert)

        create_federation_dm_member_change_body = cls(
            conversation_id=conversation_id,
            actor=actor,
            issued_at=issued_at,
            signature=signature,
            added=added,
            removed=removed,
            signer_cert=signer_cert,
        )

        create_federation_dm_member_change_body.additional_properties = d
        return create_federation_dm_member_change_body

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
