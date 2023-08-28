import time

from shortcuts import AppFocus, TerminalExpression, ChangeVolume, MsgBox, OpenApp, CloseApp, If

VOLUME = 12

time.sleep(3)

# AppFocus("spotify", ChangeVolume(TerminalExpression(VOLUME))).execute()

If(TerminalExpression(True), MsgBox(TerminalExpression("hi"))).execute()
