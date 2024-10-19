from textx import metamodel_from_file
import os

from app.utils import module_path

entity_mm = metamodel_from_file(module_path('grammar.tx'))

def scan_macro_files():
    macro_files = []
    for file in os.listdir(module_path("test-programs")):
        if file.endswith(".tm"):
            macro_files.append(os.path.join(module_path("test-programs"), file))
    return macro_files

def load_macros_model(file_path):
    model = entity_mm.model_from_file(file_path)
    return model

def load_macros():
    macro_files = scan_macro_files()
    return [load_macros_model(macros) for macros in macro_files]

def main():
    macros = load_macros()
    print(macros)


if __name__ == "__main__":
    main()
