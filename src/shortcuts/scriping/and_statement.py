from shortcuts import Expression
from typing import Any


class And(Expression):
    def __init__(self, first: Expression, second: Expression):
        self.first = first
        self.second = second

    def execute(self, context: Any = None) -> Any:
        return self.first.execute(context) and self.second.execute(context)
