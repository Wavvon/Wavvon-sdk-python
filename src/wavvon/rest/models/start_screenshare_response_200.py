from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartScreenshareResponse200")


@_attrs_define
class StartScreenshareResponse200:
    """
    Attributes:
        stream_id (str | Unset):
        channel_id (str | Unset):
    """

    stream_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stream_id = self.stream_id

        channel_id = self.channel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stream_id is not UNSET:
            field_dict["stream_id"] = stream_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stream_id = d.pop("stream_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        start_screenshare_response_200 = cls(
            stream_id=stream_id,
            channel_id=channel_id,
        )

        start_screenshare_response_200.additional_properties = d
        return start_screenshare_response_200

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
