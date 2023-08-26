from shortcuts import Expression
from typing import Any
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import ctypes


MIN_VOLUME = 0
MAX_VOLUME = 100


class ChangeVolume(Expression):
    def __init__(self, volume: Expression):
        ChangeVolume.validate_volume(volume)
        self.volume = volume

    def execute(self, context: Any = None) -> None:
        """
        Change the system volume.

        :param context: execution context. Default is None.
        """
        desired_volume: int = self.volume.execute(context)
        if type(desired_volume) != int:
            raise TypeError("Desired volume must be an integer")
        if desired_volume > MAX_VOLUME or desired_volume < MIN_VOLUME:
            raise ValueError(f"Desired volume must be between {MIN_VOLUME} and {MAX_VOLUME}")
        ChangeVolume.set_volume(desired_volume)

    @staticmethod
    def validate_volume(volume: Expression) -> None:
        """Validate that the volume is an Expression."""
        if not isinstance(volume, Expression):
            raise TypeError("Volume must be an Expression")

    @staticmethod
    def set_volume(volume: int):
        """Set system volume."""

        ctypes.windll.ole32.CoInitialize(0)

        all_devices = AudioUtilities.GetAllDevices()
        for device in all_devices:
            interface = device.EndpointVolume.QueryInterface(IAudioEndpointVolume)
            interface.SetMasterVolumeLevelScalar(volume / 100, None)
