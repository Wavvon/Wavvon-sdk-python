from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_component_type import MessageComponentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_option import SelectOption


T = TypeVar("T", bound="MessageComponent")


@_attrs_define
class MessageComponent:
    """
    Attributes:
        type_ (MessageComponentType):
        custom_id (str):
        label (str | Unset):
        style (str | Unset):
        disabled (bool | Unset):
        placeholder (str | Unset):
        min_values (int | Unset):
        max_values (int | Unset):
        options (list[SelectOption] | Unset):
    """

    type_: MessageComponentType
    custom_id: str
    label: str | Unset = UNSET
    style: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    placeholder: str | Unset = UNSET
    min_values: int | Unset = UNSET
    max_values: int | Unset = UNSET
    options: list[SelectOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        custom_id = self.custom_id

        label = self.label

        style = self.style

        disabled = self.disabled

        placeholder = self.placeholder

        min_values = self.min_values

        max_values = self.max_values

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "custom_id": custom_id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if style is not UNSET:
            field_dict["style"] = style
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if min_values is not UNSET:
            field_dict["min_values"] = min_values
        if max_values is not UNSET:
            field_dict["max_values"] = max_values
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.select_option import SelectOption

        d = dict(src_dict)
        type_ = MessageComponentType(d.pop("type"))

        custom_id = d.pop("custom_id")

        label = d.pop("label", UNSET)

        style = d.pop("style", UNSET)

        disabled = d.pop("disabled", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        min_values = d.pop("min_values", UNSET)

        max_values = d.pop("max_values", UNSET)

        _options = d.pop("options", UNSET)
        options: list[SelectOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = SelectOption.from_dict(options_item_data)

                options.append(options_item)

        message_component = cls(
            type_=type_,
            custom_id=custom_id,
            label=label,
            style=style,
            disabled=disabled,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=options,
        )

        message_component.additional_properties = d
        return message_component

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
