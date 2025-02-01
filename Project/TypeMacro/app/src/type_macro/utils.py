import os
from typing import TypeVar


def module_path(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)


T = TypeVar("T")


def flatten_list(matrix: list[list[T]]) -> list[T]:
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list
