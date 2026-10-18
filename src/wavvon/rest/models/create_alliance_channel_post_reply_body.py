from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAllianceChannelPostReplyBody")


@_attrs_define
class CreateAllianceChannelPostReplyBody:
    """
    Attributes:
        body (str):
        reply_to_id (str | Unset): For threaded replies
    """

    body: str
    reply_to_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        reply_to_id = self.reply_to_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if reply_to_id is not UNSET:
            field_dict["reply_to_id"] = reply_to_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body = d.pop("body")

        reply_to_id = d.pop("reply_to_id", UNSET)

        create_alliance_channel_post_reply_body = cls(
            body=body,
            reply_to_id=reply_to_id,
        )

        create_alliance_channel_post_reply_body.additional_properties = d
        return create_alliance_channel_post_reply_body

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
