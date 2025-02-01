from __future__ import annotations

from type_macro.model.enums.type import Type
from type_macro.model.function import Function
from type_macro.model.parent import Parent
from type_macro.model.sequence_part.function_call.attribute import Attribute
from type_macro.model.sequence_part.sequence_part import SequencePart
from type_macro.utils import flatten_list


class FunctionCall(SequencePart):
    parent_function_call: FunctionCall | None = None
    function: Function | None = None

    def __init__(self, function, attributes, parent: Parent):
        self.function_name = function.name
        self.attributes = [
            Attribute(attribute, index) for index, attribute in enumerate(attributes)
        ]
        self.parent = parent

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        self.function = self.parent.find_function_by_name(self.function_name)
        if self.function is None:
            raise Exception("Function with name:" + self.function_name + " not found")
        self.parent_function_call = function_call
        for attribute in self.attributes:
            self.check_function_typings(attribute.index)
        return flatten_list(
            [
                sequence_part.get_whole_key_sequence(self)
                for sequence_part in self.function.sequence
            ]
        )

    def get_attribute_by_index(self, index: int) -> Attribute:
        return self.attributes[index]

    def check_function_typings(self, index: int):
        parameter = self.function.parameters[index]
        attribute = self.get_attribute_by_index(index)
        if attribute.parameter_name is None:
            if (parameter.a_type == Type.NUMBER) and attribute.int_value is None:
                raise Exception(
                    "Parameter: "
                    + parameter.name
                    + " has an invalid type in function "
                    + self.function.name
                    + ", value "
                    + str(attribute.bool_value)
                )
            if (parameter.a_type == Type.BOOLEAN) and attribute.bool_value is None:
                raise Exception(
                    "Parameter: "
                    + parameter.name
                    + " has an invalid type in function "
                    + self.function.name
                    + ", value "
                    + str(attribute.int_value)
                )

    def resolve_attribute_value(self, index: int) -> Attribute:
        attribute = self.get_attribute_by_index(index)
        if attribute.parameter_name is not None:
            if self.parent_function_call is None:
                raise Exception(
                    "Value not found for parameter:" + attribute.parameter_name
                )
            parameter = self.parent_function_call.function.get_parameter_by_name(
                attribute.parameter_name
            )
            return self.parent_function_call.resolve_attribute_value(parameter.index)
        else:
            return attribute
