from pyautogui import press
from shortcuts import Expression
from typing import Any


PLAYPAUSE = "playpause"


class MusicPlayPause(Expression):
    def execute(self, context: Any = None) -> Any:
        """Play or pause the music"""
        press(PLAYPAUSE)
