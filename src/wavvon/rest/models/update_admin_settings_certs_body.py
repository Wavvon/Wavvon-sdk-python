from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_admin_settings_certs_body_cert_others import (
    UpdateAdminSettingsCertsBodyCertOthers,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trusted_cert_type import TrustedCertType
    from ..models.update_admin_settings_certs_body_cert_issuer_urls import (
        UpdateAdminSettingsCertsBodyCertIssuerUrls,
    )


T = TypeVar("T", bound="UpdateAdminSettingsCertsBody")


@_attrs_define
class UpdateAdminSettingsCertsBody:
    """
    Attributes:
        cert_auto_issue (bool | str | Unset):
        cert_min_age_days (int | str | Unset):
        cert_validity_days (int | str | Unset):
        cert_trusted_issuers (list[str] | Unset):
        cert_trusted_types (list[TrustedCertType] | Unset):
        cert_others (UpdateAdminSettingsCertsBodyCertOthers | Unset):
        cert_replaces_invite (bool | str | Unset):
        cert_issuer_urls (UpdateAdminSettingsCertsBodyCertIssuerUrls | Unset): Replaces the whole map, like the trust
            list it accompanies.
    """

    cert_auto_issue: bool | str | Unset = UNSET
    cert_min_age_days: int | str | Unset = UNSET
    cert_validity_days: int | str | Unset = UNSET
    cert_trusted_issuers: list[str] | Unset = UNSET
    cert_trusted_types: list[TrustedCertType] | Unset = UNSET
    cert_others: UpdateAdminSettingsCertsBodyCertOthers | Unset = UNSET
    cert_replaces_invite: bool | str | Unset = UNSET
    cert_issuer_urls: UpdateAdminSettingsCertsBodyCertIssuerUrls | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_auto_issue: bool | str | Unset
        if isinstance(self.cert_auto_issue, Unset):
            cert_auto_issue = UNSET
        else:
            cert_auto_issue = self.cert_auto_issue

        cert_min_age_days: int | str | Unset
        if isinstance(self.cert_min_age_days, Unset):
            cert_min_age_days = UNSET
        else:
            cert_min_age_days = self.cert_min_age_days

        cert_validity_days: int | str | Unset
        if isinstance(self.cert_validity_days, Unset):
            cert_validity_days = UNSET
        else:
            cert_validity_days = self.cert_validity_days

        cert_trusted_issuers: list[str] | Unset = UNSET
        if not isinstance(self.cert_trusted_issuers, Unset):
            cert_trusted_issuers = self.cert_trusted_issuers

        cert_trusted_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cert_trusted_types, Unset):
            cert_trusted_types = []
            for cert_trusted_types_item_data in self.cert_trusted_types:
                cert_trusted_types_item = cert_trusted_types_item_data.to_dict()
                cert_trusted_types.append(cert_trusted_types_item)

        cert_others: str | Unset = UNSET
        if not isinstance(self.cert_others, Unset):
            cert_others = self.cert_others.value

        cert_replaces_invite: bool | str | Unset
        if isinstance(self.cert_replaces_invite, Unset):
            cert_replaces_invite = UNSET
        else:
            cert_replaces_invite = self.cert_replaces_invite

        cert_issuer_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert_issuer_urls, Unset):
            cert_issuer_urls = self.cert_issuer_urls.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_auto_issue is not UNSET:
            field_dict["cert_auto_issue"] = cert_auto_issue
        if cert_min_age_days is not UNSET:
            field_dict["cert_min_age_days"] = cert_min_age_days
        if cert_validity_days is not UNSET:
            field_dict["cert_validity_days"] = cert_validity_days
        if cert_trusted_issuers is not UNSET:
            field_dict["cert_trusted_issuers"] = cert_trusted_issuers
        if cert_trusted_types is not UNSET:
            field_dict["cert_trusted_types"] = cert_trusted_types
        if cert_others is not UNSET:
            field_dict["cert_others"] = cert_others
        if cert_replaces_invite is not UNSET:
            field_dict["cert_replaces_invite"] = cert_replaces_invite
        if cert_issuer_urls is not UNSET:
            field_dict["cert_issuer_urls"] = cert_issuer_urls

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trusted_cert_type import TrustedCertType
        from ..models.update_admin_settings_certs_body_cert_issuer_urls import (
            UpdateAdminSettingsCertsBodyCertIssuerUrls,
        )

        d = dict(src_dict)

        def _parse_cert_auto_issue(data: object) -> bool | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | str | Unset, data)

        cert_auto_issue = _parse_cert_auto_issue(d.pop("cert_auto_issue", UNSET))

        def _parse_cert_min_age_days(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cert_min_age_days = _parse_cert_min_age_days(d.pop("cert_min_age_days", UNSET))

        def _parse_cert_validity_days(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cert_validity_days = _parse_cert_validity_days(
            d.pop("cert_validity_days", UNSET)
        )

        cert_trusted_issuers = cast(list[str], d.pop("cert_trusted_issuers", UNSET))

        _cert_trusted_types = d.pop("cert_trusted_types", UNSET)
        cert_trusted_types: list[TrustedCertType] | Unset = UNSET
        if _cert_trusted_types is not UNSET:
            cert_trusted_types = []
            for cert_trusted_types_item_data in _cert_trusted_types:
                cert_trusted_types_item = TrustedCertType.from_dict(
                    cert_trusted_types_item_data
                )

                cert_trusted_types.append(cert_trusted_types_item)

        _cert_others = d.pop("cert_others", UNSET)
        cert_others: UpdateAdminSettingsCertsBodyCertOthers | Unset
        if isinstance(_cert_others, Unset):
            cert_others = UNSET
        else:
            cert_others = UpdateAdminSettingsCertsBodyCertOthers(_cert_others)

        def _parse_cert_replaces_invite(data: object) -> bool | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | str | Unset, data)

        cert_replaces_invite = _parse_cert_replaces_invite(
            d.pop("cert_replaces_invite", UNSET)
        )

        _cert_issuer_urls = d.pop("cert_issuer_urls", UNSET)
        cert_issuer_urls: UpdateAdminSettingsCertsBodyCertIssuerUrls | Unset
        if isinstance(_cert_issuer_urls, Unset):
            cert_issuer_urls = UNSET
        else:
            cert_issuer_urls = UpdateAdminSettingsCertsBodyCertIssuerUrls.from_dict(
                _cert_issuer_urls
            )

        update_admin_settings_certs_body = cls(
            cert_auto_issue=cert_auto_issue,
            cert_min_age_days=cert_min_age_days,
            cert_validity_days=cert_validity_days,
            cert_trusted_issuers=cert_trusted_issuers,
            cert_trusted_types=cert_trusted_types,
            cert_others=cert_others,
            cert_replaces_invite=cert_replaces_invite,
            cert_issuer_urls=cert_issuer_urls,
        )

        update_admin_settings_certs_body.additional_properties = d
        return update_admin_settings_certs_body

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
