import typer

from .type_macro import type_macro


app = typer.Typer()
app.command()(type_macro)


if __name__ == "__main__":
    app()
