from abc import ABC, abstractmethod

from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sequence_part import SequencePart


class Command(ABC):
    sequence: list[SequencePart] | None = None

    @abstractmethod
    def get_macro(self) -> MacroCommand:
        pass
