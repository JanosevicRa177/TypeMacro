from app.model.sequence_part.loop_command.loop_iterator import LoopIterator
from app.model.sequence_part.sequence_part import SequencePart


class LoopCommand(SequencePart):

    def __init__(self, repetitions, sequence: list[SequencePart]):
        self.repetitions = LoopIterator(repetitions)
        self.sequence = sequence

    def run_part(self) -> bool:
        pass
