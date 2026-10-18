from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signed_member_change import SignedMemberChange


T = TypeVar("T", bound="CreateFriendBody")


@_attrs_define
class CreateFriendBody:
    """
    Attributes:
        public_key (str):
        signed (SignedMemberChange | Unset): The actor's signature over a group add or leave (wire-format.md, "Group DM
            member change"). Without it the change holds on this hub only; with it the hub carries the change to the other
            members' hubs. Only on a hub advertising `dms.group.signedmembers`.
        hub_url (str | Unset): Required for federated (cross-hub) friends
    """

    public_key: str
    signed: SignedMemberChange | Unset = UNSET
    hub_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        signed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signed, Unset):
            signed = self.signed.to_dict()

        hub_url = self.hub_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
            }
        )
        if signed is not UNSET:
            field_dict["signed"] = signed
        if hub_url is not UNSET:
            field_dict["hub_url"] = hub_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.signed_member_change import SignedMemberChange

        d = dict(src_dict)
        public_key = d.pop("public_key")

        _signed = d.pop("signed", UNSET)
        signed: SignedMemberChange | Unset
        if isinstance(_signed, Unset):
            signed = UNSET
        else:
            signed = SignedMemberChange.from_dict(_signed)

        hub_url = d.pop("hub_url", UNSET)

        create_friend_body = cls(
            public_key=public_key,
            signed=signed,
            hub_url=hub_url,
        )

        create_friend_body.additional_properties = d
        return create_friend_body

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
