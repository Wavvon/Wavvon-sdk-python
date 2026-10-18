from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from typing_extensions import Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_channel_posts_response_200_results_item import (
        SearchChannelPostsResponse200ResultsItem,
    )


T = TypeVar("T", bound="SearchChannelPostsResponse200")


@_attrs_define
class SearchChannelPostsResponse200:
    """
    Attributes:
        results (list[SearchChannelPostsResponse200ResultsItem] | Unset):
        cursor (str | Unset):
    """

    results: list[SearchChannelPostsResponse200ResultsItem] | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_channel_posts_response_200_results_item import (
            SearchChannelPostsResponse200ResultsItem,
        )

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[SearchChannelPostsResponse200ResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = SearchChannelPostsResponse200ResultsItem.from_dict(
                    results_item_data
                )

                results.append(results_item)

        cursor = d.pop("cursor", UNSET)

        search_channel_posts_response_200 = cls(
            results=results,
            cursor=cursor,
        )

        search_channel_posts_response_200.additional_properties = d
        return search_channel_posts_response_200

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
