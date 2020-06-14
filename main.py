import functools
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from window.controllers.static_color import ColorController
from window.window import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(window)

    ColorController(win)

    window.show()

    sys.exit(app.exec())

