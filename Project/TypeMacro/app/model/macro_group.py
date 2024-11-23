from app.model.commands.full_macro import FullMacro
from app.model.function import Function
from app.model.parameter import Parameter
from app.model.parent import Parent
from app.utils import flatten_list


class MacroGroup(Parent):
    keypress_delay = 50
    color_offset = 10
    full_macros: list[FullMacro] | None = None
    file_name: str | None = None

    def __init__(self, model, file_name):
        from app.model.converter.converter import interpret_command

        self.file_name = file_name
        if model.keypressDelay:
            self.keypress_delay = model.keypressDelay.keypress_delay
        if model.colorOffset:
            self.color_offset = model.colorOffset.offset
        self.functions = [Function(function.name, function.parameters, function.sequence, self) for function in model.functions]
        macros = [interpret_command(command, self) for command in model.commands]
        self.full_macros = [
            FullMacro(macro.get_macro(), flatten_list([sequence_part.get_whole_key_sequence(None) for sequence_part in macro.sequence]))
            for macro in macros
        ]

    def find_function_by_name(self, name: str) -> Function:
        return next((function for function in self.functions if function.name == name), None)

    def get_parameter_by_name(self, name) -> Parameter:
        raise Exception("There is no parameter: " + name + " in program")
