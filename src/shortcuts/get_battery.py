from shortcuts import Expression
from typing import Any
import psutil


class GetBattery(Expression):
    def execute(self, context: Any = None) -> Any:
        """Get computer battery percent"""
        return psutil.sensors_battery().percent
