import keyboard
from shortcuts import Expression
from typing import Any
from threading import Thread


class AddKeyboardShortcut(Expression):
    def __init__(self, keys: Expression, action: Expression):
        self.keys = keys
        self.action = action

    def execute(self, context: Any = None) -> Any:
        """Execute the wait_for_keypress function in a separate thread."""
        thread = Thread(target=self.wait_for_keypress, args=(context,))
        thread.start()
        return thread

    def wait_for_keypress(self, context: Any):
        """Wait for keys and execute action."""
        keys = self.keys.execute(context)
        while True:
            keyboard.wait(keys)
            self.action.execute(context)
