from app.model.parameter import Parameter
from app.model.sequence_part.if_command.comparison import Comparison


class Condition:
    comparison: Comparison | None = None
    identifier: Parameter | None = None

    def __init__(self, condition):
        if condition.comparison:
            self.comparison = Comparison(condition.comparison)
        if condition.identifier:
            self.identifier = condition.identifier.name