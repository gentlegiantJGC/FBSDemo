import unittest
from PySide2.QtWidgets import QPushButton, QLabel
from .base_ui_test import BaseUITest


class MainWindowTest(BaseUITest.BaseUITest):
    RequiredAttributes = (
        ("button_1", QPushButton),
        ("button_2", QPushButton),
        ("button_3", QPushButton),
        ("platform", QLabel)
    )
    ui_file = "gui/mainwindow.ui"


if __name__ == '__main__':
    unittest.main()
