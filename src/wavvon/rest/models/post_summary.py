from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSummary")


@_attrs_define
class PostSummary:
    """
    Attributes:
        id (str | Unset):
        channel_id (str | Unset):
        author_pubkey (None | str | Unset): Null on tombstoned posts for non-moderators
        title (None | str | Unset):
        created_at (int | Unset):
        edited_at (int | Unset): Omitted when never edited
        is_pinned (bool | Unset):
        is_locked (bool | Unset):
        reply_count (int | Unset):
        last_activity_at (int | Unset):
        is_deleted (bool | Unset):
        unread_reply_count (int | Unset): Replies after the viewer's read cursor. Omitted when unauthenticated.
    """

    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    author_pubkey: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    edited_at: int | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    is_locked: bool | Unset = UNSET
    reply_count: int | Unset = UNSET
    last_activity_at: int | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    unread_reply_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        author_pubkey: None | str | Unset
        if isinstance(self.author_pubkey, Unset):
            author_pubkey = UNSET
        else:
            author_pubkey = self.author_pubkey

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        created_at = self.created_at

        edited_at = self.edited_at

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        reply_count = self.reply_count

        last_activity_at = self.last_activity_at

        is_deleted = self.is_deleted

        unread_reply_count = self.unread_reply_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if author_pubkey is not UNSET:
            field_dict["author_pubkey"] = author_pubkey
        if title is not UNSET:
            field_dict["title"] = title
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if reply_count is not UNSET:
            field_dict["reply_count"] = reply_count
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if unread_reply_count is not UNSET:
            field_dict["unread_reply_count"] = unread_reply_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        def _parse_author_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_pubkey = _parse_author_pubkey(d.pop("author_pubkey", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        created_at = d.pop("created_at", UNSET)

        edited_at = d.pop("edited_at", UNSET)

        is_pinned = d.pop("is_pinned", UNSET)

        is_locked = d.pop("is_locked", UNSET)

        reply_count = d.pop("reply_count", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        unread_reply_count = d.pop("unread_reply_count", UNSET)

        post_summary = cls(
            id=id,
            channel_id=channel_id,
            author_pubkey=author_pubkey,
            title=title,
            created_at=created_at,
            edited_at=edited_at,
            is_pinned=is_pinned,
            is_locked=is_locked,
            reply_count=reply_count,
            last_activity_at=last_activity_at,
            is_deleted=is_deleted,
            unread_reply_count=unread_reply_count,
        )

        post_summary.additional_properties = d
        return post_summary

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
