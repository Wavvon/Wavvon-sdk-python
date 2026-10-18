from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplyView")


@_attrs_define
class ReplyView:
    """
    Attributes:
        id (str | Unset):
        post_id (str | Unset):
        author_pubkey (None | str | Unset):
        body (None | str | Unset): Null on tombstoned replies
        created_at (int | Unset):
        edited_at (int | Unset): Omitted when never edited
        reply_to_id (str | Unset): Omitted on top-level replies
        is_deleted (bool | Unset):
    """

    id: str | Unset = UNSET
    post_id: str | Unset = UNSET
    author_pubkey: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    created_at: int | Unset = UNSET
    edited_at: int | Unset = UNSET
    reply_to_id: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        post_id = self.post_id

        author_pubkey: None | str | Unset
        if isinstance(self.author_pubkey, Unset):
            author_pubkey = UNSET
        else:
            author_pubkey = self.author_pubkey

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        created_at = self.created_at

        edited_at = self.edited_at

        reply_to_id = self.reply_to_id

        is_deleted = self.is_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if author_pubkey is not UNSET:
            field_dict["author_pubkey"] = author_pubkey
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if reply_to_id is not UNSET:
            field_dict["reply_to_id"] = reply_to_id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        post_id = d.pop("post_id", UNSET)

        def _parse_author_pubkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_pubkey = _parse_author_pubkey(d.pop("author_pubkey", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        created_at = d.pop("created_at", UNSET)

        edited_at = d.pop("edited_at", UNSET)

        reply_to_id = d.pop("reply_to_id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        reply_view = cls(
            id=id,
            post_id=post_id,
            author_pubkey=author_pubkey,
            body=body,
            created_at=created_at,
            edited_at=edited_at,
            reply_to_id=reply_to_id,
            is_deleted=is_deleted,
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
