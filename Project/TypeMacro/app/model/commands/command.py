from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def run_command(self) -> bool:
        pass
