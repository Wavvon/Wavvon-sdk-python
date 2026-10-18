from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.message_embeds_item import MessageEmbedsItem
    from ..models.message_game import MessageGame
    from ..models.reaction import Reaction
    from ..models.reply_context import ReplyContext


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        sender (str | Unset):
        sender_name (None | str | Unset):
        content (str | Unset):
        created_at (int | Unset):
        edited_at (int | None | Unset):
        attachments (list[Attachment] | Unset):
        reactions (list[Reaction] | Unset):
        reply_to (ReplyContext | Unset):
        visible_to_pubkey (str | Unset): Omitted unless set. When present, only the named user should see this message
            (ephemeral bot replies).
        reply_count (int | Unset): Number of direct replies; non-zero only on thread roots.
        embeds (list[MessageEmbedsItem] | Unset): Omitted unless set. Rich embeds authored by an app (docs/apps.md).
        game (MessageGame | Unset): Omitted unless set. Game-modal launch card authored by an app (docs/apps.md).
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    sender: str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    content: str | Unset = UNSET
    created_at: int | Unset = UNSET
    edited_at: int | None | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    reactions: list[Reaction] | Unset = UNSET
    reply_to: ReplyContext | Unset = UNSET
    visible_to_pubkey: str | Unset = UNSET
    reply_count: int | Unset = UNSET
    embeds: list[MessageEmbedsItem] | Unset = UNSET
    game: MessageGame | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        sender = self.sender

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        content = self.content

        created_at = self.created_at

        edited_at: int | None | Unset
        if isinstance(self.edited_at, Unset):
            edited_at = UNSET
        else:
            edited_at = self.edited_at

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)

        reply_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_to, Unset):
            reply_to = self.reply_to.to_dict()

        visible_to_pubkey = self.visible_to_pubkey

        reply_count = self.reply_count

        embeds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.embeds, Unset):
            embeds = []
            for embeds_item_data in self.embeds:
                embeds_item = embeds_item_data.to_dict()
                embeds.append(embeds_item)

        game: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game, Unset):
            game = self.game.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if visible_to_pubkey is not UNSET:
            field_dict["visible_to_pubkey"] = visible_to_pubkey
        if reply_count is not UNSET:
            field_dict["reply_count"] = reply_count
        if embeds is not UNSET:
            field_dict["embeds"] = embeds
        if game is not UNSET:
            field_dict["game"] = game

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attachment import Attachment
        from ..models.message_embeds_item import MessageEmbedsItem
        from ..models.message_game import MessageGame
        from ..models.reaction import Reaction
        from ..models.reply_context import ReplyContext

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        sender = d.pop("sender", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        content = d.pop("content", UNSET)

        created_at = d.pop("created_at", UNSET)

        def _parse_edited_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edited_at = _parse_edited_at(d.pop("edited_at", UNSET))

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _reactions = d.pop("reactions", UNSET)
        reactions: list[Reaction] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = Reaction.from_dict(reactions_item_data)

                reactions.append(reactions_item)

        _reply_to = d.pop("reply_to", UNSET)
        reply_to: ReplyContext | Unset
        if isinstance(_reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = ReplyContext.from_dict(_reply_to)

        visible_to_pubkey = d.pop("visible_to_pubkey", UNSET)

        reply_count = d.pop("reply_count", UNSET)

        _embeds = d.pop("embeds", UNSET)
        embeds: list[MessageEmbedsItem] | Unset = UNSET
        if _embeds is not UNSET:
            embeds = []
            for embeds_item_data in _embeds:
                embeds_item = MessageEmbedsItem.from_dict(embeds_item_data)

                embeds.append(embeds_item)

        _game = d.pop("game", UNSET)
        game: MessageGame | Unset
        if isinstance(_game, Unset):
            game = UNSET
        else:
            game = MessageGame.from_dict(_game)

        message = cls(
            id=id,
            channel_id=channel_id,
            sender=sender,
            sender_name=sender_name,
            content=content,
            created_at=created_at,
            edited_at=edited_at,
            attachments=attachments,
            reactions=reactions,
            reply_to=reply_to,
            visible_to_pubkey=visible_to_pubkey,
            reply_count=reply_count,
            embeds=embeds,
            game=game,
        )

        message.additional_properties = d
        return message

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
