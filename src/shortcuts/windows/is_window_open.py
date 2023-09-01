from shortcuts import Expression
from typing import Any
from pywinauto import Desktop


class IsWindowOpen(Expression):
    def __init__(self, window_name: Expression):
        self.window_name = window_name

    def execute(self, context: Any = None) -> Any:
        """Check if the window is open."""
        windows = Desktop(backend="uia").windows()
        window = self.window_name.execute(context).lower()
        for open_window_name in [w.window_text() for w in windows]:
            if window in open_window_name.lower():
                return True

        return False
