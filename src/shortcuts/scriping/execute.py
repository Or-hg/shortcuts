from shortcuts import Expression
from typing import Any


class Execute(Expression):
    """Execute a python command."""
    def __init__(self, command: Expression):
        self.command = command

    def execute(self, context: Any = None) -> Any:
        return exec(self.command.execute(context))
