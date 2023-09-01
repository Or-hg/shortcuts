from shortcuts import Expression
from typing import Any


class Not(Expression):
    def __init__(self, boolean: Expression):
        self.boolean = boolean

    def execute(self, context: Any = None) -> Any:
        return not self.boolean.execute(context)