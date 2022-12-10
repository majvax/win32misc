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

    class Animation:
        hide = win32con.AW_HIDE
        blend = win32con.AW_BLEND
        center = win32con.AW_CENTER
        hor_positive = win32con.AW_HOR_POSITIVE
        hot_negative = win32con.AW_HOR_NEGATIVE
        slide = win32con.AW_SLIDE
        ver_positive = win32con.AW_VER_POSITIVE
        ver_negative = win32con.AW_VER_NEGATIVE

        def __init__(self) -> None:
            pass
    @staticmethod
    def get_console_hwnd() -> int:
        """
        Return the hwnd of the console
        """
        return win32console.GetConsoleWindow()

    @staticmethod
    def get_window_hwnd() -> int:
        """
        Return the hwnd of the Foreground window
        """
        return win32gui.GetForegroundWindow()

    @staticmethod
    def disable_keyboard_exit() -> None:
        """
        Disable keyboard exit (ctrl + c)
        :return: None
        """
        signal.signal(signal.SIGINT, handle_off)

    @staticmethod
    def enable_keyboard_exit() -> None:
        """
        Enable keyboard exit
        :return: None
        """
        signal.signal(signal.SIGINT, handle_on)

    def __init__(self, hwnd=get_window_hwnd()) -> None:
        """
        initialize the class
        :param hwnd: the hwnd on which all style will be applied
        """
        self.hwnd = hwnd
        self.hMenu = win32gui.GetSystemMenu(hwnd, 0)
        _, _, self.SCREEN_WIDTH, self.SCREEN_HEIGHT = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

    def exit(self) -> None:
        """
        Send `PostMessage` to exit the window
        :return: None
        """
        win32gui.PostMessage(self.hwnd, win32con.WM_CLOSE, 0, 0)

    def disable_exit_btn(self) -> None:
        """
        disable exit button
        :return: None
        """
        try:
            win32gui.EnableMenuItem(self.hMenu, win32con.SC_CLOSE,
                                    win32con.MF_BYCOMMAND | win32con.MF_DISABLED | win32con.MF_GRAYED)
        finally:
            return

    def enable_exit_btn(self) -> None:
        """
        Enable exit button
        :return: None
        """
        try:
            win32gui.EnableMenuItem(self.hMenu, win32con.SC_CLOSE,
                                    win32con.MF_BYCOMMAND | win32con.MF_ENABLED)
        finally:
            return

    def disable_min_btn(self) -> None:
        """
        disable the minimize button on windows
        :return: None
        """
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) & ~win32con.WS_MINIMIZEBOX)
        finally:
            return

    def enable_min_btn(self) -> None:
        """
        Enable minimize button on windows
        :return: None
        """
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) | win32con.WS_MINIMIZEBOX)
        finally:
            return

    def disable_max_btn(self) -> None:
        """
        Disable maximize button
        :return: None
        """
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)
        finally:
            return

    def enable_max_btn(self) -> None:
        """
        Enable maximize button
        :return: None
        """
        try:
            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE,
                                   win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE) | win32con.WS_MAXIMIZEBOX)
        finally:
            return

    def disable_all(self) -> None:
        """
        disable exit, maximize and minimize button as well as keyboard exit
        :return: None
        """
        self.disable_exit_btn()
        self.disable_max_btn()
        self.disable_min_btn()
        Window.disable_keyboard_exit()
        return

    def enable_all(self) -> None:
        """
        Enable exit, maximize and minimize button as well as keyboard exit
        :return: None
        """
        self.enable_exit_btn()
        self.enable_max_btn()
        self.enable_min_btn()
        Window.enable_keyboard_exit()
        return

    def set_title(self, title: str) -> None:
        """
        Set the new title of the window
        :param title: The new title of the window
        :return: None
        """
        win32gui.SetWindowText(self.hwnd, title)
        return

    def hide(self) -> None:
        """
        Hide the window
        :return: None
        """
        win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)
        return

    def show(self) -> None:
        """
        Show window
        :return: None
        """
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
        return

    def blur_window(self) -> None:
        """
        Apply a nice acrylic blur to the window
        :return: None
        """
        GlobalBlur(self.hwnd)
        return

    def to_foreground(self) -> None:
        """
        Set the foreground window
        :return: None
        """
        win32gui.SetForegroundWindow(self.hwnd)

    def animate_window(self, time: int = 200, flags: Animation = Animation.blend) -> None:
        """
        Set an animation to the window.
        Doesn't work with console window.
        -> Animation.hide in the flags parameters to hide the window.
        -> Default to Show
        :param flags: Window.Animation, flags to animate the window
        :param time: The time it takes to play the animation
        :return: None
        """
        try:
            win32gui.AnimateWindow(self.hwnd, time, flags)
        finally:
            return

    def set_topmost(self) -> None:
        """
        Set the window on top of other's
        :return: None
        """
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, left, top, right-left, bottom-top, 0)

    def disable_resizing(self) -> None:
        """
        Disable resizing the window
        :return: None
        """
        try:
            win32gui.DeleteMenu(self.hMenu, win32con.SC_SIZE, win32con.MF_BYCOMMAND)
        finally:
            return

    def enable_resizing(self) -> None:
        """
        **Unavailable for now**
        Enable resizing the window
        :return: None
        """
        ...

    def center(self) -> None:
        """
        Center the window
        :return: None
        """
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        win32gui.SetWindowPos(self.hwnd,
                              None,
                              int((self.SCREEN_WIDTH-(right-left))/2),
                              int((self.SCREEN_HEIGHT-(bottom-top))/2),
                              right-left,
                              bottom-top,
                              win32con.SWP_NOZORDER
                              )