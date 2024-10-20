from app.model.converter.converter import interpret_sequence_part
from app.model.parameter import Parameter


class Function:

    def __init__(self, name, parameters, sequence):
        self.name = name
        self.parameters = [Parameter(parameter.name, parameter.type, index) for index, parameter in enumerate(parameters)]
        self.sequence = [interpret_sequence_part(sequence_part) for sequence_part in sequence]
