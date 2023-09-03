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
from gui import AddShortcutWindow, FONT, FONT_SIZE, DeleteShortcutWindow, ViewShortcutsWindow


TITLE = "Shortcuts GUI"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_shortcut_button = None
        self.delete_shortcut_button = None
        self.view_shortcuts_button = None
        self.welcome_label = None
        self.init_ui()
        self.add_shortcut_window = None
        self.delete_shortcut_window = None
        self.view_shortcuts_window = None

    def init_ui(self):
        self.setWindowTitle(TITLE)

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height())

        self.create_welcome_label()

        self.create_add_shortcut_button()

        self.create_delete_shortcut_button()

        self.create_view_shortcuts_button()

    def create_welcome_label(self):
        self.welcome_label = QLabel(self)
        font = QFont(FONT, 40)
        font.setBold(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setGeometry(650, 100, 600, 50)
        self.welcome_label.setText("Welcome to Shortcuts!")
        self.welcome_label.adjustSize()

    def create_add_shortcut_button(self):
        self.add_shortcut_button = QPushButton(self)
        self.add_shortcut_button.setFont(QFont(FONT, 20))
        self.add_shortcut_button.setGeometry(400, 300, 200, 50)
        self.add_shortcut_button.setText("Add Shortcut")
        self.add_shortcut_button.clicked.connect(self.on_click_add_shortcut)
        self.add_shortcut_button.adjustSize()

    def create_delete_shortcut_button(self):
        self.delete_shortcut_button = QPushButton(self)
        self.delete_shortcut_button.setFont(QFont(FONT, 20))
        self.delete_shortcut_button.setGeometry(850, 300, 200, 50)
        self.delete_shortcut_button.setText("Delete Shortcut")
        self.delete_shortcut_button.clicked.connect(self.on_click_delete_shortcut)
        self.delete_shortcut_button.adjustSize()

    def create_view_shortcuts_button(self):
        self.view_shortcuts_button = QPushButton(self)
        self.view_shortcuts_button.setFont(QFont(FONT, 20))
        self.view_shortcuts_button.setGeometry(1300, 300, 200, 50)
        self.view_shortcuts_button.setText("View Shortcuts")
        self.view_shortcuts_button.clicked.connect(self.on_click_view_shortcuts)
        self.view_shortcuts_button.adjustSize()

    def on_click_add_shortcut(self):
        self.add_shortcut_window = AddShortcutWindow()
        self.add_shortcut_window.showMaximized()

    def on_click_delete_shortcut(self):
        self.delete_shortcut_window = DeleteShortcutWindow()
        self.delete_shortcut_window.showMaximized()

    def on_click_view_shortcuts(self):
        self.view_shortcuts_window = ViewShortcutsWindow()
        self.view_shortcuts_window.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showMaximized()
    sys.exit(app.exec_())
