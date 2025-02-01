from type_macro.model.commands.auto_pixel_color_command import AutoPixelColorCommand
from type_macro.model.commands.command import Command
from type_macro.model.commands.macro import Macro
from type_macro.model.sequence_part.function_call.function_call import FunctionCall
from type_macro.model.sequence_part.if_command.if_command import IfCommand
from type_macro.model.sequence_part.loop_command.loop_command import LoopCommand
from type_macro.model.sequence_part.macro_command.macro_command import MacroCommand
from type_macro.model.sequence_part.sequence_part import SequencePart
from type_macro.model.sequence_part.sleep_command.random_sleep_command import (
    RandomSleepCommand,
)
from type_macro.model.sequence_part.sleep_command.sleep_command import SleepCommand


def interpret_sequence_part(sequence_part, parent) -> SequencePart:
    if sequence_part.sleep is not None:
        if sequence_part.sleep.__class__.__name__ == "Sleep":
            return SleepCommand(sequence_part.sleep.sleepValue, parent)
        if sequence_part.sleep.__class__.__name__ == "RandomSleep":
            return RandomSleepCommand(
                sequence_part.sleep.min, sequence_part.sleep.max, parent
            )
    elif sequence_part.loop is not None:
        sequence = [
            interpret_sequence_part(sequence_part, parent)
            for sequence_part in sequence_part.loop.sequence
        ]
        return LoopCommand(sequence_part.loop.loop_iterator, sequence, parent)
    elif sequence_part.if_ is not None:
        if_sequence = [
            interpret_sequence_part(sequence_part, parent)
            for sequence_part in sequence_part.if_.if_sequence
        ]
        else_sequence = None
        if sequence_part.if_.else_statement is not None:
            else_sequence = [
                interpret_sequence_part(sequence_part, parent)
                for sequence_part in sequence_part.if_.else_statement.else_sequence
            ]
        return IfCommand(
            sequence_part.if_.condition, if_sequence, else_sequence, parent
        )
    elif sequence_part.macro is not None:
        return MacroCommand(sequence_part.macro.keys)
    elif sequence_part.func_call is not None:
        return FunctionCall(sequence_part.func_call, sequence_part.attributes, parent)


def interpret_command(command, parent) -> Command:
    if command.auto_pixel_command is not None:
        sequence = [
            interpret_sequence_part(sequence_part, parent)
            for sequence_part in command.auto_pixel_command.sequence
        ]
        return AutoPixelColorCommand(
            command.auto_pixel_command.color,
            command.auto_pixel_command.x,
            command.auto_pixel_command.y,
            command.auto_pixel_command.pixel_listen_delay,
            sequence,
        )
    if command.macro_command is not None:
        sequence = [
            interpret_sequence_part(sequence_part, parent)
            for sequence_part in command.macro_command.sequence
        ]
        macro_command = MacroCommand(command.macro_command.macro.keys)
        return Macro(macro_command, sequence)
