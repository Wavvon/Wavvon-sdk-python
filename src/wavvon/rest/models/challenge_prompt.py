from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.challenge_prompt_mode import ChallengePromptMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengePrompt")


@_attrs_define
class ChallengePrompt:
    """
    Attributes:
        id (str | Unset):
        mode (ChallengePromptMode | Unset):
        prompt_svg (None | str | Unset): SVG puzzle image, present when mode includes puzzle
        expires_at (int | Unset):
    """

    id: str | Unset = UNSET
    mode: ChallengePromptMode | Unset = UNSET
    prompt_svg: None | str | Unset = UNSET
    expires_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        prompt_svg: None | str | Unset
        if isinstance(self.prompt_svg, Unset):
            prompt_svg = UNSET
        else:
            prompt_svg = self.prompt_svg

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if prompt_svg is not UNSET:
            field_dict["prompt_svg"] = prompt_svg
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ChallengePromptMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ChallengePromptMode(_mode)

        def _parse_prompt_svg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_svg = _parse_prompt_svg(d.pop("prompt_svg", UNSET))

        expires_at = d.pop("expires_at", UNSET)

        challenge_prompt = cls(
            id=id,
            mode=mode,
            prompt_svg=prompt_svg,
            expires_at=expires_at,
        )

        challenge_prompt.additional_properties = d
        return challenge_prompt

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
