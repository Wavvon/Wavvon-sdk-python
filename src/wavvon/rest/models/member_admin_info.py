from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="MemberAdminInfo")


@_attrs_define
class MemberAdminInfo:
    """A member as listed for administrators by `GET /hub/members`.

    Attributes:
        public_key (str):
        display_name (None | str):
        online (bool):
        first_seen_at (int):
        last_seen_at (int):
        roles (list[Role]):
        birthday (None | str):
    """

    public_key: str
    display_name: None | str
    online: bool
    first_seen_at: int
    last_seen_at: int
    roles: list[Role]
    birthday: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        display_name: None | str
        display_name = self.display_name

        online = self.online

        first_seen_at = self.first_seen_at

        last_seen_at = self.last_seen_at

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        birthday: None | str
        birthday = self.birthday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "display_name": display_name,
                "online": online,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
                "roles": roles,
                "birthday": birthday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.role import Role

        d = dict(src_dict)
        public_key = d.pop("public_key")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        online = d.pop("online")

        first_seen_at = d.pop("first_seen_at")

        last_seen_at = d.pop("last_seen_at")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

        def _parse_birthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthday = _parse_birthday(d.pop("birthday"))

        member_admin_info = cls(
            public_key=public_key,
            display_name=display_name,
            online=online,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            roles=roles,
            birthday=birthday,
        )

        member_admin_info.additional_properties = d
        return member_admin_info

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
