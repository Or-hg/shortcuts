import pytest
from typing import Any
from shortcuts import TerminalExpression


@pytest.mark.parametrize("data", ["hi",
                                  None,
                                  5,
                                  -5,
                                  [1,2,3]])
def test_execute(data: Any) -> None:
    assert TerminalExpression(data).execute() == data