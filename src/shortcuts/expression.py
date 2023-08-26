from abc import ABC, abstractmethod
from typing import Any


class Expression(ABC):
    """Abstract class representing an expression."""

    @abstractmethod
    def execute(self, context: Any = None) -> Any:
        """
        Execute the expression.

        :param context: execution context. Default is None.
        """
        pass
