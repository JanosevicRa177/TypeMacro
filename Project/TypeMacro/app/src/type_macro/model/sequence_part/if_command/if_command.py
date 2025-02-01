from type_macro.model.enums.type import Type
from type_macro.model.parent import Parent
from type_macro.model.sequence_part.function_call.attribute import Attribute
from type_macro.model.sequence_part.function_call.function_call import FunctionCall
from type_macro.model.sequence_part.if_command.condition import Condition
from type_macro.model.sequence_part.sequence_part import SequencePart
from type_macro.utils import flatten_list


class IfCommand(SequencePart):
    else_sequence: list[SequencePart] | None = None

    def __init__(
        self,
        condition,
        if_sequence: list[SequencePart],
        else_sequence: list[SequencePart] | None,
        parent: Parent,
    ):
        self.condition = Condition(condition)
        self.if_sequence = if_sequence
        if else_sequence is not None:
            self.else_sequence = else_sequence
        self.parent = parent

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        if self.condition.identifier:
            parameter = self.parent.get_parameter_by_name(self.condition.identifier)
            attribute = function_call.get_attribute_by_index(parameter.index)
            if attribute.bool_value is None:
                raise Exception(
                    "Attribute and parameter missmatch: "
                    + parameter.name
                    + " , "
                    + attribute.get_value()
                )
            elif attribute.bool_value:
                return flatten_list(
                    [
                        sequence_part.get_whole_key_sequence(function_call)
                        for sequence_part in self.if_sequence
                    ]
                )
            elif self.else_sequence is not None:
                return flatten_list(
                    [
                        sequence_part.get_whole_key_sequence(function_call)
                        for sequence_part in self.else_sequence
                    ]
                )
            else:
                return []
        if self.condition.comparison:
            left_parameter_type = self.get_attribute_type(
                self.condition.comparison.left
            )
            right_parameter_type = self.get_attribute_type(
                self.condition.comparison.right
            )
            if left_parameter_type != right_parameter_type:
                raise Exception(
                    "Left and right parameter types missmatch: "
                    + self.condition.comparison.left.get_value()
                    + " , "
                    + self.condition.comparison.right.get_value()
                )
            if self.condition.comparison.evaluate(function_call):
                return flatten_list(
                    [
                        sequence_part.get_whole_key_sequence(function_call)
                        for sequence_part in self.if_sequence
                    ]
                )
            elif self.else_sequence is not None:
                return flatten_list(
                    [
                        sequence_part.get_whole_key_sequence(function_call)
                        for sequence_part in self.else_sequence
                    ]
                )
            else:
                return []

    def get_attribute_type(self, attribute: Attribute) -> Type:
        if attribute.parameter_name:
            parameter = self.parent.get_parameter_by_name(attribute.parameter_name)
            return parameter.a_type
        elif attribute.bool_value:
            return Type.BOOLEAN
        elif attribute.int_value:
            return Type.NUMBER
        else:
            raise Exception("Invalid type")
