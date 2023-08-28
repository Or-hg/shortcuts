from shortcuts import Expression
import AppOpener
from typing import Any


class OpenApp(Expression):
    def __init__(self, app: Expression):
        self.app = app

    def execute(self, context: Any = None) -> Any:
        """Open the app"""
        AppOpener.open(self.app.execute(context))
