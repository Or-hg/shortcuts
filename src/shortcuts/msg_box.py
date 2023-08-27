from shortcuts import Expression
from typing import Any
from easygui import msgbox


TITLE = "shortcut message"


class MsgBox(Expression):
    """Create a popup message box."""

    def __init__(self, msg: Expression):
        self.msg = msg

    def execute(self, context: Any = None) -> Any:
        """Create the message box."""
        msgbox(self.msg.execute(context), title=TITLE)
