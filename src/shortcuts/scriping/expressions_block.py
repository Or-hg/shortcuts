from shortcuts import Expression
from typing import Any, List


class ExpressionsBlock(Expression):
    def __init__(self, expressions: List[Expression]):
        self.expressions = expressions

    def execute(self, context: Any = None) -> Any:
        for expression in self.expressions:
            expression.execute(context)
