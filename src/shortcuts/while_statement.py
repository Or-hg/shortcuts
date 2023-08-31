from shortcuts import Expression, TerminalExpression
from typing import Any
from threading import Thread
import time


class While(Expression):
    def __init__(self, condition: Expression, action: Expression, sleep: Expression = TerminalExpression(1)):
        self.condition = condition
        self.action = action
        self.sleep = sleep

    def execute(self, context: Any = None) -> Any:
        """Execute the loop function in a different thread."""
        thread = Thread(target=self.loop, args=(context,))
        thread.start()

    def loop(self, context: Any = None):
        """Execute while loop."""
        sleep = self.sleep.execute(context)
        while self.condition.execute(context):
            self.action.execute(context)
            time.sleep(sleep)
