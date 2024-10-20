from app.model.converter.converter import interpret_command
from app.model.function import Function


class MacroGroup:
    keypress_delay = 50
    color_offset = 10

    def __init__(self, model):
        if model.keypressDelay:
            self.keypress_delay = model.keypressDelay.keypress_delay
        if model.colorOffset:
            self.color_offset = model.colorOffset.offset

        self.functions = [Function(function.name, function.parameters, function.sequence) for function in model.functions]
        self.macros = [interpret_command(command) for command in model.commands]
