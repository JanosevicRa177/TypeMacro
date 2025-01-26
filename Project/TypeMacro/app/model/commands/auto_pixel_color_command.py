import string

from app.model.commands.command import Command
from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sequence_part import SequencePart


class AutoPixelColorCommand(Command):

    def __init__(
        self,
        color: string,
        x: int,
        y: int,
        pixel_listen_delay: int,
        sequence: list[SequencePart],
    ):
        self.color = color
        self.x = x
        self.y = y
        self.pixel_listen_delay = pixel_listen_delay
        self.sequence = sequence

    def get_macro(self) -> MacroCommand:
        return MacroCommand(["color", self.color, str(self.x), str(self.y)])
