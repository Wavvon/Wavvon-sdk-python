from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_auth_challenge_response_200_scheme import (
    CreateAuthChallengeResponse200Scheme,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAuthChallengeResponse200")


@_attrs_define
class CreateAuthChallengeResponse200:
    """
    Attributes:
        challenge (str): 32 random bytes, lowercase hex (64 chars)
        scheme (CreateAuthChallengeResponse200Scheme | Unset): Present when the answer may be signed over "wavvon/auth-
            challenge/v1\\0" || hex-decoded challenge (wire-format.md). Omitted by older hubs, which take a signature over
            the raw decoded bytes only. A hub that sends it still accepts the raw form.
    """

    challenge: str
    scheme: CreateAuthChallengeResponse200Scheme | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        scheme: str | Unset = UNSET
        if not isinstance(self.scheme, Unset):
            scheme = self.scheme.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
            }
        )
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        challenge = d.pop("challenge")

        _scheme = d.pop("scheme", UNSET)
        scheme: CreateAuthChallengeResponse200Scheme | Unset
        if isinstance(_scheme, Unset):
            scheme = UNSET
        else:
            scheme = CreateAuthChallengeResponse200Scheme(_scheme)

        create_auth_challenge_response_200 = cls(
            challenge=challenge,
            scheme=scheme,
        )

        create_auth_challenge_response_200.additional_properties = d
        return create_auth_challenge_response_200

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
