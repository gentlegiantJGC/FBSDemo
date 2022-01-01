import sys
from demo.app import get_context
from demo.gui.main_window import MainWindow
from PySide2.QtUiTools import QUiLoader


def main():
    get_context()

    window = MainWindow()
    window.show()
    exit_code = get_context().app.exec_()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
