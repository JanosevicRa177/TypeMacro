import string

from app.model.function import Function
from app.model.macro_group import MacroGroup
from app.model.sequence_part.function_call.function_call import FunctionCall
from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sequence_part import SequencePart
from app.utils import flatten_list


class IfCursorCommand(SequencePart):

    def __init__(self, sequence: list[SequencePart], cursor_color: string, parent: Function | MacroGroup):
        self.sequence = sequence
        self.cursor_color = cursor_color
        self.parent = parent

    def run_part(self) -> bool:
        pass

    def get_whole_key_sequence(self, function_call: FunctionCall | None) -> list[SequencePart]:
        sequence_parts = (
            [MacroCommand(["cursor", self.cursor_color])]
            + flatten_list([sequence_part.get_whole_key_sequence(function_call) for sequence_part in self.sequence])
            + [MacroCommand(["cursor_end"])]
        )
        return sequence_parts
