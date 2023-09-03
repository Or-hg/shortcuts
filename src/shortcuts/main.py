import time

from shortcuts import (DetectAppFocus, TerminalExpression, ChangeVolume, MsgBox,
                       DetectWindowFocus, WhatsappMessage, IsAppRunning, GetBattery,
                       IsComputerPlugged, OpenApp, MusicPlayPause, If, RunFile,
                       While, Not, GetVolume, SetVariable, GetVariable, Wait,
                       Concatenate, Execute, GetSystemTime, TakeScreenshot, ExpressionsBlock,
                       And, Or, IsWindowOpen, DetectScreenshotTaken, AddKeyboardShortcut)

VOLUME = 10
SPOTIFY = 'spotify'
YOUTUBE = 'youtube'
WAS_SPOTIFY_PLAYING = 'was spotify playing'
WHATSAPP = "whatsapp"

time.sleep(3)

# When switching to spotify, change volume
DetectAppFocus(TerminalExpression(SPOTIFY), ChangeVolume(TerminalExpression(VOLUME))).execute()

# When switching to youtube, change volume
DetectWindowFocus(TerminalExpression(YOUTUBE), ChangeVolume(TerminalExpression(VOLUME))).execute()

# When switching to youtube, if spotify is playing music, stop it.
DetectWindowFocus(TerminalExpression(YOUTUBE),
                  If(And(IsAppRunning(TerminalExpression(SPOTIFY)), Not(IsWindowOpen(TerminalExpression(SPOTIFY)))), MusicPlayPause())).execute()

# When taking a screenshot - open whatsapp
DetectScreenshotTaken(OpenApp(TerminalExpression(WHATSAPP))).execute()