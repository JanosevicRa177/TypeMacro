from __future__ import annotations

from abc import ABC, abstractmethod


class SequencePart(ABC):

    @abstractmethod
    def get_whole_key_sequence(self, function_call) -> list[SequencePart]:
        pass
