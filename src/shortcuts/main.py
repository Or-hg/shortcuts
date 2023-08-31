import time

from shortcuts import (AppFocus, TerminalExpression, ChangeVolume, MsgBox,
                       WindowFocus, WhatsappMessage, IsAppRunning, GetBattery,
                       IsComputerPlugged)

VOLUME = 12

time.sleep(3)

AppFocus("spotify", ChangeVolume(TerminalExpression(VOLUME))).execute()

WindowFocus("youtube", ChangeVolume(TerminalExpression(VOLUME))).execute()
