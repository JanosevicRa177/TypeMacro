from app.model.sequence_part.function_call.attribute import Attribute
from app.model.sequence_part.function_call.function_call import FunctionCall


def _resolve_attribute(attribute, function_call: FunctionCall | None) -> Attribute:
    if attribute.parameter_name:
        parameter = function_call.function.get_parameter_by_name(attribute.parameter_name)
        real_attribute = function_call.resolve_attribute_value(parameter.index)
        return real_attribute
    else:
        return attribute


class Comparison:

    def __init__(self, comparison):
        self.left = Attribute(comparison.left, 0)
        self.operator = comparison.operator
        self.right = Attribute(comparison.right, 0)

    def evaluate(self, function_call: FunctionCall | None):
        left_value = _resolve_attribute(self.left, function_call)
        right_value = _resolve_attribute(self.right, function_call)
        if left_value.bool_value is not None and right_value.bool_value is not None:
            if self.operator not in ("==", "!="):
                raise ValueError("Invalid operator '{}' for boolean comparison.".format(self.operator))
        if self.operator == "==":
            return left_value.get_value() == right_value.get_value()
        elif self.operator == "!=":
            return left_value.get_value() != right_value.get_value()
        elif self.operator == "<":
            return left_value.get_value() < right_value.get_value()
        elif self.operator == "<=":
            return left_value.get_value() <= right_value.get_value()
        elif self.operator == ">":
            return left_value.get_value() > right_value.get_value()
        elif self.operator == ">=":
            return left_value.get_value() >= right_value.get_value()
        else:
            raise ValueError("Unknown comparison operator: {}".format(self.operator))
