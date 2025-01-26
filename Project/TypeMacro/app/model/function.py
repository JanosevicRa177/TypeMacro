from __future__ import annotations
from app.model.parameter import Parameter
from app.model.parent import Parent


class Function(Parent):
    def __init__(self, name, parameters, sequence, parent):
        from app.model.converter.converter import interpret_sequence_part

        self.name = name
        self.parameters = [
            Parameter(parameter.name, parameter.type, index)
            for index, parameter in enumerate(parameters)
        ]
        self.sequence = [
            interpret_sequence_part(sequence_part, self) for sequence_part in sequence
        ]
        self.parent = parent

    def get_parameter_by_name(self, name) -> Parameter:
        for parameter in self.parameters:
            if parameter.name == name:
                return parameter
        raise Exception("There is no parameter: " + name + " in class " + self.name)

    def find_function_by_name(self, name: str) -> Function:
        return self.parent.find_function_by_name(name)
