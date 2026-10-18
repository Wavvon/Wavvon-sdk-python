from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_me_app_profile_body_game import SetMeAppProfileBodyGame


T = TypeVar("T", bound="SetMeAppProfileBody")


@_attrs_define
class SetMeAppProfileBody:
    """
    Attributes:
        name (str):
        avatar_url (str | Unset):
        description (str | Unset):
        webhook_url (str | Unset): https only; receives slash invocations
        homepage_url (str | Unset):
        mini_app_url (str | Unset):
        requires_camera (bool | Unset):
        game (SetMeAppProfileBodyGame | Unset):
    """

    name: str
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    homepage_url: str | Unset = UNSET
    mini_app_url: str | Unset = UNSET
    requires_camera: bool | Unset = UNSET
    game: SetMeAppProfileBodyGame | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        avatar_url = self.avatar_url

        description = self.description

        webhook_url = self.webhook_url

        homepage_url = self.homepage_url

        mini_app_url = self.mini_app_url

        requires_camera = self.requires_camera

        game: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game, Unset):
            game = self.game.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url
        if mini_app_url is not UNSET:
            field_dict["mini_app_url"] = mini_app_url
        if requires_camera is not UNSET:
            field_dict["requires_camera"] = requires_camera
        if game is not UNSET:
            field_dict["game"] = game

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_me_app_profile_body_game import SetMeAppProfileBodyGame

        d = dict(src_dict)
        name = d.pop("name")

        avatar_url = d.pop("avatar_url", UNSET)

        description = d.pop("description", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        homepage_url = d.pop("homepage_url", UNSET)

        mini_app_url = d.pop("mini_app_url", UNSET)

        requires_camera = d.pop("requires_camera", UNSET)

        _game = d.pop("game", UNSET)
        game: SetMeAppProfileBodyGame | Unset
        if isinstance(_game, Unset):
            game = UNSET
        else:
            game = SetMeAppProfileBodyGame.from_dict(_game)

        set_me_app_profile_body = cls(
            name=name,
            avatar_url=avatar_url,
            description=description,
            webhook_url=webhook_url,
            homepage_url=homepage_url,
            mini_app_url=mini_app_url,
            requires_camera=requires_camera,
            game=game,
        )

        set_me_app_profile_body.additional_properties = d
        return set_me_app_profile_body

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
