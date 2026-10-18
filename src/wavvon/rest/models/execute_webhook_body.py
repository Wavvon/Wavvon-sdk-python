from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_webhook_body_embeds import ExecuteWebhookBodyEmbeds


T = TypeVar("T", bound="ExecuteWebhookBody")


@_attrs_define
class ExecuteWebhookBody:
    """
    Attributes:
        content (str):
        username (str | Unset): Overrides the webhook's display name
        avatar_url (str | Unset):
        embeds (ExecuteWebhookBodyEmbeds | Unset):
    """

    content: str
    username: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    embeds: ExecuteWebhookBodyEmbeds | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        username = self.username

        avatar_url = self.avatar_url

        embeds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embeds, Unset):
            embeds = self.embeds.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if embeds is not UNSET:
            field_dict["embeds"] = embeds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.execute_webhook_body_embeds import ExecuteWebhookBodyEmbeds

        d = dict(src_dict)
        content = d.pop("content")

        username = d.pop("username", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        _embeds = d.pop("embeds", UNSET)
        embeds: ExecuteWebhookBodyEmbeds | Unset
        if isinstance(_embeds, Unset):
            embeds = UNSET
        else:
            embeds = ExecuteWebhookBodyEmbeds.from_dict(_embeds)

        execute_webhook_body = cls(
            content=content,
            username=username,
            avatar_url=avatar_url,
            embeds=embeds,
        )

        execute_webhook_body.additional_properties = d
        return execute_webhook_body

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
