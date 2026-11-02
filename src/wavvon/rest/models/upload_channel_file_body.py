from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UploadChannelFileBody")


@_attrs_define
class UploadChannelFileBody:
    """
    Attributes:
        file (File | Unset):
        as_file (bool | Unset): Keep the original image bytes; download only.
    """

    file: File | Unset = UNSET
    as_file: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        as_file = self.as_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if as_file is not UNSET:
            field_dict["as_file"] = as_file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.as_file, Unset):
            files.append(("as_file", (None, str(self.as_file).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        as_file = d.pop("as_file", UNSET)

        upload_channel_file_body = cls(
            file=file,
            as_file=as_file,
        )

        upload_channel_file_body.additional_properties = d
        return upload_channel_file_body

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
