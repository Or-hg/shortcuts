import time

from shortcuts import (DetectAppFocus, TerminalExpression, ChangeVolume, MsgBox,
                       DetectWindowFocus, WhatsappMessage, IsAppRunning, GetBattery,
                       IsComputerPlugged, OpenApp, MusicPlayPause, If, RunFile,
                       While, Not, GetVolume, SetVariable, GetVariable, Wait,
                       Concatenate, Execute, GetSystemTime, TakeScreenshot, ExpressionsBlock,
                       And, Or)

VOLUME = 10

time.sleep(3)

DetectAppFocus(TerminalExpression("spotify"), ChangeVolume(TerminalExpression(VOLUME))).execute()

DetectWindowFocus(TerminalExpression("youtube"), ChangeVolume(TerminalExpression(VOLUME))).execute()

DetectWindowFocus(TerminalExpression("youtube"), If(IsAppRunning(TerminalExpression("spotify")), MusicPlayPause()),
                  If(IsAppRunning(TerminalExpression("spotify")), MusicPlayPause())).execute()
