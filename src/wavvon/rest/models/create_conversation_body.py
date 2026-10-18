from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_conversation_body_member_hubs import (
        CreateConversationBodyMemberHubs,
    )
    from ..models.create_conversation_body_member_masters import (
        CreateConversationBodyMemberMasters,
    )


T = TypeVar("T", bound="CreateConversationBody")


@_attrs_define
class CreateConversationBody:
    """
    Attributes:
        members (list[str]):
        member_hubs (CreateConversationBodyMemberHubs | Unset):
        member_masters (CreateConversationBodyMemberMasters | Unset):
    """

    members: list[str]
    member_hubs: CreateConversationBodyMemberHubs | Unset = UNSET
    member_masters: CreateConversationBodyMemberMasters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = self.members

        member_hubs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_hubs, Unset):
            member_hubs = self.member_hubs.to_dict()

        member_masters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_masters, Unset):
            member_masters = self.member_masters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
            }
        )
        if member_hubs is not UNSET:
            field_dict["member_hubs"] = member_hubs
        if member_masters is not UNSET:
            field_dict["member_masters"] = member_masters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_conversation_body_member_hubs import (
            CreateConversationBodyMemberHubs,
        )
        from ..models.create_conversation_body_member_masters import (
            CreateConversationBodyMemberMasters,
        )

        d = dict(src_dict)
        members = cast(list[str], d.pop("members"))

        _member_hubs = d.pop("member_hubs", UNSET)
        member_hubs: CreateConversationBodyMemberHubs | Unset
        if isinstance(_member_hubs, Unset):
            member_hubs = UNSET
        else:
            member_hubs = CreateConversationBodyMemberHubs.from_dict(_member_hubs)

        _member_masters = d.pop("member_masters", UNSET)
        member_masters: CreateConversationBodyMemberMasters | Unset
        if isinstance(_member_masters, Unset):
            member_masters = UNSET
        else:
            member_masters = CreateConversationBodyMemberMasters.from_dict(
                _member_masters
            )

        create_conversation_body = cls(
            members=members,
            member_hubs=member_hubs,
            member_masters=member_masters,
        )

        create_conversation_body.additional_properties = d
        return create_conversation_body

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
