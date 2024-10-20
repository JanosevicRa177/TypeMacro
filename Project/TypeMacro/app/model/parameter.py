import string
from app.model.enums.type import Type


class Parameter:

    def __init__(self, name: string, a_type: string, index: int):
        self.name = name
        self.index = index
        self.a_type = Type.from_string(a_type)
