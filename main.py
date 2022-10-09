import platform

import keyboard
import pyautogui
import pyperclip

charka = '́'
chachek = '̌'
u = "̊"


def ctrl_v():
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")


def print_u():
    tmp = pyperclip.paste()
    pyperclip.copy(u)
    ctrl_v()
    pyperclip.copy(tmp)


def print_charka():
    tmp = pyperclip.paste()
    pyperclip.copy(charka)
    ctrl_v()
    pyperclip.copy(tmp)


def print_chachek():
    tmp = pyperclip.paste()
    pyperclip.copy(chachek)
    ctrl_v()
    pyperclip.copy(tmp)


keyboard.add_hotkey('ctrl + shift + =', print_chachek, suppress=True)
keyboard.add_hotkey('ctrl + =', print_charka, suppress=True)
keyboard.add_hotkey('ctrl + 0', print_u, suppress=True)

while True:
    pass
