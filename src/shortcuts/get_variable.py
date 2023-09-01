from shortcuts import Expression, VARIABLES
from typing import Any


class GetVariable(Expression):
    def __init__(self, name: Expression):
        self.name = name

    def execute(self, context: Any = None) -> Any:
        return VARIABLES[self.name.execute(context)]
