from shortcuts import ChangeVolume, TerminalExpression, Expression
from typing import Any
import pytest
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


@pytest.mark.parametrize("volume", [TerminalExpression(5),
                                    TerminalExpression("hi")])
def test_validate_volume_valid(volume: Expression):
    ChangeVolume(volume)


@pytest.mark.parametrize("volume", [5, "hi"])
def test_validate_volume_invalid(volume: Any):
    with pytest.raises(TypeError):
        ChangeVolume(volume)


@pytest.mark.parametrize("volume", [5, 100, 0, 45])
def test_execute_valid(volume: int):
    ChangeVolume(TerminalExpression(volume)).execute()
    all_devices = AudioUtilities.GetAllDevices()
    for device in all_devices:
        interface = device.EndpointVolume.QueryInterface(IAudioEndpointVolume)
        actual_volume = interface.GetMasterVolumeLevelScalar()
        assert abs(volume - actual_volume * 100) <= 1


@pytest.mark.parametrize("volume", ["hi", [], None])
def test_execute_invalid_terminal_expression(volume: int):
    with pytest.raises(TypeError):
        ChangeVolume(TerminalExpression(volume)).execute()


@pytest.mark.parametrize("volume", [5, 100, 0, 45])
def test_get_volume(volume: int):
    ChangeVolume(TerminalExpression(volume)).execute()
    assert abs(volume - ChangeVolume.get_volume()) <= 1
