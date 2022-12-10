from .stdout import Stdout
from .window import Window

import win32console


hwnd = win32console.GetConsoleWindow()
window = Window(hwnd)
