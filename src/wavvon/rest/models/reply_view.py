from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reaction import Reaction
    from ..models.reply_view_attachments_item import ReplyViewAttachmentsItem


T = TypeVar("T", bound="ReplyView")


@_attrs_define
class ReplyView:
    """
    Attributes:
        id (str):
        post_id (str):
        author_pubkey (None | str):
        body (None | str): Null on tombstoned replies
        created_at (int):
        is_deleted (bool):
        reactions (list[Reaction]):
        attachments (list[ReplyViewAttachmentsItem]):
        edited_at (int | Unset): Omitted when never edited
        reply_to_id (str | Unset): Omitted on top-level replies
        author_hub (str | Unset): Origin hub public key (hex) when authored through the alliance forum write-proxy.
            Omitted for local replies.
    """

    id: str
    post_id: str
    author_pubkey: None | str
    body: None | str
    created_at: int
    is_deleted: bool
    reactions: list[Reaction]
    attachments: list[ReplyViewAttachmentsItem]
    edited_at: int | Unset = UNSET
    reply_to_id: str | Unset = UNSET
    author_hub: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        post_id = self.post_id

        author_pubkey: None | str
        author_pubkey = self.author_pubkey

        body: None | str
        body = self.body

        created_at = self.created_at

        is_deleted = self.is_deleted

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        edited_at = self.edited_at

        reply_to_id = self.reply_to_id

        author_hub = self.author_hub

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "post_id": post_id,
                "author_pubkey": author_pubkey,
                "body": body,
                "created_at": created_at,
                "is_deleted": is_deleted,
                "reactions": reactions,
                "attachments": attachments,
            }
        )
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if reply_to_id is not UNSET:
            field_dict["reply_to_id"] = reply_to_id
        if author_hub is not UNSET:
            field_dict["author_hub"] = author_hub

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reaction import Reaction
        from ..models.reply_view_attachments_item import ReplyViewAttachmentsItem

        d = dict(src_dict)
        id = d.pop("id")

        post_id = d.pop("post_id")

        def _parse_author_pubkey(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author_pubkey = _parse_author_pubkey(d.pop("author_pubkey"))

        def _parse_body(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body = _parse_body(d.pop("body"))

        created_at = d.pop("created_at")

        is_deleted = d.pop("is_deleted")

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = Reaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = ReplyViewAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        edited_at = d.pop("edited_at", UNSET)

        reply_to_id = d.pop("reply_to_id", UNSET)

        author_hub = d.pop("author_hub", UNSET)

        reply_view = cls(
            id=id,
            post_id=post_id,
            author_pubkey=author_pubkey,
            body=body,
            created_at=created_at,
            is_deleted=is_deleted,
            reactions=reactions,
            attachments=attachments,
            edited_at=edited_at,
            reply_to_id=reply_to_id,
            author_hub=author_hub,
        )

        reply_view.additional_properties = d
        return reply_view

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
