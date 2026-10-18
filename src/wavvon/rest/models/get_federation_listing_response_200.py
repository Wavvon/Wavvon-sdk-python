from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFederationListingResponse200")


@_attrs_define
class GetFederationListingResponse200:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        public_key (str | Unset):
        hub_url (str | Unset):
        tags (list[str] | Unset):
        member_count_approx (int | Unset): Rounded down to the nearest 10
        listed (bool | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_key: str | Unset = UNSET
    hub_url: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    member_count_approx: int | Unset = UNSET
    listed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_key = self.public_key

        hub_url = self.hub_url

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        member_count_approx = self.member_count_approx

        listed = self.listed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if hub_url is not UNSET:
            field_dict["hub_url"] = hub_url
        if tags is not UNSET:
            field_dict["tags"] = tags
        if member_count_approx is not UNSET:
            field_dict["member_count_approx"] = member_count_approx
        if listed is not UNSET:
            field_dict["listed"] = listed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        public_key = d.pop("public_key", UNSET)

        hub_url = d.pop("hub_url", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        member_count_approx = d.pop("member_count_approx", UNSET)

        listed = d.pop("listed", UNSET)

        get_federation_listing_response_200 = cls(
            name=name,
            description=description,
            public_key=public_key,
            hub_url=hub_url,
            tags=tags,
            member_count_approx=member_count_approx,
            listed=listed,
        )

        get_federation_listing_response_200.additional_properties = d
        return get_federation_listing_response_200

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
