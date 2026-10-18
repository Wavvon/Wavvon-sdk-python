from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignAdminDirectoryListingBody")


@_attrs_define
class SignAdminDirectoryListingBody:
    """
    Attributes:
        hub_url (str):
        tags (list[str]):
        language (str):
        bio (str):
        invite_code (str | Unset):
    """

    hub_url: str
    tags: list[str]
    language: str
    bio: str
    invite_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub_url = self.hub_url

        tags = self.tags

        language = self.language

        bio = self.bio

        invite_code = self.invite_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hub_url": hub_url,
                "tags": tags,
                "language": language,
                "bio": bio,
            }
        )
        if invite_code is not UNSET:
            field_dict["invite_code"] = invite_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hub_url = d.pop("hub_url")

        tags = cast(list[str], d.pop("tags"))

        language = d.pop("language")

        bio = d.pop("bio")

        invite_code = d.pop("invite_code", UNSET)

        sign_admin_directory_listing_body = cls(
            hub_url=hub_url,
            tags=tags,
            language=language,
            bio=bio,
            invite_code=invite_code,
        )

        sign_admin_directory_listing_body.additional_properties = d
        return sign_admin_directory_listing_body

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
