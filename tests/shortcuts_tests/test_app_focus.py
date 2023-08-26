from shortcuts import AppFocus, ChangeVolume, TerminalExpression


def test_app_focus():
    AppFocus("spotify", ChangeVolume(TerminalExpression(50))).execute()

