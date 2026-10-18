from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.me_info_approval_status import MeInfoApprovalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="MeInfo")


@_attrs_define
class MeInfo:
    """
    Attributes:
        public_key (str | Unset):
        display_name (None | str | Unset):
        avatar (None | str | Unset):
        findable_by_allies (bool | Unset):
        approval_status (MeInfoApprovalStatus | Unset):
        roles (list[Role] | Unset):
    """

    public_key: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    findable_by_allies: bool | Unset = UNSET
    approval_status: MeInfoApprovalStatus | Unset = UNSET
    roles: list[Role] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        findable_by_allies = self.findable_by_allies

        approval_status: str | Unset = UNSET
        if not isinstance(self.approval_status, Unset):
            approval_status = self.approval_status.value

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if findable_by_allies is not UNSET:
            field_dict["findable_by_allies"] = findable_by_allies
        if approval_status is not UNSET:
            field_dict["approval_status"] = approval_status
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.role import Role

        d = dict(src_dict)
        public_key = d.pop("public_key", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        findable_by_allies = d.pop("findable_by_allies", UNSET)

        _approval_status = d.pop("approval_status", UNSET)
        approval_status: MeInfoApprovalStatus | Unset
        if isinstance(_approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = MeInfoApprovalStatus(_approval_status)

        _roles = d.pop("roles", UNSET)
        roles: list[Role] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = Role.from_dict(roles_item_data)

                roles.append(roles_item)

        me_info = cls(
            public_key=public_key,
            display_name=display_name,
            avatar=avatar,
            findable_by_allies=findable_by_allies,
            approval_status=approval_status,
            roles=roles,
        )

        me_info.additional_properties = d
        return me_info

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
