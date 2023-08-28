from shortcuts import Expression
from typing import Any
from easygui import msgbox
from threading import Thread


TITLE = "shortcut message"


class MsgBox(Expression):
    """Create a popup message box."""

    def __init__(self, msg: Expression):
        self.msg = msg

    def execute(self, context: Any = None) -> Any:
        """Execute the create_msg_box function in a new thread"""
        thread = Thread(target=self.create_msg_box, args=(context,))
        thread.start()

    def create_msg_box(self, context: Any = None) -> Any:
        """Create the message box."""
        msgbox(self.msg.execute(context), title=TITLE)
