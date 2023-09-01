from shortcuts import Expression, TerminalExpression
from typing import Any
import datetime


class GetSystemTime(Expression):
    def __init__(self, only_time: Expression = TerminalExpression(False)):
        self.only_time = only_time

    def execute(self, context: Any = None) -> Any:
        now = datetime.datetime.now()
        if self.only_time.execute(context):
            return now.time().strftime('%H:%M:%S')
        return now.strftime('%Y-%m-%d %H:%M:%S')
