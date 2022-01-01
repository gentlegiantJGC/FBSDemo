from PySide2.QtCore import Slot, QMetaObject
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap
from PySide2.QtUiTools import QUiLoader


from demo.app import get_context


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ui = QUiLoader().load(get_context().get_resource("gui/mainwindow.ui"), self)
        ui.platform.setPixmap(
            QPixmap(
                get_context().get_resource("platform_logo.png")
            )
        )
        QMetaObject.connectSlotsByName(self)

    @Slot()
    def on_button_1_clicked(self):
        print("1")

    @Slot()
    def on_button_2_clicked(self):
        print("2")

    @Slot()
    def on_button_3_clicked(self):
        print("3")
