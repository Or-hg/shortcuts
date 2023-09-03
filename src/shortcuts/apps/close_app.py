from shortcuts import Expression
import AppOpener
from typing import Any


class CloseApp(Expression):
    def __init__(self, app):
        self.app = app

    def execute(self, context: Any = None) -> Any:
        """Close the app"""
        app = self.app.execute(context)
        if not isinstance(app, str):
            raise TypeError("app must be a string")
        AppOpener.close(app)
