from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_admin_settings_certs_response_200_cert_mode import (
    ListAdminSettingsCertsResponse200CertMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_admin_settings_certs_response_200_cert_issuer_urls import (
        ListAdminSettingsCertsResponse200CertIssuerUrls,
    )


T = TypeVar("T", bound="ListAdminSettingsCertsResponse200")


@_attrs_define
class ListAdminSettingsCertsResponse200:
    """
    Attributes:
        cert_mode (ListAdminSettingsCertsResponse200CertMode | Unset):
        cert_auto_issue (bool | Unset):
        cert_min_age_days (int | Unset):
        cert_validity_days (int | Unset):
        cert_trusted_issuers (list[str] | Unset):
        cert_issuer_urls (ListAdminSettingsCertsResponse200CertIssuerUrls | Unset): Issuer pubkey to base URL, for the
            issuers this hub can pull a portfolio from during admission. Sparse: trust does not require an address, and an
            issuer without one still has its pushed certs honoured.
    """

    cert_mode: ListAdminSettingsCertsResponse200CertMode | Unset = UNSET
    cert_auto_issue: bool | Unset = UNSET
    cert_min_age_days: int | Unset = UNSET
    cert_validity_days: int | Unset = UNSET
    cert_trusted_issuers: list[str] | Unset = UNSET
    cert_issuer_urls: ListAdminSettingsCertsResponse200CertIssuerUrls | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_mode: str | Unset = UNSET
        if not isinstance(self.cert_mode, Unset):
            cert_mode = self.cert_mode.value

        cert_auto_issue = self.cert_auto_issue

        cert_min_age_days = self.cert_min_age_days

        cert_validity_days = self.cert_validity_days

        cert_trusted_issuers: list[str] | Unset = UNSET
        if not isinstance(self.cert_trusted_issuers, Unset):
            cert_trusted_issuers = self.cert_trusted_issuers

        cert_issuer_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert_issuer_urls, Unset):
            cert_issuer_urls = self.cert_issuer_urls.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_mode is not UNSET:
            field_dict["cert_mode"] = cert_mode
        if cert_auto_issue is not UNSET:
            field_dict["cert_auto_issue"] = cert_auto_issue
        if cert_min_age_days is not UNSET:
            field_dict["cert_min_age_days"] = cert_min_age_days
        if cert_validity_days is not UNSET:
            field_dict["cert_validity_days"] = cert_validity_days
        if cert_trusted_issuers is not UNSET:
            field_dict["cert_trusted_issuers"] = cert_trusted_issuers
        if cert_issuer_urls is not UNSET:
            field_dict["cert_issuer_urls"] = cert_issuer_urls

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_admin_settings_certs_response_200_cert_issuer_urls import (
            ListAdminSettingsCertsResponse200CertIssuerUrls,
        )

        d = dict(src_dict)
        _cert_mode = d.pop("cert_mode", UNSET)
        cert_mode: ListAdminSettingsCertsResponse200CertMode | Unset
        if isinstance(_cert_mode, Unset):
            cert_mode = UNSET
        else:
            cert_mode = ListAdminSettingsCertsResponse200CertMode(_cert_mode)

        cert_auto_issue = d.pop("cert_auto_issue", UNSET)

        cert_min_age_days = d.pop("cert_min_age_days", UNSET)

        cert_validity_days = d.pop("cert_validity_days", UNSET)

        cert_trusted_issuers = cast(list[str], d.pop("cert_trusted_issuers", UNSET))

        _cert_issuer_urls = d.pop("cert_issuer_urls", UNSET)
        cert_issuer_urls: ListAdminSettingsCertsResponse200CertIssuerUrls | Unset
        if isinstance(_cert_issuer_urls, Unset):
            cert_issuer_urls = UNSET
        else:
            cert_issuer_urls = (
                ListAdminSettingsCertsResponse200CertIssuerUrls.from_dict(
                    _cert_issuer_urls
                )
            )

        list_admin_settings_certs_response_200 = cls(
            cert_mode=cert_mode,
            cert_auto_issue=cert_auto_issue,
            cert_min_age_days=cert_min_age_days,
            cert_validity_days=cert_validity_days,
            cert_trusted_issuers=cert_trusted_issuers,
            cert_issuer_urls=cert_issuer_urls,
        )

        list_admin_settings_certs_response_200.additional_properties = d
        return list_admin_settings_certs_response_200

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
