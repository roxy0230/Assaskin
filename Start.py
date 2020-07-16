import os

import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication

from UI import MainWindow
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow.MainWindow()
    ui.setupUI(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
