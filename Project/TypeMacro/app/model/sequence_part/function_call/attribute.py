class Attribute:

    def __init__(self, attribute, index):
        self.value = attribute.__dir__()
        if attribute.bool:
            self.bool_value = attribute.bool
        elif attribute.int:
            self.int_value = attribute.int
        elif attribute.parameter:
            self.parameter_name = attribute.parameter.name

    def get_value(self):
        if self.bool_value:
            return self.bool_value
        elif self.int_value:
            return self.int_value
        elif self.parameter_name:
            return self.parameter_name

    def run_part(self) -> bool:
        pass
