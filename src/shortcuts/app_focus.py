from shortcuts import Expression
from typing import Any
from win32gui import GetWindowText, GetForegroundWindow
from time import sleep


SLEEP = 1


class AppFocus(Expression):
    def __init__(self, app_name: str, action: Expression):
        self.app_name = app_name
        self.action = action

    def execute(self, context: Any = None) -> Any:
        """When the app is focused, execute action."""
        while True:
            while self.app_name.lower() not in GetWindowText(GetForegroundWindow()).lower():
                sleep(SLEEP)

            self.action.execute(context)

            while self.app_name.lower() in GetWindowText(GetForegroundWindow()).lower():
                sleep(SLEEP)
