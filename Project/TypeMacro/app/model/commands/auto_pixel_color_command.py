import string

from app.model.commands.command import Command
from app.model.sequence_part.sequence_part import SequencePart


class AutoPixelColorCommand(Command):

    def __init__(self, color: string, x: int, y: int, sequence: list[SequencePart]):
        self.color = color
        self.x = x
        self.y = y
        self.sequence = sequence

    def run_command(self) -> bool:
        pass
