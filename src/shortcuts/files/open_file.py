from shortcuts import Expression
from typing import Any
from os import startfile


class OpenFile(Expression):
    def __init__(self, file: Expression):
        self.file = file

    def execute(self, context: Any = None) -> Any:
        """Open the file in its default app"""
        file = self.file.execute(context)
        if not isinstance(file, str):
            raise TypeError("file must be a string")

        startfile(file)
