from shortcuts import Expression, WindowMgr
from typing import Any
from time import sleep
import threading


SLEEP = 1


class WindowFocus(Expression):
    def __init__(self, window_name: Expression, action: Expression, blur_action: Expression = None):
        self.window_name = window_name
        self.action = action
        self.blur_action = blur_action

    def execute(self, context: Any = None) -> Any:
        """Execute the handle_focus function in a new thread"""
        thread = threading.Thread(target=self.handle_focus, args=(context,))
        thread.start()

    def handle_focus(self, context: Any = None) -> Any:
        """When the app is focused, execute action."""
        window = self.window_name.execute(context)
        while True:
            while window.lower() not in WindowMgr.get_active_window_name().lower():
                sleep(SLEEP)

            if self.action is not None:
                self.action.execute(context)

            while window.lower() in WindowMgr.get_active_window_name().lower():
                sleep(SLEEP)

            if self.blur_action is not None:
                self.blur_action.execute(context)
