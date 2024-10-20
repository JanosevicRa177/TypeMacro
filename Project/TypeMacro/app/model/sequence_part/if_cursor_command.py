import string

from app.model.sequence_part.sequence_part import SequencePart


class IfCursorCommand(SequencePart):

    def __init__(self, sequence: list[SequencePart], cursor_color: string):
        self.sequence = sequence
        self.cursor_color = cursor_color

    def run_part(self) -> bool:
        pass
