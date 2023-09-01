from shortcuts import Expression
from typing import Any
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


class GetVolume(Expression):
    def execute(self, context: Any = None) -> Any:
        """Get the system volume."""
        ctypes.windll.ole32.CoInitialize(0)

        speakers = AudioUtilities.GetSpeakers()
        interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        return int(volume.GetMasterVolumeLevelScalar() * 100)
