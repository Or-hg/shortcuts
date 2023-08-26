from shortcuts import Expression
from typing import Any


class TerminalExpression(Expression):
    """Class representing a terminal expression."""

    def __init__(self, data: Any):
        self.data = data

    def execute(self, context: Any = None) -> Any:
        """
        Return the data.

        :param context: execution context. Default is None.
        """
        return self.data
