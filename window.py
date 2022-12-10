import win32console
import win32gui
import win32con
import signal
import sys
from BlurWindow.blurWindow import GlobalBlur


def handle_off(signum, frame):
    pass


def handle_on(signum, frame):
    sys.exit()


class Window:

    @staticmethod
    def get_console_hwnd() -> any:
        """
        Return the hwnd of the console
        """
        return win32console.GetConsoleWindow()

    @staticmethod
    def get_window_hwnd() -> any:
        """
        Return the hwnd of Foreground window
        """
        return win32gui.GetForegroundWindow()

    @staticmethod
    def disable_keyboard_exit():
        signal.signal(signal.SIGINT, handle_off)

    @staticmethod
    def enable_keyboard_exit():
        signal.signal(signal.SIGINT, handle_on)

    def __init__(self, hwnd=win32console.GetConsoleWindow()) -> None:
        self.hwnd = hwnd
        self.hMenu = win32gui.GetSystemMenu(hwnd, 0)

    def exit(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_CLOSE, 0, 0)

    def disable_exit_btn(self):
        try:
            win32gui.EnableMenuItem(self.hMenu, win32con.SC_CLOSE,
                                    win32con.MF_BYCOMMAND | win32con.MF_DISABLED | win32con.MF_GRAYED)
            return 0
        except Exception as e:
            return e

    def enable_exit_btn(self):
        try:
            win32gui.EnableMenuItem(self.hMenu, win32con.SC_CLOSE,
                                    win32con.MF_BYCOMMAND | win32con.MF_ENABLED)
            return 0
        except Exception as e:
            return e

    def disable_min_btn(self):
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) & ~win32con.WS_MINIMIZEBOX)
            return 0
        except Exception as e:
            return e

    def enable_min_btn(self):
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) | win32con.WS_MINIMIZEBOX)
            return 0
        except Exception as e:
            return e

    def disable_max_btn(self):
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)
            return 0
        except Exception as e:
            return e

    def enable_max_btn(self):
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) | win32con.WS_MAXIMIZEBOX)
            return 0
        except Exception as e:
            return e

    def disable_all(self):
        self.disable_exit_btn()
        self.disable_max_btn()
        self.disable_min_btn()
        Window.disable_keyboard_exit()

    def enable_all(self):
        self.enable_exit_btn()
        self.enable_max_btn()
        self.enable_min_btn()
        Window.enable_keyboard_exit()

    def set_title(self, title: str):
        win32gui.SetWindowText(self.hwnd, title)

    def hide(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)

    def show(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)

    def blur_window(self):
        GlobalBlur(self.hwnd)
