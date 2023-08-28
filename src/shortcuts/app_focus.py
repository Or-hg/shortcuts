from shortcuts import Expression, WindowMgr
from typing import Any
from win32gui import GetWindowText, GetForegroundWindow, GetClassName
from time import sleep
import threading


SLEEP = 1


class AppFocus(Expression):
    def __init__(self, app_name: str, action: Expression):
        self.app_name = app_name
        self.action = action

    def execute(self, context: Any = None) -> Any:
        """Execute the handle_focus function in a new thread"""
        thread = threading.Thread(target=self.handle_focus, args=(context,))
        thread.start()

    def handle_focus(self, context: Any = None) -> Any:
        """When the app is focused, execute action."""
        while True:
            while self.app_name.lower() not in WindowMgr.get_active_window_process_name().lower():
                sleep(SLEEP)

            self.action.execute(context)

            while self.app_name.lower() in WindowMgr.get_active_window_process_name().lower():
                sleep(SLEEP)