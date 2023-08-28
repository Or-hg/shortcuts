import time

from shortcuts import AppFocus, TerminalExpression, ChangeVolume, MsgBox, OpenApp, CloseApp

VOLUME = 12

time.sleep(3)

# AppFocus("spotify", ChangeVolume(TerminalExpression(VOLUME))).execute()

OpenApp(TerminalExpression("file explorer")).execute()

time.sleep(5)

CloseApp(TerminalExpression("file explorer")).execute()
