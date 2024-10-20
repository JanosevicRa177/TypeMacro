from app.model.commands.auto_pixel_color_command import AutoPixelColorCommand
from app.model.commands.command import Command
from app.model.commands.macro import Macro
from app.model.sequence_part.function_call.function_call import FunctionCall
from app.model.sequence_part.if_command.if_command import IfCommand
from app.model.sequence_part.if_cursor_command import IfCursorCommand
from app.model.sequence_part.loop_command.loop_command import LoopCommand
from app.model.sequence_part.macro_command.macro_command import MacroCommand
from app.model.sequence_part.sleep_command.random_sleep_command import RandomSleepCommand
from app.model.sequence_part.sequence_part import SequencePart
from app.model.sequence_part.sleep_command.sleep_command import SleepCommand


def interpret_sequence_part(sequence_part) -> SequencePart:
    if sequence_part.if_cursor is not None:
        sequence = [interpret_sequence_part(sequence_part) for sequence_part in sequence_part.if_cursor.if_sequence]
        return IfCursorCommand(sequence, sequence_part.if_cursor.color)
    elif sequence_part.sleep is not None:
        if sequence_part.sleep.__class__.__name__ == "Sleep":
            return SleepCommand(sequence_part.sleep.sleepValue)
        if sequence_part.sleep.__class__.__name__ == "RandomSleep":
            return RandomSleepCommand(sequence_part.sleep.min, sequence_part.sleep.max)
    elif sequence_part.loop is not None:
        sequence = [interpret_sequence_part(sequence_part) for sequence_part in sequence_part.loop.sequence]
        return LoopCommand(sequence_part.loop.loop_iterator, sequence)
    elif sequence_part.if_ is not None:
        if_sequence = [interpret_sequence_part(sequence_part) for sequence_part in sequence_part.if_.if_sequence]
        else_sequence = None
        if sequence_part.if_.else_statement is not None:
            else_sequence = [interpret_sequence_part(sequence_part) for sequence_part in sequence_part.if_.else_statement.else_sequence]
        return IfCommand(sequence_part.if_.condition, if_sequence, else_sequence)
    elif sequence_part.macro is not None:
        return MacroCommand(sequence_part.macro.keys)
    elif sequence_part.func_call is not None:
        return FunctionCall(sequence_part.func_call, sequence_part.attributes)


def interpret_command(command) -> Command:
    if command.auto_pixel_command is not None:
        sequence = [interpret_sequence_part(sequence_part) for sequence_part in command.auto_pixel_command.sequence]
        return AutoPixelColorCommand(command.auto_pixel_command.color, command.auto_pixel_command.x, command.auto_pixel_command.y, sequence)
    if command.macro_command is not None:
        sequence = [interpret_sequence_part(sequence_part) for sequence_part in command.macro_command.sequence]
        macro_command = MacroCommand(command.macro_command.macro.keys)
        return Macro(macro_command, sequence)