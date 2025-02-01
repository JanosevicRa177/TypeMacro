from type_macro.model.enums.type import Type
from type_macro.model.parent import Parent
from type_macro.model.sequence_part.function_call.attribute import Attribute
from type_macro.model.sequence_part.function_call.function_call import FunctionCall
from type_macro.model.sequence_part.sequence_part import SequencePart
from type_macro.utils import flatten_list


def _resolve_attribute(attribute, function_call: FunctionCall | None) -> Attribute:
    if attribute.parameter_name:
        parameter = function_call.function.get_parameter_by_name(
            attribute.parameter_name
        )
        real_attribute = function_call.resolve_attribute_value(parameter.index)
        return real_attribute
    else:
        return attribute


class LoopCommand(SequencePart):

    def __init__(self, repetitions, sequence: list[SequencePart], parent: Parent):
        self.repetitions = Attribute(repetitions, 0)
        self.sequence = sequence
        self.parent = parent
        attribute_type = self.get_attribute_type(self.repetitions)
        if attribute_type != Type.NUMBER:
            raise Exception(
                "Wrong type in loop command for parameter: "
                + self.repetitions.get_value()
            )

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        attribute = _resolve_attribute(self.repetitions, function_call)
        if attribute.int_value is None:
            raise Exception(
                "Attribute type missmatch in loop: "
                + function_call.function.name
                + " , "
                + attribute.get_value()
            )
        return (
            flatten_list(
                [
                    sequence_part.get_whole_key_sequence(function_call)
                    for sequence_part in self.sequence
                ]
            )
            * attribute.int_value
        )

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
