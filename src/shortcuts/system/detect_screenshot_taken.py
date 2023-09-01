from shortcuts import Expression
from typing import Any
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .take_screenshot import SCREENSHOTS_FOLDER


class DetectScreenshotTaken(Expression):
    def __init__(self, action: Expression):
        self.action = action

    def execute(self, context: Any = None) -> Any:
        class ScreenshotHandler(FileSystemEventHandler):
            def __init__(self, outer_instance: DetectScreenshotTaken):
                self.outer_instance = outer_instance
                super().__init__()

            def on_created(self, event):
                self.outer_instance.action.execute(context)

        observer = Observer()
        event_handler = ScreenshotHandler(self)  # create event handler
        # set observer to use created handler in directory
        observer.schedule(event_handler, path=SCREENSHOTS_FOLDER)
        observer.start()
        observer.join()
