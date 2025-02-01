from typing import Annotated

import typer
from textx import metamodel_from_file

from type_macro.interpreter.interpreter import interpret
from type_macro.loop_checker.checker import Checker
from type_macro.model.macro_group import MacroGroup
from type_macro.utils import module_path

entity_mm = metamodel_from_file(module_path("grammar.tx"), auto_init_attributes=False)


def load_macro_model(file_path):
    model = entity_mm.model_from_file(file_path)
    macro_group = MacroGroup(model, file_path)
    return macro_group


def type_macro(
    name: Annotated[
        str, typer.Argument(help="Relative path to TypeMacro DSL script")
    ] = ""
):
    macro = load_macro_model(name)
    checker = Checker()
    checker.detect_cycle(macro.full_macros, macro.file_name)

    interpret(macro)
