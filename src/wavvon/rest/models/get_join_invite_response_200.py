from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.landing import Landing


T = TypeVar("T", bound="GetJoinInviteResponse200")


@_attrs_define
class GetJoinInviteResponse200:
    """
    Attributes:
        hub_name (str | Unset):
        description (None | str | Unset):
        member_count (int | Unset):
        online_count (int | Unset): Connected members, not counting invisible ones.
        landing (Landing | Unset): How the invite landing looks (hubs advertising `hub.landing`). Each field is omitted
            when unset.
        code (str | Unset):
    """

    hub_name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    member_count: int | Unset = UNSET
    online_count: int | Unset = UNSET
    landing: Landing | Unset = UNSET
    code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub_name = self.hub_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        member_count = self.member_count

        online_count = self.online_count

        landing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.landing, Unset):
            landing = self.landing.to_dict()

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hub_name is not UNSET:
            field_dict["hub_name"] = hub_name
        if description is not UNSET:
            field_dict["description"] = description
        if member_count is not UNSET:
            field_dict["member_count"] = member_count
        if online_count is not UNSET:
            field_dict["online_count"] = online_count
        if landing is not UNSET:
            field_dict["landing"] = landing
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.landing import Landing

        d = dict(src_dict)
        hub_name = d.pop("hub_name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        member_count = d.pop("member_count", UNSET)

        online_count = d.pop("online_count", UNSET)

        _landing = d.pop("landing", UNSET)
        landing: Landing | Unset
        if isinstance(_landing, Unset):
            landing = UNSET
        else:
            landing = Landing.from_dict(_landing)

        code = d.pop("code", UNSET)

        get_join_invite_response_200 = cls(
            hub_name=hub_name,
            description=description,
            member_count=member_count,
            online_count=online_count,
            landing=landing,
            code=code,
        )

        get_join_invite_response_200.additional_properties = d
        return get_join_invite_response_200

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
