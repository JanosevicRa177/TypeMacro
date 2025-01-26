from app.model.enums.type import Type
from app.model.parent import Parent
from app.model.sequence_part.function_call.attribute import Attribute
from app.model.sequence_part.function_call.function_call import FunctionCall
from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sequence_part import SequencePart


class SleepCommand(SequencePart):

    def __init__(self, sleep_value, parent: Parent):
        self.sleep = Attribute(sleep_value, 0)
        self.parent = parent
        self.check_sleep_type(self.sleep)

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        sleep_value = self.sleep.get_value()
        if self.sleep.parameter_name:
            parameter = function_call.function.get_parameter_by_name(
                self.sleep.parameter_name
            )
            sleep_value = function_call.resolve_attribute_value(
                parameter.index
            ).get_value()
        return [MacroCommand(["sleep", str(sleep_value)])]

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
