from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_ref_kind import AttachmentRefKind
from ..models.attachment_ref_state import AttachmentRefState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentRef")


@_attrs_define
class AttachmentRef:
    """One uploaded file on a message, forum post or reply (capability `attachments.stored`). `url` is relative to the hub
    that holds the message; on an alliance read the reader's hub rewrites it to `/alliances/{alliance_id}/uploads/{id}`.
    A tombstone (`removed`, `expired`) keeps `name` and carries no bytes: `mime` is `application/octet-stream` and
    `size` 0.

        Attributes:
            id (str):
            url (str):
            name (str):
            mime (str): From the magic bytes, never from what the client declared.
            kind (AttachmentRefKind): `image` renders inline (a re-encoded WebP or JPEG); `file` is only ever downloaded.
            size (int):
            state (AttachmentRefState): `removed` by a moderator, `expired` by retention, the disk budget or the migration.
            width (int | None | Unset):
            height (int | None | Unset):
    """

    id: str
    url: str
    name: str
    mime: str
    kind: AttachmentRefKind
    size: int
    state: AttachmentRefState
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        name = self.name

        mime = self.mime

        kind = self.kind.value

        size = self.size

        state = self.state.value

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "mime": mime,
                "kind": kind,
                "size": size,
                "state": state,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        mime = d.pop("mime")

        kind = AttachmentRefKind(d.pop("kind"))

        size = d.pop("size")

        state = AttachmentRefState(d.pop("state"))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        attachment_ref = cls(
            id=id,
            url=url,
            name=name,
            mime=mime,
            kind=kind,
            size=size,
            state=state,
            width=width,
            height=height,
        )

        attachment_ref.additional_properties = d
        return attachment_ref

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
