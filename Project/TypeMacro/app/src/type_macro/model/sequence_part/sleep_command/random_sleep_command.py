from type_macro.model.enums.type import Type
from type_macro.model.parent import Parent
from type_macro.model.sequence_part.function_call.attribute import Attribute
from type_macro.model.sequence_part.function_call.function_call import FunctionCall
from type_macro.model.sequence_part.macro_command.macro_command import MacroCommand
from type_macro.model.sequence_part.sequence_part import SequencePart


class RandomSleepCommand(SequencePart):

    def __init__(self, min_sleep, max_sleep, parent: Parent):
        self.min_sleep = Attribute(min_sleep, 0)
        self.max_sleep = Attribute(max_sleep, 0)
        self.parent = parent
        self.check_sleep_type(self.min_sleep)
        self.check_sleep_type(self.max_sleep)

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        min_sleep_value = self.min_sleep.get_value()
        if self.min_sleep.parameter_name:
            parameter = function_call.function.get_parameter_by_name(
                self.min_sleep.parameter_name
            )
            min_sleep_value = function_call.resolve_attribute_value(
                parameter.index
            ).get_value()
        max_sleep_value = self.max_sleep.get_value()
        if self.max_sleep.parameter_name:
            parameter = function_call.function.get_parameter_by_name(
                self.max_sleep.parameter_name
            )
            max_sleep_value = function_call.resolve_attribute_value(
                parameter.index
            ).get_value()
        return [
            MacroCommand(["random_sleep", str(min_sleep_value), str(max_sleep_value)])
        ]

    def check_sleep_type(self, sleep: Attribute):
        if sleep.bool_value is not None:
            raise Exception("Random sleep can't take boolean as value")
        if sleep.parameter_name:
            parameter = self.parent.get_parameter_by_name(sleep.parameter_name)
            if parameter.a_type != Type.NUMBER:
                raise Exception(
                    "Wrong type in random sleep command for parameter: "
                    + parameter.name
                )
