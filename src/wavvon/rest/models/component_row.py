from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_row_type import ComponentRowType

if TYPE_CHECKING:
    from ..models.message_component import MessageComponent


T = TypeVar("T", bound="ComponentRow")


@_attrs_define
class ComponentRow:
    """
    Attributes:
        type_ (ComponentRowType):
        components (list[MessageComponent]):
    """

    type_: ComponentRowType
    components: list[MessageComponent]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.message_component import MessageComponent

        d = dict(src_dict)
        type_ = ComponentRowType(d.pop("type"))

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = MessageComponent.from_dict(components_item_data)

            components.append(components_item)

        component_row = cls(
            type_=type_,
            components=components,
        )

        component_row.additional_properties = d
        return component_row

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
