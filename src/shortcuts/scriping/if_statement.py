from shortcuts import Expression
from typing import Any


class If(Expression):
    def __init__(self, condition: Expression, action: Expression, else_action: Expression = None):
        self.condition = condition
        self.action = action
        self.else_action = else_action

    def execute(self, context: Any = None) -> Any:
        """Execute the if statement"""
        if self.condition.execute(context):
            self.action.execute(context)
        else:
            if self.else_action is not None:
                self.else_action.execute(context)