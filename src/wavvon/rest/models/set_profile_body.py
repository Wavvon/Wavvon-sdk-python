from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_hub_entry import PublicHubEntry


T = TypeVar("T", bound="SetProfileBody")


@_attrs_define
class SetProfileBody:
    """
    Attributes:
        pubkey (str):
        display_name (str):
        public_hubs (list[PublicHubEntry]):
        issued_at (int):
        signature (str):
        avatar (str | Unset):
    """

    pubkey: str
    display_name: str
    public_hubs: list[PublicHubEntry]
    issued_at: int
    signature: str
    avatar: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pubkey = self.pubkey

        display_name = self.display_name

        public_hubs = []
        for public_hubs_item_data in self.public_hubs:
            public_hubs_item = public_hubs_item_data.to_dict()
            public_hubs.append(public_hubs_item)

        issued_at = self.issued_at

        signature = self.signature

        avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pubkey": pubkey,
                "display_name": display_name,
                "public_hubs": public_hubs,
                "issued_at": issued_at,
                "signature": signature,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.public_hub_entry import PublicHubEntry

        d = dict(src_dict)
        pubkey = d.pop("pubkey")

        display_name = d.pop("display_name")

        public_hubs = []
        _public_hubs = d.pop("public_hubs")
        for public_hubs_item_data in _public_hubs:
            public_hubs_item = PublicHubEntry.from_dict(public_hubs_item_data)

            public_hubs.append(public_hubs_item)

        issued_at = d.pop("issued_at")

        signature = d.pop("signature")

        avatar = d.pop("avatar", UNSET)

        set_profile_body = cls(
            pubkey=pubkey,
            display_name=display_name,
            public_hubs=public_hubs,
            issued_at=issued_at,
            signature=signature,
            avatar=avatar,
        )

        set_profile_body.additional_properties = d
        return set_profile_body

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
