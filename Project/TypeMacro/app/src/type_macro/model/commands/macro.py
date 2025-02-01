from type_macro.model.commands.command import Command
from type_macro.model.sequence_part.macro_command.macro_command import MacroCommand
from type_macro.model.sequence_part.sequence_part import SequencePart


class Macro(Command):

    def __init__(self, macro: MacroCommand, sequence: list[SequencePart]):
        self.macro = macro
        self.sequence = sequence

    def get_macro(self) -> MacroCommand:
        return self.macro
