from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_data_members_item import WidgetDataMembersItem
    from ..models.widget_data_voice_item import WidgetDataVoiceItem


T = TypeVar("T", bound="WidgetData")


@_attrs_define
class WidgetData:
    """What the public widget shows. Never a public key; invisible members and members with `widget_hidden` are not
    counted.

        Attributes:
            name (str):
            online_count (int):
            icon (str | Unset):
            members (list[WidgetDataMembersItem] | Unset): In `names` and `voice` modes.
            voice (list[WidgetDataVoiceItem] | Unset): In `voice` mode, the occupied voice rooms.
            invite_url (str | Unset):
    """

    name: str
    online_count: int
    icon: str | Unset = UNSET
    members: list[WidgetDataMembersItem] | Unset = UNSET
    voice: list[WidgetDataVoiceItem] | Unset = UNSET
    invite_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        online_count = self.online_count

        icon = self.icon

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        voice: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.voice, Unset):
            voice = []
            for voice_item_data in self.voice:
                voice_item = voice_item_data.to_dict()
                voice.append(voice_item)

        invite_url = self.invite_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "online_count": online_count,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if members is not UNSET:
            field_dict["members"] = members
        if voice is not UNSET:
            field_dict["voice"] = voice
        if invite_url is not UNSET:
            field_dict["invite_url"] = invite_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.widget_data_members_item import WidgetDataMembersItem
        from ..models.widget_data_voice_item import WidgetDataVoiceItem

        d = dict(src_dict)
        name = d.pop("name")

        online_count = d.pop("online_count")

        icon = d.pop("icon", UNSET)

        _members = d.pop("members", UNSET)
        members: list[WidgetDataMembersItem] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = WidgetDataMembersItem.from_dict(members_item_data)

                members.append(members_item)

        _voice = d.pop("voice", UNSET)
        voice: list[WidgetDataVoiceItem] | Unset = UNSET
        if _voice is not UNSET:
            voice = []
            for voice_item_data in _voice:
                voice_item = WidgetDataVoiceItem.from_dict(voice_item_data)

                voice.append(voice_item)

        invite_url = d.pop("invite_url", UNSET)

        widget_data = cls(
            name=name,
            online_count=online_count,
            icon=icon,
            members=members,
            voice=voice,
            invite_url=invite_url,
        )

        widget_data.additional_properties = d
        return widget_data

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
