from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hub_info_challenge_mode import HubInfoChallengeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hub_info_badges_item import HubInfoBadgesItem
    from ..models.hub_info_cert_requirement import HubInfoCertRequirement
    from ..models.hub_info_rotation import HubInfoRotation


T = TypeVar("T", bound="HubInfo")


@_attrs_define
class HubInfo:
    """`GET /info`. Additive by rule: ignore fields you do not recognise.

    Attributes:
        name (str):
        description (None | str):
        icon (None | str):
        public_key (str): The hub's Ed25519 identity, hex. This is the hub's ID.
        version (str): For display and "this hub is very old" warnings **only**. Never
            decide whether a feature exists by comparing this — use
            `capabilities`.
        capabilities (list[str]): What this hub can do, e.g. `voice.wt`, `list.cursor`. Test
            membership to decide what to offer; absent or empty means a hub
            predating capability advertising, which reads correctly as "knows
            nothing". The list only ever grows — a string never changes
            spelling or meaning once published.
             Example: ['list.cursor', 'pairing.subkey', 'recovery.attestation', 'screenshare.v2', 'voice.wt'].
        invite_only (bool):
        min_security_level (int):
        min_pow_level (int):
        challenge_mode (HubInfoChallengeMode):
        self_tags (list[str]):
        nsfw (bool):
        badges (list[HubInfoBadgesItem]): Badges other hubs issued to this hub.
        emoji_count (int):
        lan_mode (bool):
        birthdays_enabled (bool):
        max_attachment_bytes (int):
        canonical_url (str | Unset): The address this hub says clients should use for it. Behind a farm
            this is the hub's owner-chosen name (`https://farm.example/hub/
            MangiaDaPippo`) and it **changes** when the hub is renamed —
            re-read it whenever you refresh `/info` and update the address you
            have stored.

            Following it is safe because a hub is identified by `public_key`,
            never by its address: you change *where* you look, not who you
            believe you are talking to. Absent when the hub has no public
            address.
        farm_url (str | Unset): When present, send `/auth/*` here instead of to the hub. Omitted unless set.
        cert_requirement (HubInfoCertRequirement | Unset): What a certificate must show to admit a member. Omitted
            unless set.
        sfu_url (str | Unset): Omitted unless the hub runs an SFU.
        rotation (HubInfoRotation | Unset): Hub key rotation payload during the transition window after a rotate-key
            ceremony (see `GET /key-rotation`). Omitted when no rotation is in progress.
        lan_tls (str | Unset): Omitted unless set.
        lan_fingerprint (str | Unset): Omitted unless set.
        welcome_label (str | Unset): Omitted unless set.
        welcome_invite_url (str | Unset): Omitted unless set.
        farewell_label (str | Unset): Omitted unless set.
        voice_wt_url (str | Unset): WebTransport voice endpoint. Omitted unless set.
        voice_cert_hash (str | Unset): Omitted unless set.
        timezone (str | Unset): Omitted unless set.
    """

    name: str
    description: None | str
    icon: None | str
    public_key: str
    version: str
    capabilities: list[str]
    invite_only: bool
    min_security_level: int
    min_pow_level: int
    challenge_mode: HubInfoChallengeMode
    self_tags: list[str]
    nsfw: bool
    badges: list[HubInfoBadgesItem]
    emoji_count: int
    lan_mode: bool
    birthdays_enabled: bool
    max_attachment_bytes: int
    canonical_url: str | Unset = UNSET
    farm_url: str | Unset = UNSET
    cert_requirement: HubInfoCertRequirement | Unset = UNSET
    sfu_url: str | Unset = UNSET
    rotation: HubInfoRotation | Unset = UNSET
    lan_tls: str | Unset = UNSET
    lan_fingerprint: str | Unset = UNSET
    welcome_label: str | Unset = UNSET
    welcome_invite_url: str | Unset = UNSET
    farewell_label: str | Unset = UNSET
    voice_wt_url: str | Unset = UNSET
    voice_cert_hash: str | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str
        description = self.description

        icon: None | str
        icon = self.icon

        public_key = self.public_key

        version = self.version

        capabilities = self.capabilities

        invite_only = self.invite_only

        min_security_level = self.min_security_level

        min_pow_level = self.min_pow_level

        challenge_mode = self.challenge_mode.value

        self_tags = self.self_tags

        nsfw = self.nsfw

        badges = []
        for badges_item_data in self.badges:
            badges_item = badges_item_data.to_dict()
            badges.append(badges_item)

        emoji_count = self.emoji_count

        lan_mode = self.lan_mode

        birthdays_enabled = self.birthdays_enabled

        max_attachment_bytes = self.max_attachment_bytes

        canonical_url = self.canonical_url

        farm_url = self.farm_url

        cert_requirement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert_requirement, Unset):
            cert_requirement = self.cert_requirement.to_dict()

        sfu_url = self.sfu_url

        rotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rotation, Unset):
            rotation = self.rotation.to_dict()

        lan_tls = self.lan_tls

        lan_fingerprint = self.lan_fingerprint

        welcome_label = self.welcome_label

        welcome_invite_url = self.welcome_invite_url

        farewell_label = self.farewell_label

        voice_wt_url = self.voice_wt_url

        voice_cert_hash = self.voice_cert_hash

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "icon": icon,
                "public_key": public_key,
                "version": version,
                "capabilities": capabilities,
                "invite_only": invite_only,
                "min_security_level": min_security_level,
                "min_pow_level": min_pow_level,
                "challenge_mode": challenge_mode,
                "self_tags": self_tags,
                "nsfw": nsfw,
                "badges": badges,
                "emoji_count": emoji_count,
                "lan_mode": lan_mode,
                "birthdays_enabled": birthdays_enabled,
                "max_attachment_bytes": max_attachment_bytes,
            }
        )
        if canonical_url is not UNSET:
            field_dict["canonical_url"] = canonical_url
        if farm_url is not UNSET:
            field_dict["farm_url"] = farm_url
        if cert_requirement is not UNSET:
            field_dict["cert_requirement"] = cert_requirement
        if sfu_url is not UNSET:
            field_dict["sfu_url"] = sfu_url
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if lan_tls is not UNSET:
            field_dict["lan_tls"] = lan_tls
        if lan_fingerprint is not UNSET:
            field_dict["lan_fingerprint"] = lan_fingerprint
        if welcome_label is not UNSET:
            field_dict["welcome_label"] = welcome_label
        if welcome_invite_url is not UNSET:
            field_dict["welcome_invite_url"] = welcome_invite_url
        if farewell_label is not UNSET:
            field_dict["farewell_label"] = farewell_label
        if voice_wt_url is not UNSET:
            field_dict["voice_wt_url"] = voice_wt_url
        if voice_cert_hash is not UNSET:
            field_dict["voice_cert_hash"] = voice_cert_hash
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hub_info_badges_item import HubInfoBadgesItem
        from ..models.hub_info_cert_requirement import HubInfoCertRequirement
        from ..models.hub_info_rotation import HubInfoRotation

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_icon(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon = _parse_icon(d.pop("icon"))

        public_key = d.pop("public_key")

        version = d.pop("version")

        capabilities = cast(list[str], d.pop("capabilities"))

        invite_only = d.pop("invite_only")

        min_security_level = d.pop("min_security_level")

        min_pow_level = d.pop("min_pow_level")

        challenge_mode = HubInfoChallengeMode(d.pop("challenge_mode"))

        self_tags = cast(list[str], d.pop("self_tags"))

        nsfw = d.pop("nsfw")

        badges = []
        _badges = d.pop("badges")
        for badges_item_data in _badges:
            badges_item = HubInfoBadgesItem.from_dict(badges_item_data)

            badges.append(badges_item)

        emoji_count = d.pop("emoji_count")

        lan_mode = d.pop("lan_mode")

        birthdays_enabled = d.pop("birthdays_enabled")

        max_attachment_bytes = d.pop("max_attachment_bytes")

        canonical_url = d.pop("canonical_url", UNSET)

        farm_url = d.pop("farm_url", UNSET)

        _cert_requirement = d.pop("cert_requirement", UNSET)
        cert_requirement: HubInfoCertRequirement | Unset
        if isinstance(_cert_requirement, Unset):
            cert_requirement = UNSET
        else:
            cert_requirement = HubInfoCertRequirement.from_dict(_cert_requirement)

        sfu_url = d.pop("sfu_url", UNSET)

        _rotation = d.pop("rotation", UNSET)
        rotation: HubInfoRotation | Unset
        if isinstance(_rotation, Unset):
            rotation = UNSET
        else:
            rotation = HubInfoRotation.from_dict(_rotation)

        lan_tls = d.pop("lan_tls", UNSET)

        lan_fingerprint = d.pop("lan_fingerprint", UNSET)

        welcome_label = d.pop("welcome_label", UNSET)

        welcome_invite_url = d.pop("welcome_invite_url", UNSET)

        farewell_label = d.pop("farewell_label", UNSET)

        voice_wt_url = d.pop("voice_wt_url", UNSET)

        voice_cert_hash = d.pop("voice_cert_hash", UNSET)

        timezone = d.pop("timezone", UNSET)

        hub_info = cls(
            name=name,
            description=description,
            icon=icon,
            public_key=public_key,
            version=version,
            capabilities=capabilities,
            invite_only=invite_only,
            min_security_level=min_security_level,
            min_pow_level=min_pow_level,
            challenge_mode=challenge_mode,
            self_tags=self_tags,
            nsfw=nsfw,
            badges=badges,
            emoji_count=emoji_count,
            lan_mode=lan_mode,
            birthdays_enabled=birthdays_enabled,
            max_attachment_bytes=max_attachment_bytes,
            canonical_url=canonical_url,
            farm_url=farm_url,
            cert_requirement=cert_requirement,
            sfu_url=sfu_url,
            rotation=rotation,
            lan_tls=lan_tls,
            lan_fingerprint=lan_fingerprint,
            welcome_label=welcome_label,
            welcome_invite_url=welcome_invite_url,
            farewell_label=farewell_label,
            voice_wt_url=voice_wt_url,
            voice_cert_hash=voice_cert_hash,
            timezone=timezone,
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
