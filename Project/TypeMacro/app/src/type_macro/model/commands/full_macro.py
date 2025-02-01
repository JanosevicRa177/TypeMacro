from collections import Counter

from type_macro.model.commands.auto_pixel_color_command import AutoPixelColorCommand
from type_macro.model.commands.command import Command
from type_macro.model.sequence_part.macro_command.macro_command import MacroCommand
from type_macro.utils import flatten_list


class FullMacro:
    is_auto_pixel: bool = False

    def __init__(self, macro: Command):
        if isinstance(macro, AutoPixelColorCommand):
            self.is_auto_pixel = True
            self.color = macro.color
            self.x = macro.x
            self.y = macro.y
            self.pixel_listen_delay = macro.pixel_listen_delay
        else:
            self.macro = macro.get_macro()
        self.sequence = flatten_list(
            [
                sequence_part.get_whole_key_sequence(None)
                for sequence_part in macro.sequence
            ]
        )

    def is_activated_by(self, macro_to_check: MacroCommand) -> bool:
        if self.is_auto_pixel:
            return False
        self_keys = [key.value.lower() for key in self.macro.keys]
        check_keys = [key.value.lower() for key in macro_to_check.keys]
        return Counter(self_keys) == Counter(check_keys)
