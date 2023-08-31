from shortcuts import Expression
from typing import Any
import psutil


class IsAppRunning(Expression):
    def __init__(self, app: Expression):
        self.app = app

    def execute(self, context: Any = None) -> Any:
        """Check if the app is running"""
        processes = (i.name().lower() for i in psutil.process_iter())
        for process in processes:
            if self.app.execute(context).lower() in process:
                return True
        return False
