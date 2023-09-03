from shortcuts import Expression
import AppOpener
from typing import Any


class OpenApp(Expression):
    def __init__(self, app: Expression):
        self.app = app

    def execute(self, context: Any = None) -> Any:
        """Open the app"""
        app = self.app.execute(context)
        if not isinstance(app, str):
            raise TypeError("app must be a string")

        AppOpener.open(app)
