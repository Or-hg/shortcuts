from shortcuts import Expression
from typing import Any


VARIABLES = {}


class SetVariable(Expression):
    def __init__(self, name: Expression, value: Expression):
        self.name = name
        self.value = value

    def execute(self, context: Any = None) -> Any:
        VARIABLES[self.name.execute(context)] = self.value.execute(context)