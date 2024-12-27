import threading
import time
from time import sleep

from pynput.keyboard import Key, Listener, KeyCode, Controller

from app.model.commands.full_macro import FullMacro
from app.model.macro_group import MacroGroup
from app.model.sequence_part.macro_command.macro_command import MacroCommand

current_keypress_group = set()
listener: Listener = Listener()
should_listen = True
event: threading.Event
keypress_delay: int | None = None


def execute_macro_sequence(macros: list[MacroCommand]):
    keyboard = Controller()
    sleep(0.2)
    for macro in macros:
        if not should_listen:
            break
        for key in macro.keys:
            keyboard.press(to_key_code(key.value.lower()))
        sleep(keypress_delay / 1000)
        for key in macro.keys:
            keyboard.release(to_key_code(key.value.lower()))


def listen_to_macro(full_macro: FullMacro):
    global current_keypress_group
    macro_as_set = set([key.value.lower() for key in full_macro.macro.keys])
    while should_listen:
        time.sleep(0.1)
        if current_keypress_group == macro_as_set:
            thread = threading.Thread(target=execute_macro_sequence, args=[full_macro.sequence])
            thread.daemon = True
            thread.start()


def interpret(macro: MacroGroup):
    global listener
    global keypress_delay
    keypress_delay = macro.keypress_delay
    print(len(macro.full_macros))
    for macro_command in macro.full_macros:
        thread = threading.Thread(target=listen_to_macro, args=[macro_command])
        thread.daemon = True
        thread.start()
    listener = Listener(on_press=on_keypress, on_release=release)
    listener.start()
    listener.join()


def on_keypress(key: Key | KeyCode | None):
    global listener
    key_str = map_key_to_string(key)
    current_keypress_group.add(key_str)
    print(current_keypress_group)


def release(key: Key | KeyCode | None) -> bool:
    key_str = map_key_to_string(key)
    current_keypress_group.discard(key_str)
    print(current_keypress_group)


def map_key_to_string(key: Key | KeyCode | None) -> str:
    key = listener.canonical(key)
    if isinstance(key, KeyCode):
        key_str = key.char
        if key_str is None:
            key_str = map_specific_keys(key)
    else:
        key_str = key.name
    return key_str


def map_specific_keys(key) -> str:
    if str(key) == "<8>":
        return "backspace"
    elif str(key) == "<9>":
        return "tab"
    elif str(key) == "<32>":
        return "space"
    elif str(key) == "<13>":
        return "enter"
    elif str(key) == "<27>":
        return "esc"
    elif str(key) == "<112>":
        return "f1"
    elif str(key) == "<113>":
        return "f2"
    elif str(key) == "<114>":
        return "f3"
    elif str(key) == "<115>":
        return "f4"
    elif str(key) == "<116>":
        return "f5"
    elif str(key) == "<117>":
        return "f6"
    elif str(key) == "<118>":
        return "f7"
    elif str(key) == "<119>":
        return "f8"
    elif str(key) == "<120>":
        return "f9"
    elif str(key) == "<121>":
        return "f10"
    elif str(key) == "<122>":
        return "f11"
    elif str(key) == "<123>":
        return "f12"


def to_key_code(c: str) -> str | Key | None:
    return key_code_map[c]


key_code_map = {
    "backspace": Key.backspace,
    "tab": Key.tab,
    "enter": Key.enter,
    "shift": Key.shift,
    "esc": Key.esc,
    "space": Key.space,
    "ctrl": Key.ctrl,
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z",
    "š": "š",
    "đ": "đ",
    "ć": "ć",
    "č": "č",
    "ž": "ž",
    "f1": Key.f1,
    "f2": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    "f5": Key.f5,
    "f6": Key.f6,
    "f7": Key.f7,
    "f8": Key.f8,
    "f9": Key.f9,
    "f10": Key.f10,
    "f11": Key.f11,
    "f12": Key.f12,
}
