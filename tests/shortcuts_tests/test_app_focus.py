from shortcuts import AppFocus, ChangeVolume, TerminalExpression


def test_app_focus_change_volume():
    AppFocus("spotify", ChangeVolume(TerminalExpression(50))).execute()


