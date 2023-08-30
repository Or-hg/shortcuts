from pywinauto import Application
from typing import Any
from time import sleep
from shortcuts import Expression


SLEEP = 1


class WhatsappMessage(Expression):
    """Send whatsapp message"""
    def __init__(self, chat: Expression, message: Expression):
        self.chat = chat
        self.message = message

    def execute(self, context: Any = None) -> Any:
        """Send whatsapp message"""
        app = Application().connect(title_re=".*WhatsApp*")

        main_dlg = app.WhatsApp

        # main_dlg.print_control_identifiers()

        sleep(SLEEP)
        main_dlg.type_keys('^(f)')
        sleep(SLEEP)
        main_dlg.type_keys(self.chat.execute(context))
        sleep(SLEEP)
        main_dlg.type_keys("{TAB}")
        sleep(SLEEP)
        main_dlg.type_keys("{ENTER}")
        sleep(SLEEP)
        main_dlg.type_keys(self.message.execute(context), with_spaces=True, with_newlines=True, with_tabs=True)
        sleep(SLEEP)
        main_dlg.type_keys("{ENTER}")