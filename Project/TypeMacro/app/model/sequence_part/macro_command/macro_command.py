import warnings

from app.model.sequence_part.function_call.function_call import FunctionCall
from app.model.sequence_part.macro_command.key import Key
from app.model.sequence_part.sequence_part import SequencePart


class MacroCommand(SequencePart):

    def __init__(self, keys: list[str]):
        self.keys = [Key(key) for key in keys]
        macro_as_set = set([key.value.lower() for key in self.keys])
        if macro_as_set == {"alt", "f12"}:
            warnings.warn("Do not use Alt + f12, its used to stop the execution")

    def get_whole_key_sequence(
        self, function_call: FunctionCall | None
    ) -> list[SequencePart]:
        return [self]

    def get_macro_string(self) -> str:
        return " + ".join([key.value for key in self.keys])
