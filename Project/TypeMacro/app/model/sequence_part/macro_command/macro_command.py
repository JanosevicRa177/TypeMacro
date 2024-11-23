from app.model.sequence_part.function_call.function_call import FunctionCall
from app.model.sequence_part.macro_command.key import Key
from app.model.sequence_part.sequence_part import SequencePart


class MacroCommand(SequencePart):

    def __init__(self, keys: list[str]):
        self.keys = [Key(key) for key in keys]

    def run_part(self) -> bool:
        pass

    def get_whole_key_sequence(self, function_call: FunctionCall | None) -> list[SequencePart]:
        return [self]

    def get_macro_string(self) -> str:
        return " + ".join([key.value for key in self.keys])
