from abc import ABC, abstractmethod

from type_macro.model.parameter import Parameter


class Parent(ABC):

    @abstractmethod
    def get_parameter_by_name(self, name) -> Parameter:
        pass

    @abstractmethod
    def find_function_by_name(self, name: str):
        pass
