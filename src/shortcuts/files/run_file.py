from shortcuts import Expression
from typing import Any
import subprocess


class RunFile(Expression):
    def __init__(self, args_list: Expression):
        """
        Constructor.
        :param args_list: the result of self.args_list.execute(context) should be something like:
        ["python", "scriptpath\\script.py"] or ["script.exe"]
        """
        self.args_list = args_list

    def execute(self, context: Any = None) -> Any:
        """Run the file"""
        args = self.args_list.execute(context)
        if not isinstance(args, list):
            raise TypeError("args_list must be a string")

        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("args_list must be a list of strings")

        subprocess.run(args, shell=True)
