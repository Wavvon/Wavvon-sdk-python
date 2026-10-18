from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.game_launch_card import GameLaunchCard


T = TypeVar("T", bound="CreateAllianceChannelMessageBody")


@_attrs_define
class CreateAllianceChannelMessageBody:
    """
    Attributes:
        content (str):
        attachments (list[Attachment] | Unset):
        reply_to (str | Unset):
        game (GameLaunchCard | Unset):
    """

    content: str
    attachments: list[Attachment] | Unset = UNSET
    reply_to: str | Unset = UNSET
    game: GameLaunchCard | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        reply_to = self.reply_to

        game: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game, Unset):
            game = self.game.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if game is not UNSET:
            field_dict["game"] = game

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.game_launch_card import GameLaunchCard

        d = dict(src_dict)
        content = d.pop("content")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        reply_to = d.pop("reply_to", UNSET)

        _game = d.pop("game", UNSET)
        game: GameLaunchCard | Unset
        if isinstance(_game, Unset):
            game = UNSET
        else:
            game = GameLaunchCard.from_dict(_game)

        create_alliance_channel_message_body = cls(
            content=content,
            attachments=attachments,
            reply_to=reply_to,
            game=game,
        )

        create_alliance_channel_message_body.additional_properties = d
        return create_alliance_channel_message_body

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
