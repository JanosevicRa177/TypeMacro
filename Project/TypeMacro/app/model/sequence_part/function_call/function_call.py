from app.model.sequence_part.function_call.attribute import Attribute
from app.model.sequence_part.sequence_part import SequencePart


class FunctionCall(SequencePart):

    def __init__(self, function, attributes):
        self.function_name = function.name
        self.attributes = [Attribute(attribute, index) for index, attribute in enumerate(attributes)]

    def run_part(self) -> bool:
        pass
