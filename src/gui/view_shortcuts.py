import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QListWidget,
                             QWidget, QPushButton, QAction, QGridLayout,
                             QLineEdit, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import inspect
from shortcuts import *
from functools import partial
from typing import List

from gui.add_shortcut import FILE


SHORTCUTS = "shortcuts"
TITLE = "Add shortcut"
FONT = "Ariel"
FONT_SIZE = 10
SAVE_STR = "Save"


class ViewShortcuts(QMainWindow):

    def __init__(self):
        super().__init__()
        self.shortcuts_list = None
        self.shortcuts_dict = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(TITLE)

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height())

        # get shortcuts list
        self.shortcuts_dict = self.get_shortcuts()

        # Create shortcuts list
        self.create_shortcuts_list()
        self.shortcuts_list.clicked.connect(self.on_click_list)

    def create_shortcuts_list(self):
        self.shortcuts_list = QListWidget()
        for name, shortcut in self.shortcuts_dict.items():
            self.shortcuts_list.addItem(name)

        self.shortcuts_list.setGeometry(650, 200, 600, 600)

        self.layout().addWidget(self.shortcuts_list)

    def on_click_list(self, qmodelindex):
        item = self.shortcuts_list.currentItem()
        QMessageBox.information(self, "Info", self.shortcuts_dict[item.text()])

    @staticmethod
    def get_shortcuts():
        with open(FILE) as f:
            lines = f.read()

        shortcuts_dict = {}

        for line in lines.split("# name - "):
            if "\n" in line:
                name = line[:line.index("\n")]
                shortcut = line[line.index("\n") + 1: -2]

                shortcuts_dict[name] = shortcut

        return shortcuts_dict


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewShortcuts()
    ex.showMaximized()
    sys.exit(app.exec_())
