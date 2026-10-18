from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hub_info_challenge_mode import HubInfoChallengeMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="HubInfo")


@_attrs_define
class HubInfo:
    """Only the fields clients branch on are listed; `/info` carries more
    (badges, LAN trust material, welcome banner, voice endpoint…) and is
    additive by rule, so ignore what you do not recognise.

        Attributes:
            name (str | Unset):
            icon (None | str | Unset):
            public_key (str | Unset): The hub's Ed25519 identity, hex. This is the hub's ID.
            version (str | Unset): For display and "this hub is very old" warnings **only**. Never
                decide whether a feature exists by comparing this — use
                `capabilities`.
            capabilities (list[str] | Unset): What this hub can do, e.g. `voice.wt`, `list.cursor`. Test
                membership to decide what to offer; absent or empty means a hub
                predating capability advertising, which reads correctly as "knows
                nothing". The list only ever grows — a string never changes
                spelling or meaning once published.
                 Example: ['list.cursor', 'pairing.subkey', 'recovery.attestation', 'screenshare.v2', 'voice.wt'].
            canonical_url (str | Unset): The address this hub says clients should use for it. Behind a farm
                this is the hub's owner-chosen name (`https://farm.example/hub/
                MangiaDaPippo`) and it **changes** when the hub is renamed —
                re-read it whenever you refresh `/info` and update the address you
                have stored.

                Following it is safe because a hub is identified by `public_key`,
                never by its address: you change *where* you look, not who you
                believe you are talking to. Absent when the hub has no public
                address.
            invite_only (bool | Unset):
            min_security_level (int | Unset):
            min_pow_level (int | Unset):
            challenge_mode (HubInfoChallengeMode | Unset):
            farm_url (None | str | Unset): When set, send `/auth/*` here instead of to the hub.
    """

    name: str | Unset = UNSET
    icon: None | str | Unset = UNSET
    public_key: str | Unset = UNSET
    version: str | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    canonical_url: str | Unset = UNSET
    invite_only: bool | Unset = UNSET
    min_security_level: int | Unset = UNSET
    min_pow_level: int | Unset = UNSET
    challenge_mode: HubInfoChallengeMode | Unset = UNSET
    farm_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        public_key = self.public_key

        version = self.version

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        canonical_url = self.canonical_url

        invite_only = self.invite_only

        min_security_level = self.min_security_level

        min_pow_level = self.min_pow_level

        challenge_mode: str | Unset = UNSET
        if not isinstance(self.challenge_mode, Unset):
            challenge_mode = self.challenge_mode.value

        farm_url: None | str | Unset
        if isinstance(self.farm_url, Unset):
            farm_url = UNSET
        else:
            farm_url = self.farm_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if version is not UNSET:
            field_dict["version"] = version
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if canonical_url is not UNSET:
            field_dict["canonical_url"] = canonical_url
        if invite_only is not UNSET:
            field_dict["invite_only"] = invite_only
        if min_security_level is not UNSET:
            field_dict["min_security_level"] = min_security_level
        if min_pow_level is not UNSET:
            field_dict["min_pow_level"] = min_pow_level
        if challenge_mode is not UNSET:
            field_dict["challenge_mode"] = challenge_mode
        if farm_url is not UNSET:
            field_dict["farm_url"] = farm_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        public_key = d.pop("public_key", UNSET)

        version = d.pop("version", UNSET)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        canonical_url = d.pop("canonical_url", UNSET)

        invite_only = d.pop("invite_only", UNSET)

        min_security_level = d.pop("min_security_level", UNSET)

        min_pow_level = d.pop("min_pow_level", UNSET)

        _challenge_mode = d.pop("challenge_mode", UNSET)
        challenge_mode: HubInfoChallengeMode | Unset
        if isinstance(_challenge_mode, Unset):
            challenge_mode = UNSET
        else:
            challenge_mode = HubInfoChallengeMode(_challenge_mode)

        def _parse_farm_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farm_url = _parse_farm_url(d.pop("farm_url", UNSET))

        hub_info = cls(
            name=name,
            icon=icon,
            public_key=public_key,
            version=version,
            capabilities=capabilities,
            canonical_url=canonical_url,
            invite_only=invite_only,
            min_security_level=min_security_level,
            min_pow_level=min_pow_level,
            challenge_mode=challenge_mode,
            farm_url=farm_url,
        )

        hub_info.additional_properties = d
        return hub_info

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
