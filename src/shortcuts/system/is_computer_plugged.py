from shortcuts import Expression
from typing import Any
import psutil


class IsComputerPlugged(Expression):
    def execute(self, context: Any = None) -> Any:
        """Check if the computer is plugged in"""
        return psutil.sensors_battery().power_plugged