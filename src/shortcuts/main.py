import time

from shortcuts import (AppFocus, TerminalExpression, ChangeVolume, MsgBox,
                       WindowFocus, WhatsappMessage, IsAppRunning, GetBattery,
                       IsComputerPlugged, OpenApp, MusicPlayPause, If)

VOLUME = 10

time.sleep(3)

AppFocus(TerminalExpression("spotify"), ChangeVolume(TerminalExpression(VOLUME))).execute()

WindowFocus(TerminalExpression("youtube"), ChangeVolume(TerminalExpression(VOLUME))).execute()

WindowFocus(TerminalExpression("youtube"), If(IsAppRunning(TerminalExpression("spotify")), MusicPlayPause())).execute()