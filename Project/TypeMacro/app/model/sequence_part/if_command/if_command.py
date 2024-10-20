from app.model.sequence_part.if_command.condition import Condition
from app.model.sequence_part.sequence_part import SequencePart


class IfCommand(SequencePart):

    def __init__(self, condition, if_sequence: list[SequencePart], else_sequence: list[SequencePart] | None):
        self.condition = Condition(condition)
        self.if_sequence = if_sequence
        if else_sequence is not None:
            self.else_sequence = else_sequence

    def run_part(self) -> bool:
        pass
