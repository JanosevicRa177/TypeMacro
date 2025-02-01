from textx import metamodel_from_file
import os

from type_macro.interpreter.interpreter import interpret
from type_macro.loop_checker.checker import Checker
from type_macro.model.macro_group import MacroGroup

entity_mm = metamodel_from_file("src/type_macro/grammar.tx", auto_init_attributes=False)


def scan_macro_files():
    macro_files = []
    file_names = []
    for file in os.listdir("../test-programs"):
        if file.endswith(".tm"):
            macro_files.append(os.path.join("../test-programs", file))
            file_names.append(file)
    return macro_files, file_names


def load_macros_model(file_path, file_name):
    model = entity_mm.model_from_file(file_path)
    macro_group = MacroGroup(model, file_name)
    return macro_group


def load_macros():
    [macro_files, file_names] = scan_macro_files()
    return [
        load_macros_model(macros, file_name)
        for macros, file_name in zip(macro_files, file_names)
    ]


def main():
    macros = load_macros()
    checker = Checker()
    [
        checker.detect_cycle(macro_group.full_macros, macro_group.file_name)
        for macro_group in macros
    ]
    macro_to_start = [macro for macro in macros if macro.file_name == "test11.tm"]
    interpret(macro_to_start[0])


if __name__ == "__main__":
    main()
