from shortcuts import DetectAppFocus, ChangeVolume, TerminalExpression, WindowMgr, MsgBox, MSG_BOX_TITLE
from time import sleep


def test_app_focus_change_volume():
    app = "Spotify"
    ChangeVolume(TerminalExpression(0)).execute()
    vol = 10
    DetectAppFocus(app, ChangeVolume(TerminalExpression(vol))).execute()
    WindowMgr().find_window_by_name(app).set_foreground()
    sleep(2)
    assert abs(ChangeVolume.get_volume() - vol) <= 1


def test_app_focus_msg_box():
    app = "Spotify"
    DetectAppFocus(app, MsgBox(TerminalExpression("hi"))).execute()
    WindowMgr().find_window_by_name(app).set_foreground()
    sleep(2)
    msg_box = WindowMgr().find_window_by_name(MSG_BOX_TITLE)
    msg_box.set_foreground()
    msg_box.close_window()