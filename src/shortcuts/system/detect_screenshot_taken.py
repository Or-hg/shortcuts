import time

from shortcuts import Expression
from typing import Any
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .take_screenshot import SCREENSHOTS_FOLDER
from threading import Thread
import keyboard


PRTSCN = "prtscn"


class DetectScreenshotTaken(Expression):
    """
    When taking a screenshot, execute action.
    DISCLAIMER!!!!!! - this works only for screenshots taken by the snipping tool or the 'prtscn' key.
    DISCLAIMER!!!!!! - this works with the snipping tool only if your screenshots folder is 'SCREENSHOTS_FOLDER' (default).
    """
    def __init__(self, action: Expression):
        self.action = action

    def execute(self, context: Any = None) -> Any:
        """Execute the run_threads function in a separate thread."""
        screenshots_listeners = Thread(target=self.run_threads, args=(context,))
        screenshots_listeners.start()
        return screenshots_listeners

    def run_threads(self, context: Any = None):
        """Execute the two listeners in two threads."""
        screenshot_folder_watcher = Thread(target=self.screenshots_folder_watcher, args=(context,))
        screenshot_folder_watcher.start()
        print_screen_listener = Thread(target=self.print_screen_listener, args=(context,))
        print_screen_listener.start()
        screenshot_folder_watcher.join()
        print_screen_listener.join()

    def print_screen_listener(self, context):
        """When the PRTSCN key is pressed, execute action."""
        while True:
            keyboard.wait(PRTSCN)
            self.action.execute(context)

    def screenshots_folder_watcher(self, context):
        """
        When a file is added to SCREENSHOTS_FOLDER, execute action.
        This is the default screenshots folder for the snipping tool.
        """
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