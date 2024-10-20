from app.model.sequence_part.macro_command.key import Key
from app.model.sequence_part.sequence_part import SequencePart


class MacroCommand(SequencePart):

    def __init__(self, keys: list[Key]):
        self.keys = [Key(key) for key in keys]

    def run_part(self) -> bool:
        pass
