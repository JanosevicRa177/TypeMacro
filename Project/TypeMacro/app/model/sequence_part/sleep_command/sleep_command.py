from app.model.sequence_part.sequence_part import SequencePart


class SleepCommand(SequencePart):

    def __init__(self, sleep_value: int):
        self.sleep_value = sleep_value

    def run_part(self) -> bool:
        pass
