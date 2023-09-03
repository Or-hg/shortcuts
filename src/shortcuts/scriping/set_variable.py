from shortcuts import Expression
from typing import Any


VARIABLES = {}


class SetVariable(Expression):
    def __init__(self, name: Expression, value: Expression):
        self.name = name
        self.value = value

    def execute(self, context: Any = None) -> Any:
        name = self.name.execute(context)
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        VARIABLES[name] = self.value.execute(context)