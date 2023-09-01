from shortcuts import Expression, TerminalExpression, Concatenate, GetSystemTime
from typing import Any
import pyautogui


SCREENSHOTS_FOLDER = r"C:\Users\OR\Pictures\Screenshots"


class TakeScreenshot(Expression):
    def __init__(self, location: Expression = TerminalExpression(SCREENSHOTS_FOLDER),
                 name: Expression = Concatenate(TerminalExpression("Shortcuts_screenshot_"), GetSystemTime()),
                 extension: Expression = TerminalExpression('png')):
        self.location = location
        self.name = name
        self.extension = extension

    def execute(self, context: Any = None) -> Any:
        """Take a screenshot."""
        screenshot = pyautogui.screenshot()
        full_path = rf"{self.location.execute(context)}\{self.name.execute(context)}.{self.extension.execute(context)}"
        screenshot.save(full_path)
