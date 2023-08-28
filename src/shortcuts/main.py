import time

from shortcuts import AppFocus, TerminalExpression, ChangeVolume, MsgBox

time.sleep(3)

AppFocus("spotify", MsgBox(TerminalExpression(0))).execute()
