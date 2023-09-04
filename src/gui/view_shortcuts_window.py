import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidget, QTableWidgetItem,
                             QWidget, QPushButton, QAction, QGridLayout,
                             QLineEdit, QMessageBox, QLabel, QVBoxLayout, QAbstractItemView)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import inspect
from shortcuts import *
from functools import partial
from typing import List
from gui import AddShortcutWindow

from gui.add_shortcut_window import FILE


SHORTCUTS = "shortcuts"
TITLE = "Add shortcut"
FONT = "Ariel"
FONT_SIZE = 10
SAVE_STR = "Save"


class ViewShortcutsWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.delete_shortcut_button = None
        self.shortcuts_table = None
        self.shortcuts_dict = None
        self.add_shortcut_button = None
        self.add_shortcut_window = None
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(TITLE)

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height())

        # Create shortcuts table
        self.create_shortcuts_table()

        # Create add shortcut button
        self.create_add_shortcut_button()

        # Create refresh button
        self.create_refresh_button()

        self.create_delete_shortcut_button()
        self.delete_shortcut_button.hide()

    def create_shortcuts_table(self):
        # get shortcuts list
        self.shortcuts_dict = self.get_shortcuts()

        self.shortcuts_table = QTableWidget(self)
        self.setCentralWidget(self.shortcuts_table)

        self.shortcuts_table.setColumnCount(3)
        self.shortcuts_table.setRowCount(len(self.shortcuts_dict))

        self.shortcuts_table.setHorizontalHeaderLabels(["name", "description", "shortcut"])

        self.shortcuts_table.setFont(QFont('Ariel', 10))

        x = self.size().width()
        y = self.size().height()

        self.shortcuts_table.setGeometry(100, 50, self.frameGeometry().width() - 200,
                                         self.frameGeometry().height() - 400)

        row = 0
        for name, (description, shortcut) in self.shortcuts_dict.items():
            self.shortcuts_table.setItem(row, 0, QTableWidgetItem(name))
            self.shortcuts_table.setItem(row, 1, QTableWidgetItem(description))
            self.shortcuts_table.setItem(row, 2, QTableWidgetItem(shortcut))
            row += 1

        self.shortcuts_table.resizeRowsToContents()
        self.shortcuts_table.resizeColumnsToContents()
        self.shortcuts_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.shortcuts_table.clicked.connect(self.on_table_selection_changed)
        self.shortcuts_table.selectionModel().selectionChanged.connect(self.on_table_selection_changed)
        self.layout.addWidget(self.shortcuts_table)

    def on_table_selection_changed(self, selected, deselected):
        if selected.count() > 0:
            self.delete_shortcut_button.show()
        else:
            self.delete_shortcut_button.hide()

    def create_delete_shortcut_button(self):
        self.delete_shortcut_button = QPushButton(self)
        self.delete_shortcut_button.setFont(QFont(FONT, 15))
        self.delete_shortcut_button.setGeometry(1000, self.frameGeometry().height() - 300, 200, 50)
        self.delete_shortcut_button.setText("Delete shortcut")
        self.delete_shortcut_button.clicked.connect(self.on_click_delete_shortcut)
        self.delete_shortcut_button.adjustSize()

    def on_click_delete_shortcut(self):
        pass

    def create_add_shortcut_button(self):
        self.add_shortcut_button = QPushButton(self)
        self.add_shortcut_button.setFont(QFont(FONT, 15))
        self.add_shortcut_button.setGeometry(100, self.frameGeometry().height() - 300, 200, 50)
        self.add_shortcut_button.setText("Add shortcut")
        self.add_shortcut_button.clicked.connect(self.on_click_add_shortcut)
        self.add_shortcut_button.adjustSize()

    def on_click_add_shortcut(self):
        self.add_shortcut_window = AddShortcutWindow()
        self.add_shortcut_window.showMaximized()

    def create_refresh_button(self):
        self.add_shortcut_button = QPushButton(self)
        self.add_shortcut_button.setFont(QFont(FONT, 15))
        self.add_shortcut_button.setGeometry(500, self.frameGeometry().height() - 300, 200, 50)
        self.add_shortcut_button.setText("Refresh")
        self.add_shortcut_button.clicked.connect(self.on_click_refresh)
        self.add_shortcut_button.adjustSize()

    def on_click_refresh(self):
        self.layout.removeWidget(self.shortcuts_table)
        self.create_shortcuts_table()

    @staticmethod
    def get_shortcuts():
        with open(FILE) as f:
            lines = f.readlines()

        shortcuts_dict = {}

        i = 0
        while i < len(lines):
            line = lines[i].lstrip("\n").lstrip()
            if "# name - " not in line:
                i += 1
                continue

            name = line.lstrip("# name - ")[::-1].lstrip("\n")[::-1]
            i += 1

            line = lines[i].lstrip("\n").lstrip()
            description = ""
            while line.startswith("#"):
                description += line.lstrip("#").lstrip()
                if i == len(lines) - 1:
                    break
                i += 1
                line = lines[i].lstrip("\n").lstrip()

            shortcut = ""
            while (not line.startswith("#")) and i < len(lines):
                shortcut += line
                if i == len(lines) - 1:
                    break
                i += 1
                line = lines[i].lstrip("\n").lstrip()

            shortcuts_dict[name] = (description, shortcut)

        # for line in lines.split("# name - "):
        #     if "\n" in line and "import" not in line:
        #         name = line[:line.index("\n")]
        #         shortcut = line[line.index("\n") + 1: -2]
        #
        #         shortcuts_dict[name] = shortcut

        return shortcuts_dict


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewShortcutsWindow()
    ex.showMaximized()
    sys.exit(app.exec_())
