from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signed_member_change_signer_cert import SignedMemberChangeSignerCert


T = TypeVar("T", bound="SignedMemberChange")


@_attrs_define
class SignedMemberChange:
    """The actor's signature over a group add or leave (wire-format.md, "Group DM member change"). Without it the change
    holds on this hub only; with it the hub carries the change to the other members' hubs. Only on a hub advertising
    `dms.group.signedmembers`.

        Attributes:
            issued_at (int): unix seconds
            signature (str):
            signer_cert (SignedMemberChangeSignerCert | Unset): When the signing key is not the actor's own, the master-
                signed cert tying the two.
    """

    issued_at: int
    signature: str
    signer_cert: SignedMemberChangeSignerCert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issued_at = self.issued_at

        signature = self.signature

        signer_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signer_cert, Unset):
            signer_cert = self.signer_cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issued_at": issued_at,
                "signature": signature,
            }
        )
        if signer_cert is not UNSET:
            field_dict["signer_cert"] = signer_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.signed_member_change_signer_cert import (
            SignedMemberChangeSignerCert,
        )

        d = dict(src_dict)
        issued_at = d.pop("issued_at")

        signature = d.pop("signature")

        _signer_cert = d.pop("signer_cert", UNSET)
        signer_cert: SignedMemberChangeSignerCert | Unset
        if isinstance(_signer_cert, Unset):
            signer_cert = UNSET
        else:
            signer_cert = SignedMemberChangeSignerCert.from_dict(_signer_cert)

        signed_member_change = cls(
            issued_at=issued_at,
            signature=signature,
            signer_cert=signer_cert,
        )

        signed_member_change.additional_properties = d
        return signed_member_change

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
