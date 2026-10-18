from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_alliance_channel_body_forum_remote_write import (
    CreateAllianceChannelBodyForumRemoteWrite,
)
from ..models.create_alliance_channel_body_voice_remote_join import (
    CreateAllianceChannelBodyVoiceRemoteJoin,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAllianceChannelBody")


@_attrs_define
class CreateAllianceChannelBody:
    """
    Attributes:
        channel_id (str):
        include_descendants (bool | Unset): Share the whole subtree beneath this channel, resolved live at read time
            rather than snapshotted. Default: False.
        forum_remote_write (CreateAllianceChannelBodyForumRemoteWrite | Unset): Federated forum writes into this channel
            (forum.md §9). Default replies_only.
        voice_remote_join (CreateAllianceChannelBodyVoiceRemoteJoin | Unset): Whether members of allied hubs may join
            voice here (alliances.md). Default allowed; `none` refuses the grant at redemption with
            `voice_remote_join_disabled`.
    """

    channel_id: str
    include_descendants: bool | Unset = False
    forum_remote_write: CreateAllianceChannelBodyForumRemoteWrite | Unset = UNSET
    voice_remote_join: CreateAllianceChannelBodyVoiceRemoteJoin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        include_descendants = self.include_descendants

        forum_remote_write: str | Unset = UNSET
        if not isinstance(self.forum_remote_write, Unset):
            forum_remote_write = self.forum_remote_write.value

        voice_remote_join: str | Unset = UNSET
        if not isinstance(self.voice_remote_join, Unset):
            voice_remote_join = self.voice_remote_join.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
            }
        )
        if include_descendants is not UNSET:
            field_dict["include_descendants"] = include_descendants
        if forum_remote_write is not UNSET:
            field_dict["forum_remote_write"] = forum_remote_write
        if voice_remote_join is not UNSET:
            field_dict["voice_remote_join"] = voice_remote_join

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        include_descendants = d.pop("include_descendants", UNSET)

        _forum_remote_write = d.pop("forum_remote_write", UNSET)
        forum_remote_write: CreateAllianceChannelBodyForumRemoteWrite | Unset
        if isinstance(_forum_remote_write, Unset):
            forum_remote_write = UNSET
        else:
            forum_remote_write = CreateAllianceChannelBodyForumRemoteWrite(
                _forum_remote_write
            )

        _voice_remote_join = d.pop("voice_remote_join", UNSET)
        voice_remote_join: CreateAllianceChannelBodyVoiceRemoteJoin | Unset
        if isinstance(_voice_remote_join, Unset):
            voice_remote_join = UNSET
        else:
            voice_remote_join = CreateAllianceChannelBodyVoiceRemoteJoin(
                _voice_remote_join
            )

        create_alliance_channel_body = cls(
            channel_id=channel_id,
            include_descendants=include_descendants,
            forum_remote_write=forum_remote_write,
            voice_remote_join=voice_remote_join,
        )

        create_alliance_channel_body.additional_properties = d
        return create_alliance_channel_body

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
