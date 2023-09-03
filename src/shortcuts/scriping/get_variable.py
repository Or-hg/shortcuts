from shortcuts import Expression, VARIABLES
from typing import Any


class GetVariable(Expression):
    def __init__(self, name: Expression):
        self.name = name

    def execute(self, context: Any = None) -> Any:
        name = self.name.execute(context)
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        return VARIABLES[name]
