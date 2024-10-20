from abc import ABC, abstractmethod


class SequencePart(ABC):

    @abstractmethod
    def run_part(self) -> bool:
        pass
