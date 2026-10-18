from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadChannelFileResponse201")


@_attrs_define
class UploadChannelFileResponse201:
    """
    Attributes:
        id (str | Unset):
        url (str | Unset): Path under /uploads/
        filename (str | Unset):
        size_bytes (int | Unset):
        mime_type (str | Unset):
    """

    id: str | Unset = UNSET
    url: str | Unset = UNSET
    filename: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        filename = self.filename

        size_bytes = self.size_bytes

        mime_type = self.mime_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        filename = d.pop("filename", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        upload_channel_file_response_201 = cls(
            id=id,
            url=url,
            filename=filename,
            size_bytes=size_bytes,
            mime_type=mime_type,
        )

        upload_channel_file_response_201.additional_properties = d
        return upload_channel_file_response_201

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
