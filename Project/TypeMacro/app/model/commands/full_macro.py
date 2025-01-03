from collections import Counter

from app.model.sequence_part.macro_command.macro_command import MacroCommand


class FullMacro:

    def __init__(self, macro: MacroCommand, sequence: list[MacroCommand]):
        self.macro = macro
        self.sequence = sequence

    def run_command(self) -> bool:
        pass

    def is_activated_by(self, macro_to_check: MacroCommand) -> bool:
        self_keys = [key.value.lower() for key in self.macro.keys]
        check_keys = [key.value.lower() for key in macro_to_check.keys]
        return Counter(self_keys) == Counter(check_keys)
