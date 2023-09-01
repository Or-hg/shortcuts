from shortcuts import Expression
from typing import Any
from threading import Thread


class Wait(Expression):
    def __init__(self, wait_for: Expression):
        self.wait_for = wait_for

    def execute(self, context: Any = None) -> Any:
        """Execute self.wait_for and wait for it to finish."""
        result = self.wait_for.execute(context)
        if isinstance(result, Thread):
            result.join()
