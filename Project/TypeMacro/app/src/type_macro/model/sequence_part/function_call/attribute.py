class Attribute:
    bool_value: bool | None = None
    int_value: int | None = None
    parameter_name: str | None = None

    def __init__(self, attribute, index):
        self.value = attribute.__dir__()
        self.index = index
        if attribute.bool is not None:
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
