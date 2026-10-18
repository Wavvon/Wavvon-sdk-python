from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_admin_settings_certs_body_cert_mode import (
    UpdateAdminSettingsCertsBodyCertMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_admin_settings_certs_body_cert_issuer_urls import (
        UpdateAdminSettingsCertsBodyCertIssuerUrls,
    )
    from ..models.update_admin_settings_certs_body_cert_require import (
        UpdateAdminSettingsCertsBodyCertRequire,
    )


T = TypeVar("T", bound="UpdateAdminSettingsCertsBody")


@_attrs_define
class UpdateAdminSettingsCertsBody:
    """
    Attributes:
        cert_auto_issue (bool | str | Unset):
        cert_standing_days (int | str | Unset):
        cert_min_age_days (int | str | Unset):
        cert_validity_days (int | str | Unset):
        cert_mode (UpdateAdminSettingsCertsBodyCertMode | Unset):
        cert_trusted_issuers (list[str] | Unset):
        cert_require (UpdateAdminSettingsCertsBodyCertRequire | Unset):
        cert_min_pow_level (int | str | Unset):
        cert_issuer_urls (UpdateAdminSettingsCertsBodyCertIssuerUrls | Unset): Replaces the whole map, like the trust
            list it accompanies.
    """

    cert_auto_issue: bool | str | Unset = UNSET
    cert_standing_days: int | str | Unset = UNSET
    cert_min_age_days: int | str | Unset = UNSET
    cert_validity_days: int | str | Unset = UNSET
    cert_mode: UpdateAdminSettingsCertsBodyCertMode | Unset = UNSET
    cert_trusted_issuers: list[str] | Unset = UNSET
    cert_require: UpdateAdminSettingsCertsBodyCertRequire | Unset = UNSET
    cert_min_pow_level: int | str | Unset = UNSET
    cert_issuer_urls: UpdateAdminSettingsCertsBodyCertIssuerUrls | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_auto_issue: bool | str | Unset
        if isinstance(self.cert_auto_issue, Unset):
            cert_auto_issue = UNSET
        else:
            cert_auto_issue = self.cert_auto_issue

        cert_standing_days: int | str | Unset
        if isinstance(self.cert_standing_days, Unset):
            cert_standing_days = UNSET
        else:
            cert_standing_days = self.cert_standing_days

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

        cert_mode: str | Unset = UNSET
        if not isinstance(self.cert_mode, Unset):
            cert_mode = self.cert_mode.value

        cert_trusted_issuers: list[str] | Unset = UNSET
        if not isinstance(self.cert_trusted_issuers, Unset):
            cert_trusted_issuers = self.cert_trusted_issuers

        cert_require: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert_require, Unset):
            cert_require = self.cert_require.to_dict()

        cert_min_pow_level: int | str | Unset
        if isinstance(self.cert_min_pow_level, Unset):
            cert_min_pow_level = UNSET
        else:
            cert_min_pow_level = self.cert_min_pow_level

        cert_issuer_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert_issuer_urls, Unset):
            cert_issuer_urls = self.cert_issuer_urls.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_auto_issue is not UNSET:
            field_dict["cert_auto_issue"] = cert_auto_issue
        if cert_standing_days is not UNSET:
            field_dict["cert_standing_days"] = cert_standing_days
        if cert_min_age_days is not UNSET:
            field_dict["cert_min_age_days"] = cert_min_age_days
        if cert_validity_days is not UNSET:
            field_dict["cert_validity_days"] = cert_validity_days
        if cert_mode is not UNSET:
            field_dict["cert_mode"] = cert_mode
        if cert_trusted_issuers is not UNSET:
            field_dict["cert_trusted_issuers"] = cert_trusted_issuers
        if cert_require is not UNSET:
            field_dict["cert_require"] = cert_require
        if cert_min_pow_level is not UNSET:
            field_dict["cert_min_pow_level"] = cert_min_pow_level
        if cert_issuer_urls is not UNSET:
            field_dict["cert_issuer_urls"] = cert_issuer_urls

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_admin_settings_certs_body_cert_issuer_urls import (
            UpdateAdminSettingsCertsBodyCertIssuerUrls,
        )
        from ..models.update_admin_settings_certs_body_cert_require import (
            UpdateAdminSettingsCertsBodyCertRequire,
        )

        d = dict(src_dict)

        def _parse_cert_auto_issue(data: object) -> bool | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | str | Unset, data)

        cert_auto_issue = _parse_cert_auto_issue(d.pop("cert_auto_issue", UNSET))

        def _parse_cert_standing_days(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cert_standing_days = _parse_cert_standing_days(
            d.pop("cert_standing_days", UNSET)
        )

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

        _cert_mode = d.pop("cert_mode", UNSET)
        cert_mode: UpdateAdminSettingsCertsBodyCertMode | Unset
        if isinstance(_cert_mode, Unset):
            cert_mode = UNSET
        else:
            cert_mode = UpdateAdminSettingsCertsBodyCertMode(_cert_mode)

        cert_trusted_issuers = cast(list[str], d.pop("cert_trusted_issuers", UNSET))

        _cert_require = d.pop("cert_require", UNSET)
        cert_require: UpdateAdminSettingsCertsBodyCertRequire | Unset
        if isinstance(_cert_require, Unset):
            cert_require = UNSET
        else:
            cert_require = UpdateAdminSettingsCertsBodyCertRequire.from_dict(
                _cert_require
            )

        def _parse_cert_min_pow_level(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cert_min_pow_level = _parse_cert_min_pow_level(
            d.pop("cert_min_pow_level", UNSET)
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
            cert_standing_days=cert_standing_days,
            cert_min_age_days=cert_min_age_days,
            cert_validity_days=cert_validity_days,
            cert_mode=cert_mode,
            cert_trusted_issuers=cert_trusted_issuers,
            cert_require=cert_require,
            cert_min_pow_level=cert_min_pow_level,
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
