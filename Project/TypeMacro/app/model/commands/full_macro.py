from collections import Counter

from app.model.commands.macro import Macro
from app.model.sequence_part.macro_command.key import Key
from app.model.sequence_part.macro_command.macro_command import MacroCommand


class FullMacro:

    def __init__(self, macro: MacroCommand, sequence: list[MacroCommand]):
        self.macro = macro
        self.sequence = sequence

    def run_command(self) -> bool:
        pass

    def print_all(self):
        print("============================")
        print(" + ".join([key.value for key in self.macro.keys]))
        print([macro_command.get_macro_string() for macro_command in self.sequence])

    def is_activated_by(self, macro_to_check: MacroCommand) -> bool:
        self_keys = [key.value.lower() for key in self.macro.keys]
        check_keys = [key.value.lower() for key in macro_to_check.keys]
        return Counter(self_keys) == Counter(check_keys)
