from enum import Enum


class Type(Enum):
    NUMBER = 1
    BOOLEAN = 2

    @classmethod
    def from_string(cls, type_str):
        try:
            return cls[type_str.upper()]
        except KeyError:
            raise ValueError(f"{type_str} is not a valid Type")
