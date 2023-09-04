import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QWidget, QPushButton, QAction,
                             QLineEdit, QMessageBox, QLabel, QPlainTextEdit )
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import inspect
from shortcuts import *
from functools import partial
from typing import List


SHORTCUTS = "shortcuts"
TITLE = "Add shortcut"
FONT = "Ariel"
FONT_SIZE = 10
SAVE_STR = "Save"
FILE = r"C:\Users\OR\Desktop\test.py"


class AddShortcutWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.shortcut_box = None
        self.save_button = None
        self.description_box = None
        self.name_box = None
        self.init_ui(AddShortcutWindow.get_actions())

    def init_ui(self, actions: List[str]):
        self.setWindowTitle(TITLE)

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height())

        # Create name box
        name_box_top, name_box_height = self.create_name_box()

        # Create description box
        description_box_top, description_box_height = self.create_description_box(name_box_top, name_box_height)

        # Create shortcut box
        shortcuts_box_top, shortcuts_box_height = self.create_shortcut_box(description_box_top, description_box_height)

        last_action_button_top = self.create_action_buttons(actions, 50, shortcuts_box_top + shortcuts_box_height + 30)

        # Create a save button
        self.create_save_button(last_action_button_top)

    def create_name_box(self):
        name_box_top = 20
        name_box_height = 60

        self.name_box = QPlainTextEdit(self)
        self.name_box.setPlaceholderText("Name")
        self.name_box.move(20, name_box_top)
        self.name_box.resize(self.frameGeometry().width() - 40, name_box_height)
        self.name_box.setFont(QFont(FONT, FONT_SIZE))

        return name_box_top, name_box_height

    def create_description_box(self, name_box_top, name_box_height):
        description_box_top = name_box_height + name_box_top + 30
        description_box_height = name_box_height

        self.description_box = QPlainTextEdit(self)
        self.description_box.setPlaceholderText("Description")
        self.description_box.move(20, description_box_top)
        self.description_box.resize(self.frameGeometry().width() - 40, description_box_height)
        self.description_box.setFont(QFont(FONT, FONT_SIZE))

        return description_box_top, description_box_height

    def create_shortcut_box(self, description_box_top, description_box_height):
        shortcuts_box_top = description_box_height + description_box_top + 30
        shortcuts_box_height = description_box_height

        self.shortcut_box = QPlainTextEdit(self)
        self.shortcut_box.setPlaceholderText("Shortcut")
        self.shortcut_box.move(20, shortcuts_box_top)
        self.shortcut_box.resize(self.frameGeometry().width() - 40, shortcuts_box_height)
        self.shortcut_box.setFont(QFont(FONT, FONT_SIZE))

        return shortcuts_box_top, shortcuts_box_height

    def create_save_button(self, last_action_button_top):
        self.save_button = QPushButton(SAVE_STR, self)
        self.save_button.setFont(QFont(FONT, FONT_SIZE))
        self.save_button.setGeometry(50, last_action_button_top + 200, 100, 50)
        self.save_button.clicked.connect(self.on_click_save)
        self.save_button.adjustSize()

    def create_action_buttons(self, actions: List[str], left, top):
        width = 200
        height = 50
        count = 0
        space_width = 20
        space_length = 10
        curr_left = left
        for button_name in actions:
            button = QPushButton(button_name, self)
            button.setFont(QFont('Arial', 10))
            button.setGeometry(curr_left, top, width, height)
            button.adjustSize()

            def insert_action(name):
                parameters_dict = inspect.signature(eval(name).__init__).parameters.keys()
                parameters = ", ".join(parameters_dict)
                parameters = parameters.replace("self, ", "")
                self.shortcut_box.insertPlainText(f"{name}({parameters})")

            button.clicked.connect(partial(insert_action, button_name))
            curr_left += width + space_width
            count += 1
            if curr_left + width > self.frameGeometry().width():
                curr_left = left
                top += height + space_length

        return top

    @pyqtSlot()
    def on_click_save(self):
        name = self.name_box.toPlainText()
        if name == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please insert a name')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        with open(FILE) as f:
            lines = f.readlines()

        if f"# name - {name}\n" in lines:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(f"Name '{name}' is taken")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        shortcut = self.shortcut_box.toPlainText()
        if shortcut == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(f"Please add a shortcut")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        if "from shortcuts import *\n" not in lines:
            with open(FILE, 'a') as f:
                f.write("from shortcuts import *\n")
                f.write("\n")
                f.write("\n")

        description = self.description_box.toPlainText()
        description_lines = description.split("\n")

        with open(FILE, 'a') as f:
            f.write(f"# name - {name}\n")
            if len(description_lines) != 0:
                for description_line in description_lines:
                    if description_line != "":
                        f.write(f"# {description_line}\n")
            f.write(f"{shortcut}.execute()\n\n")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"shortcut '{name}' added")
        msg.exec_()

    @staticmethod
    def get_actions() -> List[str]:
        actions = []
        for name, obj in inspect.getmembers(sys.modules[SHORTCUTS]):
            if inspect.isclass(obj):
                actions.append(obj.__name__)

        actions.remove('WindowMgr')
        actions.remove('Expression')

        actions.sort()

        return actions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddShortcutWindow()
    ex.showMaximized()
    sys.exit(app.exec_())
