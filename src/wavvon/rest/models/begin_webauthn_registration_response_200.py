from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.begin_webauthn_registration_response_200_options import (
        BeginWebauthnRegistrationResponse200Options,
    )


T = TypeVar("T", bound="BeginWebauthnRegistrationResponse200")


@_attrs_define
class BeginWebauthnRegistrationResponse200:
    """
    Attributes:
        session_id (str | Unset):
        options (BeginWebauthnRegistrationResponse200Options | Unset): PublicKeyCredentialCreationOptions
    """

    session_id: str | Unset = UNSET
    options: BeginWebauthnRegistrationResponse200Options | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.begin_webauthn_registration_response_200_options import (
            BeginWebauthnRegistrationResponse200Options,
        )

        d = dict(src_dict)
        session_id = d.pop("session_id", UNSET)

        _options = d.pop("options", UNSET)
        options: BeginWebauthnRegistrationResponse200Options | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BeginWebauthnRegistrationResponse200Options.from_dict(_options)

        begin_webauthn_registration_response_200 = cls(
            session_id=session_id,
            options=options,
        )

        begin_webauthn_registration_response_200.additional_properties = d
        return begin_webauthn_registration_response_200

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
