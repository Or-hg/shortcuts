from shortcuts import Expression
from typing import Any


class Concatenate(Expression):
    """
    Concatenate the strings of two objects.
    for example: Concatenate(TerminalExpression(1),TerminalExpression(2)).execute() == '12',
    Concatenate(TerminalExpression('a'),TerminalExpression('b')).execute() == 'ab'
    """
    def __init__(self, string1: Expression, string2: Expression):
        self.string1 = string1
        self.string2 = string2

    def execute(self, context: Any = None) -> Any:
        return f"{self.string1.execute(context)}{self.string2.execute(context)}"
