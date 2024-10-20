from app.model.sequence_part.sequence_part import SequencePart


class RandomSleepCommand(SequencePart):

    def __init__(self, min_sleep: int, max_sleep: int):
        self.min_sleep = min_sleep
        self.max_sleep = max_sleep

    def run_part(self) -> bool:
        pass
