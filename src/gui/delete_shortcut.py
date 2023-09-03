import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QWidget, QPushButton, QAction,
                             QLineEdit, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import inspect
from shortcuts import *
from functools import partial
from typing import List

from gui.add_shortcut import FILE

SHORTCUTS = "shortcuts"
TITLE = "Delete shortcut"
FONT = "Ariel"
FONT_SIZE = 10
SAVE_STR = "Save"


class DeleteShortcut(QMainWindow):

    def __init__(self):
        super().__init__()
        self.delete_button = None
        self.name_box = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(TITLE)

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height())

        # Create name box
        name_box_top, name_box_height = self.create_name_box()

        # Create a delete button
        self.create_delete_button(name_box_top + name_box_height + 50)

    def create_name_box(self):
        name_box_top = 20
        name_box_height = 60

        self.name_box = QLineEdit(self)
        self.name_box.setPlaceholderText("Name")
        self.name_box.move(20, name_box_top)
        self.name_box.resize(self.frameGeometry().width() - 40, name_box_height)
        self.name_box.setFont(QFont(FONT, FONT_SIZE))

        return name_box_top, name_box_height

    def create_delete_button(self, name_top):
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setFont(QFont(FONT, FONT_SIZE))
        self.delete_button.setGeometry(50, name_top + 100, 100, 50)
        self.delete_button.clicked.connect(self.on_click_delete)

    @pyqtSlot()
    def on_click_delete(self):
        shortcut_to_delete = self.name_box.text()

        if not DeleteShortcut.assert_name_not_empty(shortcut_to_delete):
            return

        with open(FILE) as f:
            lines = f.readlines()

        if not DeleteShortcut.assert_shortcut_exits(shortcut_to_delete, lines):
            return

        lines_to_delete = []
        in_shortcut_to_delete = False
        shortcut_name_line = f"# name - {shortcut_to_delete}\n"
        for line in lines:
            if in_shortcut_to_delete:
                if "# name - " in line:
                    in_shortcut_to_delete = False
                else:
                    lines_to_delete.append(line)
            if line == shortcut_name_line:
                in_shortcut_to_delete = True
                lines_to_delete.append(line)

        for line in lines_to_delete:
            lines.remove(line)

        with open(FILE, 'w') as f:
            f.writelines(lines)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Shortcut '{shortcut_to_delete}' deleted")
        msg.exec_()

    @staticmethod
    def assert_name_not_empty(name_text):
        if name_text == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please insert a name')
            msg.setWindowTitle("Error")
            msg.exec_()
            return False
        return True

    @staticmethod
    def assert_shortcut_exits(shortcut_name, lines):
        if f"# name - {shortcut_name}\n" not in lines:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(f"Shortcut '{shortcut_name}' doesn't exist")
            msg.setWindowTitle("Error")
            msg.exec_()
            return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeleteShortcut()
    ex.showMaximized()
    sys.exit(app.exec_())
