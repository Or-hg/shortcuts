from shortcuts import Expression
import AppOpener
from typing import Any


class CloseApp(Expression):
    def __init__(self, app):
        self.app = app

    def execute(self, context: Any = None) -> Any:
        """Close the app"""
        AppOpener.close(self.app.execute(context))
