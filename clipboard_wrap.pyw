import tkinter as tk
from tkinter import simpledialog
import unicodedata

import pyperclip


def get_char_width(char):
    # 全角・幅広文字は2、半角文字は1として数える
    return 2 if unicodedata.east_asian_width(char) in ("F", "W", "A") else 1


def wrap_line(line, max_width):
    wrapped_lines = []
    current_line = ""
    current_width = 0

    for char in line:
        char_width = get_char_width(char)

        if current_line and current_width + char_width > max_width:
            wrapped_lines.append(current_line)
            current_line = char
            current_width = char_width
        else:
            current_line += char
            current_width += char_width

    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines


root = tk.Tk()
root.withdraw()

full_width_chars = simpledialog.askinteger(
    "改行文字数",
    "1行あたりの全角文字数を入力してください。",
    initialvalue=40,
    minvalue=1,
)

if full_width_chars is not None:
    # 全角1文字＝幅2として、内部用の最大表示幅へ変換
    max_width = full_width_chars * 2

    text = pyperclip.paste()
    wrapped_lines = []

    for line in text.splitlines():
        if line:
            wrapped_lines.extend(wrap_line(line, max_width))
        else:
            wrapped_lines.append("")

    result = "\n".join(wrapped_lines)
    pyperclip.copy(result)

root.destroy()