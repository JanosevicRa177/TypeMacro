from app.model.commands.command import Command
from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sequence_part import SequencePart


class Macro(Command):

    def __init__(self, macro: MacroCommand, sequence: list[SequencePart]):
        self.macro = macro
        self.sequence = sequence

    def run_command(self) -> bool:
        pass

    def get_macro(self) -> MacroCommand:
        return self.macro
